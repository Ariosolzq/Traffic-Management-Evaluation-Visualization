-- MariaDB dump 10.17  Distrib 10.4.13-MariaDB, for Win64 (AMD64)
--
-- Host: localhost    Database: testbase
-- ------------------------------------------------------
-- Server version	10.4.13-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `app_image`
--

DROP TABLE IF EXISTS `app_image`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `app_image` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `image_file` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_image`
--

LOCK TABLES `app_image` WRITE;
/*!40000 ALTER TABLE `app_image` DISABLE KEYS */;
INSERT INTO `app_image` VALUES (13,'翠微小学南校区','media/image\\翠微小学南校区\\邢家伟 2023_06_16 17_17_52 翠微小学南校区 29-门口交通秩序.jpg'),(17,'北京市东城区板厂小学低部校区','media/image\\北京市东城区板厂小学低部校区\\李清霖 2023_03_23 15_02_52 北京市东城区板厂小学低部校区 42-不走斑马线.jpg'),(18,'北京市东城区板厂小学低部校区','media/image\\北京市东城区板厂小学低部校区\\李清霖 2023_03_23 15_04_07 北京市东城区板厂小学低部校区 39-非机动车闯红灯.jpg'),(19,'北京市东城区板厂小学低部校区','media/image\\北京市东城区板厂小学低部校区\\李清霖 2023_03_23 15_05_57 北京市东城区板厂小学低部校区 41-行人闯红灯.jpg'),(20,'翠微小学南校区','media/image\\翠微小学南校区\\谢祥 2023_03_23 09_25_46 翠微小学南校区 15-前方学校.jpg');
/*!40000 ALTER TABLE `app_image` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-08-18 14:52:01
