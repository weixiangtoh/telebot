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

--
-- password decode for each of the users:
-- alice1
-- bobby2
-- charlie3
-- daryl4
--

-- INSERT INTO `USER` VALUES ('alice', 'Alice NG', '$2y$10$nNEB5sQQWA9dPEovaYEcpOt3cVFpWRZN4jmMNqgvXU1cWu7TiZCkS');
-- INSERT INTO `USER` VALUES ('bobby', 'Bobby TAN', '$2y$10$1SxSjTk/mNL6ETuZBDDzJ..iWzow.bISd2cGiz6q0tG6CgTYTchHe');
-- INSERT INTO `USER` VALUES ('charlie', 'Charlie LEE', '$2y$10$v8IZ63lH3u9DfR2kg8A/oefyQIEB45x2lWBji4rBCAMBiXtPhLaDS');
-- INSERT INTO `USER` VALUES ('daryl', 'Daryl KOH', '$2y$10$/44hgwbCUNG0wUcpDH1bnek36YbLmbG0VAja5kZig2Sax/8xfnpO6');
