  -- https://quebit.com/askquebit/quebit-products/sql-server-image-and-varbinary-data-types/#:~:text=The%20IMAGE%20data%20type%20in,version%20of%20MS%20SQL%20Server. 
SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";

CREATE DATABASE IF NOT EXISTS `storeItems` 
DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `storeItems`;


DROP TABLE IF EXISTS `storeItems`;
CREATE TABLE IF NOT EXISTS `storeItems` (
	`sid` int not null,
    `itemId` int not null AUTO_INCREMENT,
    `itemName` varchar(100),
    `itemQty` int,
    `itemImage` text, -- to check again, varbinary(max) or something else
    `discountedPrice` float,
    `discountPriceQty` int,
    `originalPrice` float,
    `quota` int,
    `category` varchar(100),
    `description` varchar(200),
    `mimetype` text,
    primary key(`itemId`)

) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
