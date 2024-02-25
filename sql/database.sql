CREATE DATABASE bruteinfinitecraft;
USE bruteinfinitecraft;

--
-- Table structure for table `item`
--

DROP TABLE IF EXISTS `item`;
CREATE TABLE `item` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` text NOT NULL,
  `symbole` varchar(255) NOT NULL,
  `isNew` tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
);

--
-- Table structure for table `craft`
--

DROP TABLE IF EXISTS `craft`;
CREATE TABLE `craft` (
  `id` int NOT NULL AUTO_INCREMENT,
  `idItem1` int NOT NULL,
  `idItem2` int NOT NULL,
  `idResult` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `craft_item_FK` (`idItem1`),
  KEY `craft_item_FK_1` (`idItem2`),
  KEY `craft_item_FK_2` (`idResult`),
  CONSTRAINT `craft_item_FK` FOREIGN KEY (`idItem1`) REFERENCES `item` (`id`),
  CONSTRAINT `craft_item_FK_1` FOREIGN KEY (`idItem2`) REFERENCES `item` (`id`),
  CONSTRAINT `craft_item_FK_2` FOREIGN KEY (`idResult`) REFERENCES `item` (`id`)
);

--
-- Starting datas
--

INSERT INTO item (name, symbole) VALUES ('Water', '💧');
INSERT INTO item (name, symbole) VALUES ('Fire', '🔥');
INSERT INTO item (name, symbole) VALUES ('Wind', '🌬️');
INSERT INTO item (name, symbole) VALUES ('Earth', '🌍');
