/*
Navicat MySQL Data Transfer

Source Server         : MySQL56
Source Server Version : 50641
Source Host           : localhost:3306
Source Database       : test

Target Server Type    : MYSQL
Target Server Version : 50641
File Encoding         : 65001

Date: 2018-12-24 21:21:29
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `final_result`
-- ----------------------------
DROP TABLE IF EXISTS `final_result`;
CREATE TABLE `final_result` (
  `Name1` varchar(20) DEFAULT NULL,
  `Product1` varchar(20) DEFAULT NULL,
  `Date1` date DEFAULT NULL,
  `Result` varchar(20) DEFAULT NULL,
  `Name2` varchar(20) DEFAULT NULL,
  `Product2` varchar(20) DEFAULT NULL,
  `Date2` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of final_result
-- ----------------------------
INSERT INTO `final_result` VALUES ('Alan', 'Anta', '2017-01-05', 'TRUE', 'Alan', 'Anta', '2017-01-05');
INSERT INTO `final_result` VALUES ('Steven', 'Anta', '2017-01-09', 'TRUE', 'Steven', 'Anta', '2017-01-09');
INSERT INTO `final_result` VALUES ('Alan', 'Aokang', '2017-01-05', 'FALSE', null, null, null);
INSERT INTO `final_result` VALUES ('David', 'BMW', '2017-01-07', 'FALSE', null, null, null);
INSERT INTO `final_result` VALUES ('Michael', 'Aokang', '2017-01-08', 'FALSE', null, null, null);
INSERT INTO `final_result` VALUES (null, null, null, 'FALSE', 'David', 'Aokang', '2017-01-07');
INSERT INTO `final_result` VALUES (null, null, null, 'FALSE', 'Tony', 'BMW', '2017-01-15');
