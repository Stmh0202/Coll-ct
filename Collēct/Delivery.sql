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
-- Database: `delivery`
--
CREATE DATABASE IF NOT EXISTS `delivery` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `delivery`;

-- --------------------------------------------------------

--
-- Table structure for table `delivery_records`
--

DROP TABLE IF EXISTS `delivery_records`;
CREATE TABLE IF NOT EXISTS `delivery_records` (
  `delivery_id` int(11) NOT NULL AUTO_INCREMENT,
  `order_id` int(11) NOT NULL,
  `Location` varchar(100) NOT NULL,
  `delivery_status` char(20) NOT NULL,
  `load_type` char(20) NOT NULL,
  PRIMARY KEY (`delivery_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

INSERT INTO `delivery_records` (`delivery_id`, `order_id`, `Location`, `delivery_status`,`load_type`) VALUES
(1, 1, 'Singapore,Singapore', "Delivered","heavy"),
(2, 2, 'USA,California', "Delivered","heavy");

