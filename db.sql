drop database if exists covid;
create database covid;
use covid;


CREATE TABLE IF NOT EXISTS `POST`(
  `id` INT AUTO_INCREMENT PRIMARY KEY,
  `username` VARCHAR(50) NOT NULL,
  `request` VARCHAR(255) NOT NULL,
  `location` varchar(50) NOT NULL,
  `status` BOOLEAN NOT NULL  
) 
