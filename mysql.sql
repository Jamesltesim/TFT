-- MySQL dump 10.13  Distrib 8.0.12, for Linux (x86_64)
--
-- Host: localhost    Database: fruit_dj
-- ------------------------------------------------------
-- Server version	8.0.12

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8mb4 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `admin_juice_burden_sheet`
--

DROP TABLE IF EXISTS `admin_juice_burden_sheet`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `admin_juice_burden_sheet` (
  `id` int(11) NOT NULL,
  `name` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `apple` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='配料表 单位 （克）';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin_juice_burden_sheet`
--

LOCK TABLES `admin_juice_burden_sheet` WRITE;
/*!40000 ALTER TABLE `admin_juice_burden_sheet` DISABLE KEYS */;
/*!40000 ALTER TABLE `admin_juice_burden_sheet` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `commodity`
--

DROP TABLE IF EXISTS `commodity`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `commodity` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(60) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `price` float unsigned NOT NULL,
  `product_id` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `stock` int(10) unsigned NOT NULL COMMENT '\n',
  `category` int(10) unsigned DEFAULT NULL,
  `status` int(11) DEFAULT '0' COMMENT '0.\n1. \n2. \n',
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  UNIQUE KEY `name_UNIQUE` (`name`),
  UNIQUE KEY `product_id_UNIQUE` (`product_id`),
  KEY `c_c_key_idx` (`category`),
  CONSTRAINT `c_c_key` FOREIGN KEY (`category`) REFERENCES `commodity_category` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `commodity`
--

LOCK TABLES `commodity` WRITE;
/*!40000 ALTER TABLE `commodity` DISABLE KEYS */;
INSERT INTO `commodity` VALUES (1,'苹果',2.8,NULL,200,1,1);
/*!40000 ALTER TABLE `commodity` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `commodity_category`
--

DROP TABLE IF EXISTS `commodity_category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `commodity_category` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(80) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT=' \n   ';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `commodity_category`
--

LOCK TABLES `commodity_category` WRITE;
/*!40000 ALTER TABLE `commodity_category` DISABLE KEYS */;
INSERT INTO `commodity_category` VALUES (1,'水果');
/*!40000 ALTER TABLE `commodity_category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `commodity_convert`
--

DROP TABLE IF EXISTS `commodity_convert`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `commodity_convert` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `product_id` int(11) DEFAULT NULL,
  `name` varchar(80) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `price_money` float DEFAULT NULL,
  `price_rewardpoint` float DEFAULT NULL,
  `original_price` float DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  UNIQUE KEY `name_UNIQUE` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='\n';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `commodity_convert`
--

LOCK TABLES `commodity_convert` WRITE;
/*!40000 ALTER TABLE `commodity_convert` DISABLE KEYS */;
/*!40000 ALTER TABLE `commodity_convert` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `commodity_new_arrival`
--

DROP TABLE IF EXISTS `commodity_new_arrival`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `commodity_new_arrival` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `commodity_id` int(10) unsigned NOT NULL,
  `desc` varchar(60) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL COMMENT '\n\n\n\n',
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  KEY `c_n_key_idx` (`commodity_id`),
  CONSTRAINT `c_n_key` FOREIGN KEY (`commodity_id`) REFERENCES `commodity` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `commodity_new_arrival`
--

LOCK TABLES `commodity_new_arrival` WRITE;
/*!40000 ALTER TABLE `commodity_new_arrival` DISABLE KEYS */;
/*!40000 ALTER TABLE `commodity_new_arrival` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `commodity_recommend`
--

DROP TABLE IF EXISTS `commodity_recommend`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `commodity_recommend` (
  `id` int(10) unsigned NOT NULL,
  `commodity_id` int(10) unsigned NOT NULL,
  `desc` varchar(60) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  UNIQUE KEY `commodity_id_UNIQUE` (`commodity_id`),
  CONSTRAINT `r_c_key` FOREIGN KEY (`commodity_id`) REFERENCES `commodity` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `commodity_recommend`
--

LOCK TABLES `commodity_recommend` WRITE;
/*!40000 ALTER TABLE `commodity_recommend` DISABLE KEYS */;
/*!40000 ALTER TABLE `commodity_recommend` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `commodity_repertory`
--

DROP TABLE IF EXISTS `commodity_repertory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `commodity_repertory` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `purchase_price` float NOT NULL COMMENT '进货价',
  `time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `operator` int(11) NOT NULL COMMENT '操作员\n',
  `detail` varchar(80) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL COMMENT '商品详情\n',
  `supplier` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '供货商',
  `expiration_date` int(10) unsigned DEFAULT '0' COMMENT '保质期 （天）',
  `product_id` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT '' COMMENT '商品编号',
  PRIMARY KEY (`id`,`time`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `commodity_repertory`
--

LOCK TABLES `commodity_repertory` WRITE;
/*!40000 ALTER TABLE `commodity_repertory` DISABLE KEYS */;
/*!40000 ALTER TABLE `commodity_repertory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `order_reservation`
--

DROP TABLE IF EXISTS `order_reservation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `order_reservation` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `arrival_time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT=' ';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `order_reservation`
--

LOCK TABLES `order_reservation` WRITE;
/*!40000 ALTER TABLE `order_reservation` DISABLE KEYS */;
/*!40000 ALTER TABLE `order_reservation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `user` (
  `user_id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `nickname` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `phone_number` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `username` varchar(80) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `passwd` varchar(80) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `register_time` datetime DEFAULT CURRENT_TIMESTAMP,
  `header_icon_url` varchar(60) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `sex` int(11) DEFAULT '0',
  `login_status` tinyint(1) DEFAULT '0',
  PRIMARY KEY (`user_id`),
  UNIQUE KEY `user_id_UNIQUE` (`user_id`),
  UNIQUE KEY `phone_number_UNIQUE` (`phone_number`)
) ENGINE=InnoDB AUTO_INCREMENT=10006 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (10000,'abc','13888888888','abc','password',NULL,NULL,NULL,NULL),(10002,'abc','13888888881','abc','password',NULL,NULL,NULL,NULL),(10003,'abc','13888888882','abc','password',NULL,NULL,NULL,NULL),(10004,'abc','13888888883','abc','password',NULL,NULL,NULL,NULL),(10005,'abc','13888888885','abc','password',NULL,NULL,NULL,1);
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_address`
--

DROP TABLE IF EXISTS `user_address`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `user_address` (
  `id` int(10) unsigned NOT NULL,
  `user_id` int(11) unsigned NOT NULL,
  `address` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `u_a_key_idx` (`user_id`),
  CONSTRAINT `u_a_key` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_address`
--

LOCK TABLES `user_address` WRITE;
/*!40000 ALTER TABLE `user_address` DISABLE KEYS */;
/*!40000 ALTER TABLE `user_address` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_balance_record`
--

DROP TABLE IF EXISTS `user_balance_record`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `user_balance_record` (
  `user_id` int(11) unsigned NOT NULL,
  `record_time` datetime DEFAULT NULL,
  `detail` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `type` int(11) DEFAULT NULL,
  `desc` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `u_b_r_key_idx` (`user_id`),
  CONSTRAINT `u_b_r_key` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='  \n  ';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_balance_record`
--

LOCK TABLES `user_balance_record` WRITE;
/*!40000 ALTER TABLE `user_balance_record` DISABLE KEYS */;
/*!40000 ALTER TABLE `user_balance_record` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_grew_record`
--

DROP TABLE IF EXISTS `user_grew_record`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `user_grew_record` (
  `id` int(11) NOT NULL,
  `user_id` int(11) unsigned NOT NULL,
  `record_time` datetime DEFAULT NULL,
  `detail` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `type` int(11) DEFAULT NULL,
  `desc` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `u_g_r_key_idx` (`user_id`),
  CONSTRAINT `u_g_r_key` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='  \n\n  ';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_grew_record`
--

LOCK TABLES `user_grew_record` WRITE;
/*!40000 ALTER TABLE `user_grew_record` DISABLE KEYS */;
/*!40000 ALTER TABLE `user_grew_record` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_info`
--

DROP TABLE IF EXISTS `user_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `user_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) unsigned NOT NULL,
  `level` int(10) unsigned NOT NULL,
  `grow_score` int(11) DEFAULT NULL COMMENT '\n',
  `balance` float DEFAULT NULL,
  `reward_point` int(11) DEFAULT NULL COMMENT '\n',
  `status` int(11) DEFAULT '1' COMMENT '1. \n2. \n3. ',
  PRIMARY KEY (`id`),
  KEY `u_i_key_idx` (`user_id`),
  CONSTRAINT `u_i_key` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_info`
--

LOCK TABLES `user_info` WRITE;
/*!40000 ALTER TABLE `user_info` DISABLE KEYS */;
/*!40000 ALTER TABLE `user_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_rewardpoint_record`
--

DROP TABLE IF EXISTS `user_rewardpoint_record`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `user_rewardpoint_record` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `user_id` int(11) unsigned NOT NULL,
  `record_time` datetime DEFAULT NULL,
  `detail` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '+10 \n\n-1 1',
  `type` int(11) DEFAULT NULL COMMENT '\n\n 1  \n2 > \n3 > ',
  `desc` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `u_r_r_key_idx` (`user_id`),
  CONSTRAINT `u_r_r_key` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='  ';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_rewardpoint_record`
--

LOCK TABLES `user_rewardpoint_record` WRITE;
/*!40000 ALTER TABLE `user_rewardpoint_record` DISABLE KEYS */;
/*!40000 ALTER TABLE `user_rewardpoint_record` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-09-02 15:04:40
