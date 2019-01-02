/*
Navicat MySQL Data Transfer

Source Server         : MySQL56
Source Server Version : 50641
Source Host           : localhost:3306
Source Database       : test

Target Server Type    : MYSQL
Target Server Version : 50641
File Encoding         : 65001

Date: 2018-12-24 21:21:57
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `uni1`
-- ----------------------------
DROP TABLE IF EXISTS `uni1`;
CREATE TABLE `uni1` (
  `Name1` varchar(20) NOT NULL,
  `Product1` varchar(20) NOT NULL,
  `Date1` date NOT NULL,
  `Result` varchar(20) DEFAULT 'FALSE'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of uni1
-- ----------------------------
INSERT INTO `uni1` VALUES ('Alan', 'Aokang', '2017-01-05', 'FALSE');
INSERT INTO `uni1` VALUES ('David', 'BMW', '2017-01-07', 'FALSE');
INSERT INTO `uni1` VALUES ('Michael', 'Aokang', '2017-01-08', 'FALSE');
