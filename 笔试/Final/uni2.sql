/*
Navicat MySQL Data Transfer

Source Server         : MySQL56
Source Server Version : 50641
Source Host           : localhost:3306
Source Database       : test

Target Server Type    : MYSQL
Target Server Version : 50641
File Encoding         : 65001

Date: 2018-12-24 21:22:05
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `uni2`
-- ----------------------------
DROP TABLE IF EXISTS `uni2`;
CREATE TABLE `uni2` (
  `Name2` varchar(20) NOT NULL,
  `Product2` varchar(20) NOT NULL,
  `Date2` date NOT NULL,
  `Result` varchar(20) DEFAULT 'FALSE'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of uni2
-- ----------------------------
INSERT INTO `uni2` VALUES ('David', 'Aokang', '2017-01-07', 'FALSE');
INSERT INTO `uni2` VALUES ('Tony', 'BMW', '2017-01-15', 'FALSE');
