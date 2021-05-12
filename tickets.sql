-- MySQL dump 10.13  Distrib 5.7.25, for Linux (x86_64)
--
-- Host: localhost    Database: tickets
-- ------------------------------------------------------
-- Server version	5.7.25-0ubuntu0.18.04.2

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` text NOT NULL,
  `password` text NOT NULL,
  `token` text,
  `firstname` text,
  `lastname` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (6,'admin','admin','1e79c39d58b9c99192470fb3456c289a','admin','admin'),(7,'mamad','123','5652849c1d4ab69aafeea0e955276acc','mamad','hp'),(8,'amir','1','e76cf7f611b4e99e2abe5ffb8471a199','',''),(9,'mohammad','hp','e8ebc9a01273295d527713dd5a6fdc04','mohammad','hosseinipour');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usertickets`
--

DROP TABLE IF EXISTS `usertickets`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `usertickets` (
  `t_id` int(11) NOT NULL AUTO_INCREMENT,
  `token` text,
  `status` text,
  `subject` text,
  `body` text,
  `date` text,
  `resp` text,
  PRIMARY KEY (`t_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usertickets`
--

LOCK TABLES `usertickets` WRITE;
/*!40000 ALTER TABLE `usertickets` DISABLE KEYS */;
INSERT INTO `usertickets` VALUES (5,'5652849c1d4ab69aafeea0e955276acc','close','slm','111','2019-04-07 12:32:29.251044','aaaa'),(6,'5652849c1d4ab69aafeea0e955276acc','inrogress','khobi?','2222','2019-04-07 12:32:46.529737',NULL),(7,'5652849c1d4ab69aafeea0e955276acc','open','khobam','3333','2019-04-07 12:33:03.385102','chetoori googooli?'),(8,'e76cf7f611b4e99e2abe5ffb8471a199','open','mamad khobi?','are','2019-04-07 13:41:24.981704',NULL),(9,'e76cf7f611b4e99e2abe5ffb8471a199','open','aaa','aaaaaa','2019-04-07 13:41:40.820499',NULL),(10,'e8ebc9a01273295d527713dd5a6fdc04','inrogress','hi','body xD','2019-04-19 00:01:33.954733','respond xD');
/*!40000 ALTER TABLE `usertickets` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-04-19  1:12:20
