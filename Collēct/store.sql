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
CREATE DATABASE IF NOT EXISTS `store` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `store`;

-- --------------------------------------------------------

--
-- Table structure for table `store`
--

DROP TABLE IF EXISTS `store`;
CREATE TABLE IF NOT EXISTS `store` (
  `sid` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `description` varchar(500) NOT NULL,
  `address` varchar(200) NOT NULL,
  `phone` int(8) NOT NULL,
  `area` varchar(20) NOT NULL,
  `photo` text NOT NULL,
  `operating_hours` varchar(200) NOT NULL,
  PRIMARY KEY (`sid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `store`
--

INSERT INTO `store` (`sid`, `name`, `description`, `address`, `phone`, `area`, `photo`, `operating_hours`) VALUES
(1, 'Teck Whye Aquarium', 'Aquarium shop in Singapore selling fish and song birds including White Rumped Shama, Mata Puteh', '26 Teck Whye Ln, Singapore 680026', 98765678, 'west','https://res.cloudinary.com/collect/image/upload/v1648464329/samples/collect/Aquarium.jpg', '9am-6pm daily'),
(2, 'Clementi Time', 'Small family owned business in the heartland. Run by a friendly couple!
Offers a wide array of services such as battery & Strap replacements. Watch repairs and servicing. Sells a good selection of Japanese brand watches.', '442 Clementi Ave 3, #01-113, Singapore 120442', 98765678, 'west','https://res.cloudinary.com/collect/image/upload/v1648464404/samples/collect/Clementi.png','9am-6pm daily'),
(3, 'Toko Warisan Trading', 'Small store selling all your spices needed for malay dishes!', '374 Bukit Batok Street 31, Block 374, Singapore 650374', 98765678, 'west','https://res.cloudinary.com/collect/image/upload/v1648464411/samples/collect/Biscuit.png', '9am-6pm daily')
; COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
