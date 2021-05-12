import os.path
import torndb
import tornado.escape
import tornado.httpserver
import tornado.ioloop
import tornado.options
import os
from binascii import hexlify
import tornado.web
from tornado.options import define, options
import datetime


define("port", default=1104, help="run on the given port", type=int)
define("mysql_host", default="127.0.0.1:3306", help="blog database host")
define("mysql_database", default="tickets", help="blog database name")
define("mysql_user", default="x", help="blog database user")
define("mysql_password", default="y", help="blog database password")

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            #GET METHOD :
            (r"/authcheck&([^&]+)&([^&]+)", authcheck),
            (r"/getticketmod&([^&]+)", getticketmod),
            (r"/getticketcli&([^&]+)", getticketcli),
            # POST METHOD :
            (r"/signup", signup),
            (r"/restoticketmod", restoticketmod),
            (r"/changestatus", changestatus),
            (r"/sendticket", sendticket),
            (r"/closeticket", closeticket),
            (r".*", defaulthandler),
        ]
        settings = dict()
        super(Application, self).__init__(handlers, **settings)
        self.db = torndb.Connection(
            host=options.mysql_host, database=options.mysql_database,
            user=options.mysql_user, password=options.mysql_password)


class BaseHandler(tornado.web.RequestHandler):
    @property
    def db(self):
        return self.application.db
    def check_user(self,user):
        resuser = self.db.get("SELECT * from users where username = %s",user)
        if resuser:
            return True
        else :
            return False

    def check_TOKEN(self,token):
        resuser = self.db.get("SELECT * from users where token = %s", token)
        if resuser:
            return True
        else:
            return False
    def check_auth(self,username,password):
        resuser = self.db.get("SELECT * from users where username = %s and password = %s", username,password)
        if resuser:
            return True
        else:
            return False


class defaulthandler(BaseHandler):
    def get(self):
        output = {'code':'404'}
        self.write(output)

    def post(self, *args, **kwargs):
        output = {'code':'404'}
        self.write(output)


class signup(BaseHandler):
    def post(self, *args, **kwargs):
        username = self.get_argument('username')
        password = self.get_argument('password')
        firstname=self.get_argument('firstname')
        lastname=self.get_argument('lastname')
        if not self.check_user(username):
            token = str(hexlify(os.urandom(16)).decode())
            self.db.execute("INSERT INTO users (username, password,token,firstname,lastname) "
                                      "values (%s,%s,%s,%s,%s) "
                                      , username, password, token, firstname, lastname)
            output = {'message:': 'Signed Up Successfully',
                      'code': '200'}
            self.write(output)
        else:
            output = {'code': '404'}
            self.write(output)


class authcheck(BaseHandler):
    def get(self, *args, **kwargs):
        if self.check_auth(args[0],args[1]):
            user = self.db.get("SELECT * from users where username = %s and password = %s", args[0], args[1])
            output = {'message': 'Logged in Successfully',
                      'code':'200',
                      'token':user.token,}
            self.write(output)
        else:
            output = {'code': '404'}
            self.write(output)


class getticketmod(BaseHandler):
    def get(self, *args, **kwargs):
        if self.check_TOKEN(args[0]):
            x=[]
            x = self.db.query("SELECT * FROM usertickets")
            output = {'tickets': "there are "+str(len(x))+" tickets",
                      'code': "200"}
            for i in range(1,len(x)+1):
                block={"subject" : x[i-1]['subject'],
                       "body": x[i-1]['body'],
                       "status": x[i-1]["status"],
                       "id": x[i-1]["t_id"],
                       "date": x[i-1]["date"]}
                output.update({"block"+str(i-1): block})
            self.write(output)


        else:
            output = {'code': '404'}
            self.write(output)


class restoticketmod(BaseHandler):
    def post(self, *args, **kwargs):
        token= self.get_argument('token')
        id = self.get_argument('id')
        message=self.get_argument('message')
        if self.check_TOKEN(token):
            self.db.execute("UPDATE usertickets SET resp = %s WHERE token = %s AND t_id = %s",message,token,id)
            a="Response to Ticket With id -"+id+ "- Sent Successfully"
            output = {'message:': a,
                      'code': '200'}
            self.write(output)
        else:
            output = {'code': '404'}
            self.write(output)


class changestatus(BaseHandler):
    def post(self, *args, **kwargs):
        token= self.get_argument('token')
        id = self.get_argument('id')
        status=self.get_argument('status')
        if self.check_TOKEN(token):
            self.db.execute("UPDATE usertickets SET status = %s WHERE token = %s AND t_id = %s",status,token,id)
            a="status of Ticket With id -"+id+ "- changed Successfully"
            output = {'message:': a,
                      'code': '200'}
            self.write(output)
        else:
            output = {'code': '404'}
            self.write(output)


class sendticket(BaseHandler):
    def post(self, *args, **kwargs):
        token= self.get_argument('token')
        subject = self.get_argument('subject')
        body=self.get_argument('body')
        if self.check_TOKEN(token):
            self.db.execute("INSERT INTO usertickets (token,status,subject,body,date)""values(%s,%s,%s,%s,%s)", token, "open",subject,body,str(datetime.datetime.now()))
            last_record=self.db.get("SELECT MAX(t_id) FROM usertickets")
            output = {'message:': 'the message sent successfully',
                      'id' : last_record,
                      'code': '200'}
            self.write(output)
        else:
            output = {'code': '404'}
            self.write(output)


class getticketcli(BaseHandler):
    def get(self, *args, **kwargs):
        if self.check_TOKEN(args[0]):
            x=[]
            x = self.db.query("SELECT * FROM usertickets WHERE token=%s",args[0])
            output = {'tickets': "there are " + str(len(x)) + " tickets",
                      'code': "200"}
            for i in range(1, len(x) + 1):
                block = {"subject": x[i - 1]['subject'],
                         "body": x[i - 1]['body'],
                         "status": x[i - 1]["status"],
                         "id": x[i - 1]["t_id"],
                         "date": x[i - 1]["date"]}
                output.update({"block " + str(i - 1): block})
            self.write(output)
        else:
            output = {'code': '404'}
            self.write(output)


class closeticket(BaseHandler):
    def post(self, *args, **kwargs):
        token= self.get_argument('token')
        id = self.get_argument('id')
        if self.check_TOKEN(token):
            self.db.execute("UPDATE usertickets SET status =%s WHERE token = %s and t_id=%s ","close",token,id)
            a="status of ticket with id -"+id+"- closed successfully"
            output = {'message:': a,
                      'id' : id,
                      'code': '200'}
            self.write(output)
        else:
            output = {'code': '404'}
            self.write(output)





def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    print ("listening...")
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()
