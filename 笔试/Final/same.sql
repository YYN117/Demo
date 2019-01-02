/*
Navicat MySQL Data Transfer

Source Server         : MySQL56
Source Server Version : 50641
Source Host           : localhost:3306
Source Database       : test

Target Server Type    : MYSQL
Target Server Version : 50641
File Encoding         : 65001

Date: 2018-12-24 21:21:40
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `same`
-- ----------------------------
DROP TABLE IF EXISTS `same`;
CREATE TABLE `same` (
  `Name1` varchar(20) NOT NULL,
  `Product1` varchar(20) NOT NULL,
  `Date1` date NOT NULL,
  `Result` varchar(20) DEFAULT 'TRUE',
  `Name2` varchar(20) NOT NULL,
  `Product2` varchar(20) NOT NULL,
  `Date2` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of same
-- ----------------------------
INSERT INTO `same` VALUES ('Alan', 'Anta', '2017-01-05', 'TRUE', 'Alan', 'Anta', '2017-01-05');
INSERT INTO `same` VALUES ('Steven', 'Anta', '2017-01-09', 'TRUE', 'Steven', 'Anta', '2017-01-09');
