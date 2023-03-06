-- phpMyAdmin SQL Dump
-- version 4.7.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Jan 14, 2019 at 06:42 AM
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
-- Database: `book`
--
CREATE DATABASE IF NOT EXISTS `gb_tracking` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `gb_tracking`;

-- --------------------------------------------------------

--
-- Table structure for table `books`
--

DROP TABLE IF EXISTS `gb_tracking`;
CREATE TABLE IF NOT EXISTS `gb_tracking` (
  `gbId` varchar(10) NOT NULL,
  `storeId` varchar(64) NOT NULL,
  `itemId` varchar(10) NOT NULL,
  `quota` int(2) NOT NULL,
  `cid` varchar(10) NOT NULL,
  `timeStamp` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `numItems` int(2) NOT NULL,
  PRIMARY KEY (`gbId`,`cid`) 
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `customer'
--

-- INSERT INTO `customer` (`gb_id`, `store_id`, `item_id`, `quota`, `cid`, `timestamp`) VALUES
-- (1, '2efnjr4', 1, '10', 10),
-- (2, 'mjdeidju3', 2, '10',10),
-- (3, 'hdbhac2', 3, '10', 10);
-- COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;