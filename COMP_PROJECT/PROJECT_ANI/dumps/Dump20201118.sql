-- MySQL dump 10.13  Distrib 8.0.22, for Win64 (x86_64)
--
-- Host: localhost    Database: project
-- ------------------------------------------------------
-- Server version	8.0.22

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `project`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `project` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `project`;

--
-- Table structure for table `booking`
--

DROP TABLE IF EXISTS `booking`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `booking` (
  `Booking_ID` int NOT NULL AUTO_INCREMENT,
  `Phone_No` int DEFAULT NULL,
  `Destination` varchar(40) DEFAULT NULL,
  `Mode_of_travel` varchar(30) DEFAULT 'flight',
  `status` varchar(20) DEFAULT 'pending',
  PRIMARY KEY (`Booking_ID`),
  KEY `Phone_No` (`Phone_No`),
  CONSTRAINT `booking_ibfk_1` FOREIGN KEY (`Phone_No`) REFERENCES `client` (`Phone_No`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `booking`
--

LOCK TABLES `booking` WRITE;
/*!40000 ALTER TABLE `booking` DISABLE KEYS */;
/*!40000 ALTER TABLE `booking` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `client`
--

DROP TABLE IF EXISTS `client`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `client` (
  `client_id` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(30) DEFAULT NULL,
  `Phone_No` int NOT NULL,
  `Address` varchar(100) DEFAULT NULL,
  `user_Id` varchar(10) NOT NULL,
  PRIMARY KEY (`Phone_No`),
  UNIQUE KEY `user_Id_UNIQUE` (`user_Id`),
  UNIQUE KEY `client_id_UNIQUE` (`client_id`)
) ENGINE=InnoDB AUTO_INCREMENT=1864466512 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `client`
--

LOCK TABLES `client` WRITE;
/*!40000 ALTER TABLE `client` DISABLE KEYS */;
INSERT INTO `client` VALUES (1864466510,'Amit',971750192,'103g sector-17 Faridabad','C16556');
/*!40000 ALTER TABLE `client` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `destination`
--

DROP TABLE IF EXISTS `destination`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `destination` (
  `Booking_ID` int DEFAULT NULL,
  `hotel` varchar(30) DEFAULT NULL,
  `duration` varchar(20) DEFAULT NULL,
  `Pay` int DEFAULT '10000',
  KEY `Booking_ID` (`Booking_ID`),
  CONSTRAINT `destination_ibfk_1` FOREIGN KEY (`Booking_ID`) REFERENCES `booking` (`Booking_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `destination`
--

LOCK TABLES `destination` WRITE;
/*!40000 ALTER TABLE `destination` DISABLE KEYS */;
/*!40000 ALTER TABLE `destination` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `payment`
--

DROP TABLE IF EXISTS `payment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `payment` (
  `Booking_Id` int DEFAULT NULL,
  `payment` int DEFAULT NULL,
  `tax` decimal(5,2) DEFAULT '0.18',
  `discount` decimal(5,2) DEFAULT '0.10',
  `Total_pay` decimal(5,2) DEFAULT NULL,
  KEY `Booking_Id` (`Booking_Id`),
  CONSTRAINT `payment_ibfk_1` FOREIGN KEY (`Booking_Id`) REFERENCES `booking` (`Booking_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `payment`
--

LOCK TABLES `payment` WRITE;
/*!40000 ALTER TABLE `payment` DISABLE KEYS */;
/*!40000 ALTER TABLE `payment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `user_id` varchar(10) NOT NULL,
  `Password` varchar(200) NOT NULL,
  `Type` varchar(30) DEFAULT 'client',
  PRIMARY KEY (`user_id`),
  UNIQUE KEY `Password_UNIQUE` (`Password`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES ('A1654','password','Admin'),('C16556','PASSWRD','client');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'project'
--

--
-- Current Database: `emp`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `emp` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `emp`;

--
-- Table structure for table `dept`
--

DROP TABLE IF EXISTS `dept`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dept` (
  `Dept_No` int NOT NULL AUTO_INCREMENT,
  `Dept_Name` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`Dept_No`)
) ENGINE=InnoDB AUTO_INCREMENT=13216136 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dept`
--

LOCK TABLES `dept` WRITE;
/*!40000 ALTER TABLE `dept` DISABLE KEYS */;
INSERT INTO `dept` VALUES (13216132,'Mechincal'),(13216133,'Accounts'),(13216134,'Sales'),(13216135,'Technical');
/*!40000 ALTER TABLE `dept` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `emp1`
--

DROP TABLE IF EXISTS `emp1`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `emp1` (
  `Emp_No` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(30) DEFAULT NULL,
  `Designation` varchar(10) DEFAULT NULL,
  `Dept_No` int DEFAULT NULL,
  `salary` int DEFAULT NULL,
  PRIMARY KEY (`Emp_No`),
  KEY `Dept_No` (`Dept_No`),
  CONSTRAINT `emp1_ibfk_1` FOREIGN KEY (`Dept_No`) REFERENCES `dept` (`Dept_No`)
) ENGINE=InnoDB AUTO_INCREMENT=127 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `emp1`
--

LOCK TABLES `emp1` WRITE;
/*!40000 ALTER TABLE `emp1` DISABLE KEYS */;
INSERT INTO `emp1` VALUES (124,'Ajay','clerk',13216132,119495),(125,'SHUBHAM','SUPERVISOR',13216134,1209970),(126,'AAKASH','MANAGER',13216135,1087225);
/*!40000 ALTER TABLE `emp1` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `job`
--

DROP TABLE IF EXISTS `job`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `job` (
  `Sno` int NOT NULL,
  `Area` varchar(10) DEFAULT NULL,
  `App_date` date DEFAULT NULL,
  `Salary` int DEFAULT NULL,
  `Retd_date` date DEFAULT NULL,
  `Dept` varchar(10) NOT NULL,
  UNIQUE KEY `Sno` (`Sno`),
  CONSTRAINT `job_ibfk_1` FOREIGN KEY (`Sno`) REFERENCES `personal` (`Empno`),
  CONSTRAINT `job_chk_1` CHECK ((`Area` in (_utf8mb4'Agra',_utf8mb4'Mathura',_utf8mb4'Delhi',_utf8mb4'Pune'))),
  CONSTRAINT `job_chk_2` CHECK ((`Salary` between 4000 and 10000))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `job`
--

LOCK TABLES `job` WRITE;
/*!40000 ALTER TABLE `job` DISABLE KEYS */;
/*!40000 ALTER TABLE `job` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `personal`
--

DROP TABLE IF EXISTS `personal`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `personal` (
  `Empno` int NOT NULL,
  `Name` varchar(10) NOT NULL,
  `Dobirth` date DEFAULT NULL,
  `Native_place` varchar(10) DEFAULT NULL,
  `Hobby` varchar(10) NOT NULL,
  PRIMARY KEY (`Empno`),
  CONSTRAINT `personal_chk_1` CHECK ((`Dobirth` > _cp850'1960-01-12')),
  CONSTRAINT `personal_chk_2` CHECK ((`Native_place` in (_cp850'Delhi',_cp850'Mumbai',_cp850'Allahabad',_cp850'Pune')))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `personal`
--

LOCK TABLES `personal` WRITE;
/*!40000 ALTER TABLE `personal` DISABLE KEYS */;
/*!40000 ALTER TABLE `personal` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student1`
--

DROP TABLE IF EXISTS `student1`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student1` (
  `No` int DEFAULT NULL,
  `Name` varchar(20) DEFAULT NULL,
  `Stipend` decimal(5,2) DEFAULT NULL,
  `Stream` varchar(10) DEFAULT NULL,
  `AvgMark` decimal(3,1) DEFAULT NULL,
  `Grade` varchar(1) DEFAULT NULL,
  `Class` varchar(3) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student1`
--

LOCK TABLES `student1` WRITE;
/*!40000 ALTER TABLE `student1` DISABLE KEYS */;
INSERT INTO `student1` VALUES (1,'KARAN',400.00,'MEDICAL',78.5,'B','12B'),(2,'DIVAKAR',450.00,'COMMERCE',89.5,'A','11C'),(3,'DIVYA',300.00,'COMMERCE',68.6,'C','12C'),(4,'ARUN',350.00,'HUMANITES',73.1,'B','12C'),(5,'SABINA',500.00,'NONMEDICAL',90.6,'A','11A'),(6,'JOHN',400.00,'MEDICAL',75.4,'B','12B'),(7,'ROBERT',250.00,'HUMANITES',64.4,'C','11A'),(8,'RUBINA',450.00,'NONMEDICAL',88.5,'A','12A'),(9,'VIKAS',500.00,'NONMEDICAL',92.0,'A','12A'),(10,'MOHAN',300.00,'COMMERCE',67.5,'C','12C');
/*!40000 ALTER TABLE `student1` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'emp'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-11-18 23:26:38
