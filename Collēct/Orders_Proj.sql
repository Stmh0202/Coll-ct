-- phpMyAdmin SQL Dump
-- version 4.7.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Jun 12, 2020 at 02:17 AM
-- Server version: 5.7.19
-- PHP Version: 7.1.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `orders_proj`
--
CREATE DATABASE IF NOT EXISTS `orders_proj` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `orders_proj`;

-- --------------------------------------------------------

--
-- Table structure for table `orders_proj`
--

DROP TABLE IF EXISTS `orders_proj`;
CREATE TABLE IF NOT EXISTS `orders_proj` (
  `order_id` int(11) NOT NULL AUTO_INCREMENT,
  `customer_id` int(11) NOT NULL,
  `itemName` varchar(100) NOT NULL,
  `quantity` int(3) NOT NULL,
  `DiscountedQtyPrice` FLOAT(4) NOT NULL,
  PRIMARY KEY (`order_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

--
-- Dumping data for table `orders_proj`
--
INSERT INTO `orders_proj` (`order_id`, `customer_id`, `itemName` , `quantity`,`DiscountedQtyPrice`) VALUES
(1, 3, 'Detergent', 4, 32.20);

