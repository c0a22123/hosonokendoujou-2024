-- MySQL dump 10.13  Distrib 9.1.0, for Linux (x86_64)
--
-- Host: localhost    Database: MyDatabase
-- ------------------------------------------------------
-- Server version	9.1.0

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
-- Table structure for table `another_infomation`
--

DROP TABLE IF EXISTS `another_infomation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `another_infomation` (
  `event_id` int NOT NULL,
  `anspot_name` varchar(100) NOT NULL,
  `anspot_opentime` time DEFAULT NULL,
  `anspot_closed` time DEFAULT NULL,
  `anspot_transportation` varchar(255) DEFAULT NULL,
  `anspot_png` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`event_id`,`anspot_name`),
  CONSTRAINT `another_infomation_ibfk_1` FOREIGN KEY (`event_id`) REFERENCES `event` (`event_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `another_infomation`
--

LOCK TABLES `another_infomation` WRITE;
/*!40000 ALTER TABLE `another_infomation` DISABLE KEYS */;
/*!40000 ALTER TABLE `another_infomation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bingo`
--

DROP TABLE IF EXISTS `bingo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bingo` (
  `user_id` int NOT NULL,
  `event_id` int NOT NULL,
  `bingo_row0` varchar(10) DEFAULT NULL,
  `bingo_row1` varchar(10) DEFAULT NULL,
  `bingo_row2` varchar(10) DEFAULT NULL,
  `bingo_row3` varchar(10) DEFAULT NULL,
  `bingo_row4` varchar(10) DEFAULT NULL,
  `bingo_row5` varchar(10) DEFAULT NULL,
  `bingo_row6` varchar(10) DEFAULT NULL,
  `bingo_row7` varchar(10) DEFAULT NULL,
  `bingo_row8` varchar(10) DEFAULT NULL,
  `total_bingo` int DEFAULT NULL,
  `bingo_row0_updated_at` timestamp NULL DEFAULT NULL,
  `bingo_row1_updated_at` timestamp NULL DEFAULT NULL,
  `bingo_row2_updated_at` timestamp NULL DEFAULT NULL,
  `bingo_row3_updated_at` timestamp NULL DEFAULT NULL,
  `bingo_row4_updated_at` timestamp NULL DEFAULT NULL,
  `bingo_row5_updated_at` timestamp NULL DEFAULT NULL,
  `bingo_row6_updated_at` timestamp NULL DEFAULT NULL,
  `bingo_row7_updated_at` timestamp NULL DEFAULT NULL,
  `bingo_row8_updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`user_id`,`event_id`),
  KEY `event_id` (`event_id`),
  CONSTRAINT `bingo_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `login` (`user_id`),
  CONSTRAINT `bingo_ibfk_2` FOREIGN KEY (`event_id`) REFERENCES `event` (`event_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bingo`
--

LOCK TABLES `bingo` WRITE;
/*!40000 ALTER TABLE `bingo` DISABLE KEYS */;
INSERT INTO `bingo` VALUES (17,1,'0','0','0','0','0','0','0','0','0',0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(18,1,'1','1','1','1','1','1','1','1','1',0,'2024-11-04 05:13:42','2024-11-04 05:09:44','2024-11-04 05:03:24','2024-11-04 05:20:59','2024-11-04 05:37:17','2024-11-04 05:24:35',NULL,NULL,'2024-11-03 06:00:54'),(19,1,'0','1','0','1','0','1','0','0','1',0,NULL,'2024-11-02 21:02:50',NULL,'2024-11-02 21:11:22',NULL,NULL,NULL,NULL,'2024-11-02 21:03:12'),(20,1,'1','1','1','1','1','1','1','1','1',0,'2024-11-08 07:00:24',NULL,'2024-11-08 06:58:34','2024-11-07 03:33:09','2024-11-08 23:55:42','2024-11-07 03:42:00',NULL,'2024-11-07 03:47:23','2024-11-07 03:43:26'),(22,1,'0','0','0','0','0','0','0','0','0',0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(23,1,'1','1','1','1','1','1','1','1','1',0,'2024-11-04 01:48:57','2024-11-04 01:51:44','2024-11-04 08:30:06','2024-11-06 23:16:28','2024-11-04 01:42:41','2024-11-06 23:18:21','2024-11-04 01:55:10','2024-11-04 07:08:45','2024-11-07 07:17:52'),(24,1,'0','0','0','0','0','0','0','0','0',0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(25,1,'0','0','0','0','0','0','0','0','0',0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(26,1,'0','0','0','0','0','0','0','0','1',0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(27,1,'0','0','0','0','0','0','0','0','0',0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(28,1,'0','0','0','0','0','0','0','0','0',0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(29,1,'0','0','0','0','0','0','0','0','0',0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(30,1,'0','1','0','0','1','0','1','1','0',0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(31,1,'0','1','0','0','1','0','1','1','0',0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(32,1,'0','1','0','0','1','0','1','1','0',0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(33,1,'0','1','0','0','1','0','1','1','0',0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(34,1,'0','0','0','0','0','0','0','0','0',0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(35,1,'0','0','0','0','0','0','0','0','0',0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(36,1,'0','0','0','0','0','0','0','0','0',0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(37,1,'0','0','0','0','0','0','0','0','0',0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(38,1,'0','0','0','0','0','0','0','0','0',0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(39,1,'0','0','0','0','0','0','0','0','0',0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(40,1,'1','1','1','1','1','1','1','1','1',0,'2024-11-03 07:38:35','2024-11-03 07:09:53','2024-11-03 08:16:41','2024-11-03 07:42:33','2024-11-04 07:11:47','2024-11-03 07:45:28','2024-11-03 07:48:07','2024-11-03 07:51:20','2024-11-03 08:11:34'),(41,1,'0','0','0','0','0','0','0','0','0',0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(43,1,'0','0','0','0','0','0','0','0','0',0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(44,1,'0','0','0','0','0','0','0','0','0',0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(45,1,'1','1','1','1','1','1','1','1','1',0,'2024-11-03 06:11:53','2024-11-03 06:16:13','2024-11-03 06:27:22','2024-11-03 06:04:30','2024-11-04 05:54:39','2024-11-03 06:00:47','2024-11-03 05:50:31','2024-11-03 05:57:43','2024-11-03 06:32:53'),(46,1,'0','0','0','0','0','0','0','0','0',0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(47,1,'1','1','1','1','1','1','1','1','1',0,'2024-11-04 05:52:09','2024-11-04 06:27:30','2024-11-04 06:18:07','2024-11-04 05:44:58','2024-11-04 06:50:59','2024-11-04 06:35:50','2024-11-04 06:01:00','2024-11-04 06:05:34','2024-11-04 06:13:15'),(48,1,'0','1','0','0','0','0','0','0','0',0,NULL,'2024-11-03 04:26:09',NULL,NULL,NULL,NULL,NULL,NULL,NULL),(49,1,'0','0','0','0','0','0','0','0','0',0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(50,1,'0','0','0','0','0','0','0','0','0',0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(51,1,'0','0','0','0','0','0','0','0','0',0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(52,1,'0','0','0','0','0','0','0','0','0',0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(53,1,'0','1','0','0','0','0','1','0','0',0,NULL,'2024-11-04 06:56:00',NULL,NULL,NULL,NULL,'2024-11-04 07:01:54',NULL,NULL),(54,1,'0','0','0','0','0','0','0','0','0',0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(55,1,'1','1','1','1','1','1','1','1','1',0,'2024-11-05 02:24:12','2024-11-05 02:29:14','2024-11-05 02:34:54','2024-11-05 02:17:20','2024-11-05 02:05:41','2024-11-05 02:56:42','2024-11-05 02:46:19','2024-11-05 02:49:14','2024-11-05 02:42:01'),(56,1,'1','1','1','1','1','1','1','1','1',0,'2024-11-05 02:24:32','2024-11-05 02:29:43','2024-11-05 02:35:59','2024-11-05 02:18:08','2024-11-05 02:01:32','2024-11-05 02:57:07','2024-11-05 02:46:22','2024-11-05 02:49:32','2024-11-05 02:42:05'),(57,1,'0','0','0','0','0','0','0','0','0',0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(58,1,'0','0','0','0','0','0','0','0','0',0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(59,1,'0','0','0','0','0','0','0','0','0',0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(60,1,'1','1','1','1','1','1','1','1','1',0,'2024-11-08 05:18:50','2024-11-08 03:40:02','2024-11-08 04:16:20','2024-11-08 03:26:51','2024-11-08 02:31:59','2024-11-08 02:07:11','2024-11-08 04:50:36','2024-11-08 04:53:34','2024-11-08 05:06:48'),(61,1,'0','0','0','0','0','0','0','0','0',0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(63,1,'1','1','1','1','1','1','1','1','1',9,'2024-11-08 04:22:15','2024-11-08 04:22:15','2024-11-08 04:22:15','2024-11-08 04:22:15','2024-11-08 04:22:15','2024-11-08 04:22:15','2024-11-08 04:22:15','2024-11-08 04:22:15','2024-11-08 04:22:15'),(64,1,'0','0','0','0','0','0','0','0','0',0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(65,1,'1','1','1','1','1','1','0','1','1',0,'2024-11-08 04:53:56','2024-11-08 05:02:02','2024-11-08 05:07:55','2024-11-08 04:09:04','2024-11-08 03:53:48','2024-11-08 04:05:07',NULL,'2024-11-08 03:06:58','2024-11-08 05:12:06'),(66,1,'0','0','0','0','0','0','0','0','0',0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(67,1,'1','1','0','1','1','1','1','1','1',0,'2024-11-09 00:34:39','2024-11-09 00:31:12',NULL,'2024-11-09 00:24:09','2024-11-09 00:49:39','2024-11-09 01:10:07','2024-11-09 01:14:41','2024-11-09 01:36:10','2024-11-09 01:40:29'),(68,1,'0','0','0','0','0','0','0','0','0',0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(69,1,'1','0','1','1','1','1','1','0','1',0,'2024-11-09 01:49:53',NULL,'2024-11-09 04:46:42','2024-11-09 02:14:11','2024-11-09 03:34:06','2024-11-09 04:28:43','2024-11-09 04:25:29',NULL,'2024-11-09 04:52:24'),(70,1,'0','0','0','1','1','1','1','1','0',0,NULL,NULL,NULL,'2024-11-09 02:31:37','2024-11-09 02:45:50','2024-11-09 03:34:13','2024-11-09 03:40:17','2024-11-09 03:52:06',NULL),(71,1,'0','1','1','0','1','0','1','1','0',0,NULL,'2024-11-09 02:34:34','2024-11-09 05:00:04',NULL,'2024-11-09 03:04:32',NULL,'2024-11-09 03:55:57','2024-11-09 03:41:57',NULL),(72,1,'1','1','1','1','1','1','1','1','1',0,'2024-11-09 03:08:43','2024-11-09 06:12:15','2024-11-10 02:41:16','2024-11-09 03:27:07','2024-11-10 02:03:28','2024-11-09 04:35:34','2024-11-09 05:10:40','2024-11-09 05:30:38','2024-11-09 05:39:49'),(73,1,'0','0','0','0','0','0','0','0','0',0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(74,1,'0','0','0','0','0','0','0','0','0',0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(75,1,'0','0','0','0','0','0','0','0','0',0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(76,1,'1','1','1','1','1','1','1','1','1',0,'2024-11-10 04:37:38','2024-11-09 07:36:50','2024-11-10 04:48:40','2024-11-09 07:41:05','2024-11-10 03:45:01','2024-11-09 07:45:24','2024-11-09 06:42:55','2024-11-09 06:39:54','2024-11-10 04:54:44'),(77,1,'0','0','0','0','0','0','0','0','0',0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(78,1,'1','1','1','1','1','1','1','1','1',0,'2024-11-10 00:25:43','2024-11-10 01:46:43','2024-11-10 01:55:23','2024-11-10 00:36:41','2024-11-10 00:58:05','2024-11-10 01:19:57','2024-11-10 01:34:34','2024-11-10 02:09:16','2024-11-10 01:59:16'),(79,1,'0','0','0','0','0','0','0','0','0',0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(80,1,'1','1','1','1','1','1','1','1','1',0,'2024-11-10 01:35:38','2024-11-10 01:32:18','2024-11-10 02:15:50','2024-11-10 01:25:01','2024-11-10 01:45:17','2024-11-10 02:09:24','2024-11-10 01:20:25','2024-11-10 02:11:38','2024-11-10 02:13:08'),(81,1,'0','0','0','0','0','0','0','0','0',0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(82,1,'1','1','1','1','1','1','1','1','1',0,'2024-11-10 03:12:11','2024-11-10 04:55:14','2024-11-10 05:13:17','2024-11-10 04:44:04','2024-11-10 03:28:14','2024-11-10 04:46:30','2024-11-10 05:27:12','2024-11-10 05:03:20','2024-11-10 05:20:11'),(83,1,'1','1','1','1','1','1','1','1','1',0,'2024-11-10 04:24:30','2024-11-10 04:21:28','2024-11-10 04:14:52','2024-11-10 03:19:59','2024-11-10 03:33:43','2024-11-10 03:58:14','2024-11-10 04:01:45','2024-11-10 04:03:51','2024-11-10 04:10:22'),(84,1,'0','1','0','0','0','0','1','1','0',0,NULL,'2024-11-10 05:26:55',NULL,NULL,NULL,NULL,'2024-11-10 05:13:36','2024-11-10 05:12:36',NULL),(85,1,'0','0','0','0','0','0','0','0','0',0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `bingo` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb3 */ ;
/*!50003 SET character_set_results = utf8mb3 */ ;
/*!50003 SET collation_connection  = utf8mb3_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `update_bingo_row0_timestamp` BEFORE UPDATE ON `bingo` FOR EACH ROW BEGIN
    IF NEW.bingo_row0 <> OLD.bingo_row0 THEN
        SET NEW.bingo_row0_updated_at = CURRENT_TIMESTAMP;
    END IF;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb3 */ ;
/*!50003 SET character_set_results = utf8mb3 */ ;
/*!50003 SET collation_connection  = utf8mb3_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `update_bingo_row1_timestamp` BEFORE UPDATE ON `bingo` FOR EACH ROW BEGIN
    IF NEW.bingo_row1 <> OLD.bingo_row1 THEN
        SET NEW.bingo_row1_updated_at = CURRENT_TIMESTAMP;
    END IF;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb3 */ ;
/*!50003 SET character_set_results = utf8mb3 */ ;
/*!50003 SET collation_connection  = utf8mb3_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `update_bingo_row2_timestamp` BEFORE UPDATE ON `bingo` FOR EACH ROW BEGIN
    IF NEW.bingo_row2 <> OLD.bingo_row2 THEN
        SET NEW.bingo_row2_updated_at = CURRENT_TIMESTAMP;
    END IF;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb3 */ ;
/*!50003 SET character_set_results = utf8mb3 */ ;
/*!50003 SET collation_connection  = utf8mb3_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `update_bingo_row3_timestamp` BEFORE UPDATE ON `bingo` FOR EACH ROW BEGIN
    IF NEW.bingo_row3 <> OLD.bingo_row3 THEN
        SET NEW.bingo_row3_updated_at = CURRENT_TIMESTAMP;
    END IF;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb3 */ ;
/*!50003 SET character_set_results = utf8mb3 */ ;
/*!50003 SET collation_connection  = utf8mb3_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `update_bingo_row4_timestamp` BEFORE UPDATE ON `bingo` FOR EACH ROW BEGIN
    IF NEW.bingo_row4 <> OLD.bingo_row4 THEN
        SET NEW.bingo_row4_updated_at = CURRENT_TIMESTAMP;
    END IF;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb3 */ ;
/*!50003 SET character_set_results = utf8mb3 */ ;
/*!50003 SET collation_connection  = utf8mb3_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `update_bingo_row5_timestamp` BEFORE UPDATE ON `bingo` FOR EACH ROW BEGIN
    IF NEW.bingo_row5 <> OLD.bingo_row5 THEN
        SET NEW.bingo_row5_updated_at = CURRENT_TIMESTAMP;
    END IF;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb3 */ ;
/*!50003 SET character_set_results = utf8mb3 */ ;
/*!50003 SET collation_connection  = utf8mb3_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `update_bingo_row6_timestamp` BEFORE UPDATE ON `bingo` FOR EACH ROW BEGIN
    IF NEW.bingo_row6 <> OLD.bingo_row6 THEN
        SET NEW.bingo_row6_updated_at = CURRENT_TIMESTAMP;
    END IF;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb3 */ ;
/*!50003 SET character_set_results = utf8mb3 */ ;
/*!50003 SET collation_connection  = utf8mb3_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `update_bingo_row7_timestamp` BEFORE UPDATE ON `bingo` FOR EACH ROW BEGIN
    IF NEW.bingo_row7 <> OLD.bingo_row7 THEN
        SET NEW.bingo_row7_updated_at = CURRENT_TIMESTAMP;
    END IF;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb3 */ ;
/*!50003 SET character_set_results = utf8mb3 */ ;
/*!50003 SET collation_connection  = utf8mb3_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `update_bingo_row8_timestamp` BEFORE UPDATE ON `bingo` FOR EACH ROW BEGIN
    IF NEW.bingo_row8 <> OLD.bingo_row8 THEN
        SET NEW.bingo_row8_updated_at = CURRENT_TIMESTAMP;
    END IF;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `coupon`
--

DROP TABLE IF EXISTS `coupon`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `coupon` (
  `user_id` int NOT NULL,
  `event_id` int NOT NULL,
  `1bingo_count` int DEFAULT NULL,
  `4bingo_count` int DEFAULT NULL,
  `8bingo_count` int DEFAULT NULL,
  PRIMARY KEY (`user_id`,`event_id`),
  KEY `event_id` (`event_id`),
  CONSTRAINT `coupon_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `login` (`user_id`),
  CONSTRAINT `coupon_ibfk_2` FOREIGN KEY (`event_id`) REFERENCES `event` (`event_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `coupon`
--

LOCK TABLES `coupon` WRITE;
/*!40000 ALTER TABLE `coupon` DISABLE KEYS */;
/*!40000 ALTER TABLE `coupon` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `coupon_store`
--

DROP TABLE IF EXISTS `coupon_store`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `coupon_store` (
  `store_name` varchar(100) NOT NULL,
  `store_infomation` text,
  `store_opentime` time DEFAULT NULL,
  `store_closed` time DEFAULT NULL,
  `store_transportation` varchar(255) DEFAULT NULL,
  `store_money` decimal(10,2) DEFAULT NULL,
  `store_png` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`store_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `coupon_store`
--

LOCK TABLES `coupon_store` WRITE;
/*!40000 ALTER TABLE `coupon_store` DISABLE KEYS */;
/*!40000 ALTER TABLE `coupon_store` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `event`
--

DROP TABLE IF EXISTS `event`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `event` (
  `event_id` int NOT NULL AUTO_INCREMENT,
  `event_name` varchar(100) DEFAULT NULL,
  `start_date` date DEFAULT NULL,
  `end_date` date DEFAULT NULL,
  PRIMARY KEY (`event_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `event`
--

LOCK TABLES `event` WRITE;
/*!40000 ALTER TABLE `event` DISABLE KEYS */;
INSERT INTO `event` VALUES (1,'','2024-11-01','2024-11-10');
/*!40000 ALTER TABLE `event` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `login`
--

DROP TABLE IF EXISTS `login`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `login` (
  `user_id` int NOT NULL AUTO_INCREMENT,
  `user_name` varchar(50) NOT NULL,
  `password` varchar(255) NOT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=86 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `login`
--

LOCK TABLES `login` WRITE;
/*!40000 ALTER TABLE `login` DISABLE KEYS */;
INSERT INTO `login` VALUES (14,'mogusa_ym6886@yahoo.co.jp','ym8413484','2024-11-02 20:11:50','2024-11-02 20:11:57'),(17,'c0a22097','test','2024-11-02 20:11:50','2024-11-02 20:11:57'),(18,'sssss','stk2247127','2024-11-02 20:11:50','2024-11-02 20:11:57'),(19,'shimada','test2','2024-11-02 20:11:50','2024-11-02 20:11:57'),(20,'kanananami','hino2024','2024-11-02 20:11:50','2024-11-02 20:11:57'),(22,'Tomochan','20180823dm','2024-11-02 20:11:50','2024-11-02 20:11:57'),(23,'のり','shuku1124','2024-11-02 20:11:50','2024-11-02 20:11:57'),(24,'せん','456','2024-11-02 20:11:50','2024-11-02 20:11:57'),(25,'denden','ty1105ty','2024-11-02 20:11:50','2024-11-02 20:11:57'),(26,'rika.b0512@gmail.com','gazhes-Dacnav-qipce7','2024-11-02 20:11:50','2024-11-02 20:11:57'),(27,'user123','pass','2024-11-02 20:11:50','2024-11-02 20:11:57'),(28,'ふう車','k1001f1020','2024-11-02 20:11:50','2024-11-02 20:11:57'),(29,'桜','miyuki0309','2024-11-02 20:11:50','2024-11-02 20:11:57'),(30,'kenken','kentama','2024-11-02 20:11:50','2024-11-02 20:11:57'),(31,'じゅんや','ponya0925','2024-11-02 20:11:50','2024-11-02 20:11:57'),(32,'くはらなおき','Cookie1046','2024-11-02 20:11:50','2024-11-02 20:11:57'),(33,'bunmonsi','Kanon0217','2024-11-02 20:11:50','2024-11-02 20:11:57'),(34,'とろとろまん','momoka1108','2024-11-02 20:11:50','2024-11-02 20:11:57'),(35,'MOKO','arashi212','2024-11-02 20:11:50','2024-11-02 20:11:57'),(36,'☆きよみ☆','love0129','2024-11-02 20:11:50','2024-11-02 20:11:57'),(37,'幸','bipxec-Cugnot-7magdi','2024-11-02 20:11:50','2024-11-02 20:11:57'),(38,'nomitaka@ezweb.ne.jp','aristtrist0916','2024-11-02 20:11:50','2024-11-02 20:11:57'),(39,'なお','705','2024-11-02 20:11:50','2024-11-02 20:11:57'),(40,'ouka','sakura0112','2024-11-02 20:11:50','2024-11-02 20:11:57'),(41,'ぽんちゃんたろう','shibata','2024-11-02 20:11:50','2024-11-02 20:11:57'),(42,'ぽんちゃんたろう','shibatayukiko','2024-11-02 20:11:50','2024-11-02 20:11:57'),(43,'ホーちゃん','hochan','2024-11-02 20:11:50','2024-11-02 20:11:57'),(44,'hiepnsx','27161992','2024-11-02 20:11:50','2024-11-02 20:11:57'),(45,'モチダ　マコト','tamabingo4215','2024-11-03 00:56:18','2024-11-03 00:56:18'),(46,'Hyla','hiroko','2024-11-03 01:25:36','2024-11-03 01:25:36'),(47,'ほかちゃん','hoka3626','2024-11-03 02:13:23','2024-11-03 02:13:23'),(48,'のあのあ','noah1978','2024-11-03 04:22:16','2024-11-03 04:22:16'),(49,'たむら','3107','2024-11-03 08:56:18','2024-11-03 08:56:18'),(50,'ヤーナ','PWbingo1118','2024-11-03 13:01:47','2024-11-03 13:01:47'),(51,'りか','rika0426','2024-11-03 22:30:57','2024-11-03 22:30:57'),(52,'kumamami','fujisan07311003','2024-11-04 04:38:11','2024-11-04 04:38:11'),(53,'たっつー','xejcod-quTsik-guvra7','2024-11-04 06:52:56','2024-11-04 06:52:56'),(54,'ちひろ','wakuwaku33','2024-11-04 06:55:01','2024-11-04 06:55:01'),(55,'ポニョ','1101','2024-11-04 12:45:23','2024-11-04 12:45:23'),(56,'ゆいぱぱ','hysak1974','2024-11-05 00:38:09','2024-11-05 00:38:09'),(57,'樽座','prime510','2024-11-05 04:29:37','2024-11-05 04:29:37'),(58,'marimo','703T39ra','2024-11-06 03:31:19','2024-11-06 03:31:19'),(59,'chitarou9559-ya@ezweb.ne.jp','chisato','2024-11-06 04:51:29','2024-11-06 04:51:29'),(60,'はらきん','ki50ki50','2024-11-08 01:51:54','2024-11-08 01:51:54'),(61,'hiromaro','3965hiro','2024-11-08 02:06:57','2024-11-08 02:06:57'),(63,'MM','bingo','2024-11-08 02:11:06','2024-11-08 02:11:06'),(64,'hotate27','Ss10271027','2024-11-08 02:13:17','2024-11-08 02:13:17'),(65,'air.sho1337@gmail.com','xajton-8tyfxe-Cejnag','2024-11-08 03:06:26','2024-11-08 03:06:26'),(66,'ぱる','pal6139','2024-11-09 00:12:41','2024-11-09 00:12:41'),(67,'alert@jcom.zaq.ne.jp','hoyahoya','2024-11-09 00:21:43','2024-11-09 00:21:43'),(68,'nf','nf231461','2024-11-09 01:26:04','2024-11-09 01:26:04'),(69,'Londan','SYRZKU','2024-11-09 01:48:36','2024-11-09 01:48:36'),(70,'qnarrk31178ai@docomo.ne.jp','BackBetB1006','2024-11-09 02:07:22','2024-11-09 02:07:22'),(71,'みんくる','jta021','2024-11-09 02:32:31','2024-11-09 02:32:31'),(72,'fshinon','49541974','2024-11-09 03:07:11','2024-11-09 03:07:11'),(73,'あーく','zyhvax-kyksAn-fudge1','2024-11-09 03:18:45','2024-11-09 03:18:45'),(74,'mieko.oka@icloud.com','matuba1614','2024-11-09 04:17:59','2024-11-09 04:17:59'),(75,'たけ','hiro','2024-11-09 06:21:13','2024-11-09 06:21:13'),(76,'Ico','uilolp','2024-11-09 06:39:17','2024-11-09 06:39:17'),(77,'mieko.oka@icloud.com','okada1614','2024-11-09 12:28:22','2024-11-09 12:28:22'),(78,'katsu3211','wada24510','2024-11-10 00:24:02','2024-11-10 00:24:02'),(79,'颯斗','12raining','2024-11-10 00:31:11','2024-11-10 00:31:11'),(80,'とっしー','toshi390','2024-11-10 00:33:00','2024-11-10 00:33:00'),(81,'U','free0000','2024-11-10 01:13:24','2024-11-10 01:13:24'),(82,'あこ','19811116','2024-11-10 03:10:45','2024-11-10 03:10:45'),(83,'ひの','Yk7gNYfTcCwRiiQ','2024-11-10 03:18:57','2024-11-10 03:18:57'),(84,'hideous3693@gmail.com','801','2024-11-10 04:41:39','2024-11-10 04:41:39'),(85,'test3','test3','2024-11-11 09:55:54','2024-11-11 09:55:54');
/*!40000 ALTER TABLE `login` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `prize_exchange`
--

DROP TABLE IF EXISTS `prize_exchange`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `prize_exchange` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `event_id` int NOT NULL,
  `exchanged` tinyint(1) DEFAULT '0',
  `exchange_date` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  KEY `event_id` (`event_id`),
  CONSTRAINT `prize_exchange_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `login` (`user_id`),
  CONSTRAINT `prize_exchange_ibfk_2` FOREIGN KEY (`event_id`) REFERENCES `event` (`event_id`)
) ENGINE=InnoDB AUTO_INCREMENT=79 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `prize_exchange`
--

LOCK TABLES `prize_exchange` WRITE;
/*!40000 ALTER TABLE `prize_exchange` DISABLE KEYS */;
INSERT INTO `prize_exchange` VALUES (1,19,1,1,'2024-11-01 01:24:38'),(2,20,1,1,'2024-11-09 00:26:11'),(4,22,1,0,'2024-11-01 03:33:22'),(5,23,1,1,'2024-11-07 07:20:18'),(6,24,1,0,'2024-11-01 03:48:41'),(7,25,1,0,'2024-11-01 05:02:43'),(8,26,1,0,'2024-11-01 06:26:12'),(9,14,1,0,'2024-11-01 07:54:31'),(12,17,1,0,'2024-11-01 07:54:31'),(13,18,1,1,'2024-11-04 05:52:51'),(22,27,1,0,'2024-11-02 05:25:58'),(23,28,1,0,'2024-11-01 12:14:14'),(24,29,1,0,'2024-11-02 05:22:39'),(25,30,1,1,'2024-11-02 06:18:10'),(26,31,1,1,'2024-11-02 06:17:57'),(27,32,1,1,'2024-11-02 06:17:41'),(28,33,1,1,'2024-11-02 06:17:24'),(29,34,1,0,'2024-11-02 05:01:29'),(30,35,1,0,'2024-11-02 05:03:00'),(31,36,1,0,'2024-11-02 05:06:08'),(32,37,1,0,'2024-11-02 05:09:19'),(33,38,1,0,'2024-11-02 05:25:26'),(34,39,1,0,'2024-11-02 05:27:51'),(35,40,1,1,'2024-11-04 07:34:46'),(36,41,1,0,'2024-11-02 05:55:28'),(37,43,1,0,'2024-11-02 06:57:50'),(38,44,1,0,'2024-11-02 17:16:45'),(39,45,1,1,'2024-11-04 06:52:30'),(40,46,1,0,'2024-11-03 01:25:36'),(41,47,1,1,'2024-11-04 06:59:42'),(42,48,1,0,'2024-11-03 04:22:16'),(43,49,1,0,'2024-11-03 08:56:19'),(44,50,1,0,'2024-11-03 13:01:47'),(45,51,1,0,'2024-11-03 22:30:57'),(46,52,1,0,'2024-11-04 04:38:11'),(47,53,1,0,'2024-11-04 06:52:56'),(48,54,1,0,'2024-11-04 06:55:01'),(49,55,1,1,'2024-11-06 01:43:40'),(50,56,1,1,'2024-11-06 01:44:35'),(51,57,1,0,'2024-11-05 04:29:37'),(52,58,1,0,'2024-11-06 03:31:19'),(53,59,1,0,'2024-11-06 04:51:29'),(54,60,1,1,'2024-11-08 05:30:24'),(55,61,1,0,'2024-11-08 02:06:57'),(56,63,1,1,'2024-11-08 03:10:00'),(57,64,1,0,'2024-11-08 02:13:17'),(58,65,1,1,'2024-11-08 05:14:43'),(59,66,1,0,'2024-11-09 00:12:41'),(60,67,1,0,'2024-11-09 00:21:43'),(61,68,1,0,'2024-11-09 01:26:04'),(62,69,1,1,'2024-11-09 04:59:08'),(63,70,1,0,'2024-11-09 02:07:22'),(64,71,1,1,'2024-11-09 03:43:24'),(65,72,1,1,'2024-11-10 02:51:24'),(66,73,1,0,'2024-11-09 03:18:46'),(67,74,1,0,'2024-11-09 04:18:00'),(68,75,1,0,'2024-11-09 06:21:13'),(69,76,1,1,'2024-11-10 04:57:14'),(70,77,1,0,'2024-11-09 03:10:00'),(71,78,1,1,'2024-11-10 02:10:14'),(72,79,1,0,'2024-11-10 00:31:11'),(73,80,1,1,'2024-11-10 02:19:42'),(74,81,1,0,'2024-11-10 01:13:24'),(75,82,1,1,'2024-11-10 05:53:32'),(76,83,1,1,'2024-11-10 04:04:07'),(77,84,1,0,'2024-11-10 04:41:39'),(78,85,1,0,'2024-11-11 09:55:54');
/*!40000 ALTER TABLE `prize_exchange` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `spot_infomation`
--

DROP TABLE IF EXISTS `spot_infomation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `spot_infomation` (
  `spot_name` varchar(100) NOT NULL,
  `spot_opentime` time DEFAULT NULL,
  `spot_closed` time DEFAULT NULL,
  `spot_transportation` varchar(255) DEFAULT NULL,
  `spot_png` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`spot_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `spot_infomation`
--

LOCK TABLES `spot_infomation` WRITE;
/*!40000 ALTER TABLE `spot_infomation` DISABLE KEYS */;
/*!40000 ALTER TABLE `spot_infomation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `store_infomation`
--

DROP TABLE IF EXISTS `store_infomation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `store_infomation` (
  `event_id` int NOT NULL,
  `store_name` varchar(100) NOT NULL,
  PRIMARY KEY (`event_id`,`store_name`),
  KEY `store_name` (`store_name`),
  CONSTRAINT `store_infomation_ibfk_1` FOREIGN KEY (`event_id`) REFERENCES `event` (`event_id`),
  CONSTRAINT `store_infomation_ibfk_2` FOREIGN KEY (`store_name`) REFERENCES `coupon_store` (`store_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `store_infomation`
--

LOCK TABLES `store_infomation` WRITE;
/*!40000 ALTER TABLE `store_infomation` DISABLE KEYS */;
/*!40000 ALTER TABLE `store_infomation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_infomation`
--

DROP TABLE IF EXISTS `user_infomation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_infomation` (
  `user_id` int NOT NULL,
  `gendar` varchar(10) DEFAULT NULL,
  `birthday` varchar(10) DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`user_id`),
  CONSTRAINT `user_infomation_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `login` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_infomation`
--

LOCK TABLES `user_infomation` WRITE;
/*!40000 ALTER TABLE `user_infomation` DISABLE KEYS */;
INSERT INTO `user_infomation` VALUES (14,'女性','60代','2024-11-02 20:08:31'),(17,'男性','20代','2024-11-02 20:08:31'),(18,'女性','30代','2024-11-02 20:08:31'),(19,'男性','30代','2024-11-02 20:08:31'),(20,'その他','30代','2024-11-02 20:08:31'),(22,'女性','30代','2024-11-02 20:08:31'),(23,'女性','40代','2024-11-02 20:08:31'),(24,'女性','50代','2024-11-02 20:08:31'),(25,'男性','30代','2024-11-02 20:08:31'),(26,'女性','40代','2024-11-02 20:08:31'),(27,'男性','20代','2024-11-02 20:08:31'),(28,'女性','30代','2024-11-02 20:08:31'),(29,'女性','30代','2024-11-02 20:08:31'),(30,'男性','20代','2024-11-02 20:08:31'),(31,'男性','20代','2024-11-02 20:08:31'),(32,'男性','20代','2024-11-02 20:08:31'),(33,'女性','20代','2024-11-02 20:08:31'),(34,'男性','50代','2024-11-02 20:08:31'),(35,'女性','50代','2024-11-02 20:08:31'),(36,'女性','60代','2024-11-02 20:08:31'),(37,'女性','40代','2024-11-02 20:08:31'),(38,'男性','50代','2024-11-02 20:08:31'),(39,'女性','50代','2024-11-02 20:08:31'),(40,'女性','30代','2024-11-02 20:08:31'),(41,'女性','40代','2024-11-02 20:08:31'),(42,'女性','40代','2024-11-02 20:08:31'),(43,'女性','60代','2024-11-02 20:08:31'),(44,'男性','30代','2024-11-02 20:08:31'),(45,'男性','50代','2024-11-03 00:56:18'),(46,'女性','40代','2024-11-03 01:25:36'),(47,'女性','50代','2024-11-03 02:13:23'),(48,'女性','40代','2024-11-03 04:22:16'),(49,'女性','30代','2024-11-03 08:56:18'),(50,'女性','50代','2024-11-03 13:01:47'),(51,'女性','20代','2024-11-03 22:30:57'),(52,'女性','60代','2024-11-04 04:38:11'),(53,'男性','30代','2024-11-04 06:52:56'),(54,'男性','30代','2024-11-04 06:55:01'),(55,'女性','40代','2024-11-04 12:45:23'),(56,'男性','40代','2024-11-05 00:38:09'),(57,'男性','40代','2024-11-05 04:29:37'),(58,'女性','30代','2024-11-06 03:31:19'),(59,'女性','60代','2024-11-06 04:51:29'),(60,'女性','50代','2024-11-08 01:51:54'),(61,'男性','70代以上','2024-11-08 02:06:57'),(63,'女性','60代','2024-11-08 02:11:06'),(64,'男性','30代','2024-11-08 02:13:17'),(65,'男性','20代','2024-11-08 03:06:26'),(66,'男性','50代','2024-11-09 00:12:41'),(67,'男性','60代','2024-11-09 00:21:43'),(68,'女性','50代','2024-11-09 01:26:04'),(69,'女性','60代','2024-11-09 01:48:36'),(70,'女性','60代','2024-11-09 02:07:22'),(71,'女性','60代','2024-11-09 02:32:31'),(72,'女性','50代','2024-11-09 03:07:11'),(73,'男性','40代','2024-11-09 03:18:45'),(74,'女性','70代以上','2024-11-09 04:17:59'),(75,'女性','40代','2024-11-09 06:21:13'),(76,'女性','30代','2024-11-09 06:39:17'),(77,'女性','70代以上','2024-11-09 12:28:22'),(78,'男性','50代','2024-11-10 00:24:02'),(79,'男性','40代','2024-11-10 00:31:11'),(80,'男性','50代','2024-11-10 00:33:00'),(81,'男性','50代','2024-11-10 01:13:24'),(82,'女性','40代','2024-11-10 03:10:45'),(83,'男性','40代','2024-11-10 03:18:57'),(84,'男性','40代','2024-11-10 04:41:39'),(85,'男性','20代','2024-11-11 09:55:54');
/*!40000 ALTER TABLE `user_infomation` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-11-11 10:18:06
