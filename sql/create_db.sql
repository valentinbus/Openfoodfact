SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";
--
--
CREATE TABLE IF NOT EXISTS `category` (
  `id` smallint(3) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;
--
--
CREATE TABLE IF NOT EXISTS `product` (
  `id` smallint(3) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `store` varchar(100) NOT NULL,
  `link` text NOT NULL,
  `nutriscore` varchar(1) NOT NULL,
  `category_fk` smallint(3) NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `product_ibfk_2` FOREIGN KEY (`category_fk`) REFERENCES `category`(`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;
--
--
CREATE TABLE IF NOT EXISTS `substitue` (
  `id` smallint(3) NOT NULL AUTO_INCREMENT,
  `id_product to substitue_fk` smallint(3) NOT NULL,
  `id_product substitue_fk` smallint(3) NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `substitue_ibfk_3` FOREIGN KEY (`id_product substitue_fk`) REFERENCES `product` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `substitue_ibfk_4` FOREIGN KEY (`id_product to substitue_FK`) REFERENCES `product` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;