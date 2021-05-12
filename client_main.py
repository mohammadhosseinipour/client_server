import requests
import os
import time
import platform
import sys

from BeautifulSoup import BeautifulSoup

PARAMS = CMD = USERNAME = PASSWORD=SUBJECT=BODY =FIRSTNAME=LASTNAME= TOKEN =USERSTATUS=USERTOKEN= MESSAGE=ID= ""
HOST="127.0.0.1"
PORT ="1104"


def __postcr__():
    return "http://"+HOST+":"+PORT+"/"+CMD+"?"


def __token__():
    return "http://" + HOST + ":" + PORT + "/" + CMD + "&" + TOKEN

def __authgetcr__():
    return "http://"+HOST+":"+PORT+"/"+CMD+"&"+USERNAME+"&"+PASSWORD


def clear():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
       os.system('clear')


def show_func_user():
    print("USERNAME : "+USERNAME+"\n"+"TOKEN : " + TOKEN)
    print("""What Do You Prefer To Do (user):
    1. send ticket
    2. get ticket
    3. close ticket
    4. Logout
    5. Exi t
    """)


def show_func_admin():
    print("ADMIN "+"\n"+"TOKEN : " + TOKEN)
    print("""What Do You Prefer To Do (ADMIN):
    1. get tickets
    2. answer the ticktes
    3. change status of the tickets
    4. Logout
    5. Exit
    """)


while True:
    clear()
    print(""""welcome to our ticket manager Please choose what you want to do:
          1.sign in
          2.signup
          3.exit
          """)
    status= sys.stdin.readline()
    if status[:-1] == '1':
        clear()
        while True:
            print("USERNAME : ")
            USERNAME = sys.stdin.readline()[:-1]
            print("PASSWORD : ")
            PASSWORD = sys.stdin.readline()[:-1]
            CMD = "authcheck"
            r = requests.get(__authgetcr__()).json()
            if str(r['code']) == '200':
                clear()
                print("USERNAME AND PASSWORD IS CORRECT\nLogging You in ...")
                TOKEN = str(r['token'])
                time.sleep(2)
                break
            else:
                clear()
                print("USERNAME AND PASSWORD IS INCORRECT\nTRY AGAIN ...")
                time.sleep(2)
        if USERNAME=="admin":
            while True :
                clear()
                show_func_admin()
                func_type = sys.stdin.readline()
                if func_type[:-1] == '1':
                    clear()
                    CMD= "getticketmod"
                    data=requests.get(__token__()).json()
                    print(str(data).replace(",","\n").replace("u\'","").replace('\'',""))
                    time.sleep(20)


                if func_type[:-1] == '2':
                    clear()
                    print ("Enter the TOKEN that u wanna respond:")
                    USERTOKEN=sys.stdin.readline()[:-1]
                    print ("enter the user's id")
                    ID=sys.stdin.readline()[:-1]
                    CMD ="restoticketmod"
                    print ("Enter the MESSAGE that u wanna respond:")
                    MESSAGE=sys.stdin.readline()[:-1]
                    PARAMS={'token':USERTOKEN,'id':ID,'message':MESSAGE}
                    data=requests.post(__postcr__(),PARAMS).json()
                    print (str(data).replace(",","\n").replace("u\'","").replace('\'',""))
                    print("""the message sent""")
                    time.sleep(5)


                if func_type[:-1] == '3':
                    clear()
                    print("enter Token:")
                    USERTOKEN=sys.stdin.readline()[:-1]
                    print ("enter the user's id")
                    ID = sys.stdin.readline()[:-1]
                    CMD="changestatus"
                    print("""statuses:
                    1.close
                    2.in progress
                    3.open""")
                    USERSTATUS=sys.stdin.readline()[:-1]
                    if USERSTATUS=="1":
                        PARAMS={'token':USERTOKEN,'id':ID,'status':'close'}
                    elif USERSTATUS=="2":
                        PARAMS = {'token': USERTOKEN,'id':ID, 'status': 'inrogress'}
                    elif USERSTATUS=="3":
                        PARAMS = {'token': USERTOKEN, 'id':ID ,'status': 'open'}
                    else:
                        print("wrong choice ")
                        time.sleep(5)
                        continue
                    data=requests.post(__postcr__(), PARAMS).json()
                    print(str(data).replace(",","\n").replace("u\'","").replace('\'',""))
                    print("status changed...")
                    time.sleep(5)

                if func_type[:-1] == '4':
                    break

                if func_type[:-1] == '5':
                    sys.exit()

        else:
            while True :
                clear()
                show_func_user()
                func_type = sys.stdin.readline()
                if func_type[:-1] == '1':
                    clear()
                    CMD= "sendticket"
                    print ("Enter the subject:")
                    SUBJECT=sys.stdin.readline()[:-1]
                    print ("Enter the Body:")
                    BODY=sys.stdin.readline()[:-1]
                    PARAMS={'token':TOKEN,'subject':SUBJECT,'body':BODY}
                    data=requests.post(__postcr__(),PARAMS).json()
                    print (str(data).replace(",","\n").replace("u\'","").replace('\'',""))
                    print("ticket sent...")
                    time.sleep(5)

                if func_type[:-1] == '2':
                    clear()
                    CMD = "getticketcli"
                    data = requests.get(__token__()).json()
                    print(str(data).replace(",","\n").replace("u\'","").replace('\'',""))
                    print("ticket taked")
                    time.sleep(20)

                if func_type[:-1] == '3':
                    clear()
                    print ("enter the your id")
                    ID = sys.stdin.readline()[:-1]
                    CMD="closeticket"
                    PARAMS={'token':TOKEN,'id':ID}
                    data=requests.post(__postcr__(),PARAMS).json()
                    print(str(data).replace(",","\n").replace("u\'","").replace('\'',""))
                    print("status changed!...")
                    time.sleep(5)

                if func_type[:-1] == '4':
                    break

                if func_type[:-1] == '5':
                    sys.exit()



    elif status[:-1] == '2':
        clear()
        while True:
            print("To Create New Account Enter The Authentication")
            print("USERNAME : ")
            USERNAME = sys.stdin.readline()[:-1]
            print("PASSWORD : ")
            PASSWORD = sys.stdin.readline()[:-1]
            FIRSTNAME=LASTNAME=""
            print ("""Wanna add you name?
            1.yes
            2.no""")
            ans=sys.stdin.readline()[:-1]
            CMD = "signup"
            PARAMS = {'username': USERNAME, 'password': PASSWORD, 'firstname': FIRSTNAME, 'lastname': LASTNAME}
            if ans=="1":
                print("Firstname : ")
                FIRSTNAME= sys.stdin.readline()[:-1]
                print("Lastname : ")
                LASTNAME=sys.stdin.readline()[:-1]
                PARAMS = {'username': USERNAME, 'password': PASSWORD, 'firstname': FIRSTNAME, 'lastname': LASTNAME}
            clear()
            r = requests.post(__postcr__(), PARAMS).json()
            if str(r['code']) == "200":
                print("Your Acount Is Created\n" + "Your Username :" + USERNAME )
                time.sleep(5)
                break
            else:
                print(r['code'] + "\n" + "Try Again")
                time.sleep(5)
                clear()

    elif status[:-1] == '3':
        sys.exit()


    else:
        print("Wrong Choose Try Again")




























