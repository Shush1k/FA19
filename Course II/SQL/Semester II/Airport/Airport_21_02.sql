-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema Airport
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `Airport` ;

-- -----------------------------------------------------
-- Schema Airport
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `Airport` DEFAULT CHARACTER SET utf8 ;
USE `Airport` ;

-- -----------------------------------------------------
-- Table `Airport`.`City`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Airport`.`City` ;

CREATE TABLE IF NOT EXISTS `Airport`.`City` (
  `idCity` INT NOT NULL AUTO_INCREMENT,
  `CityName` VARCHAR(45) NOT NULL,
  `country` VARCHAR(45) NOT NULL,
  `state` VARCHAR(45) NULL,
  PRIMARY KEY (`idCity`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Airport`.`Airport`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Airport`.`Airport` ;

CREATE TABLE IF NOT EXISTS `Airport`.`Airport` (
  `idAirport` INT NOT NULL AUTO_INCREMENT,
  `AirportName` VARCHAR(45) NOT NULL,
  `email` VARCHAR(45) NULL,
  `telephone` CHAR(20) NULL,
  `details` VARCHAR(45) NULL,
  `idCity` INT NOT NULL,
  PRIMARY KEY (`idAirport`),
  INDEX `fk_Airport_City_idx` (`idCity` ASC) VISIBLE,
  CONSTRAINT `fk_Airport_City`
    FOREIGN KEY (`idCity`)
    REFERENCES `Airport`.`City` (`idCity`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Airport`.`Rout`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Airport`.`Rout` ;

CREATE TABLE IF NOT EXISTS `Airport`.`Rout` (
  `idRout` INT NOT NULL AUTO_INCREMENT,
  `city_from` VARCHAR(45) NOT NULL,
  `city_to` VARCHAR(45) NOT NULL,
  `cost` INT NOT NULL,
  `flightTime` TIME NOT NULL,
  PRIMARY KEY (`idRout`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Airport`.`Plane`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Airport`.`Plane` ;

CREATE TABLE IF NOT EXISTS `Airport`.`Plane` (
  `idPlane` INT NOT NULL AUTO_INCREMENT,
  `model` VARCHAR(45) NOT NULL,
  `seats` INT NOT NULL,
  `madeYear` INT NOT NULL,
  `boardNumb` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idPlane`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Airport`.`Schedule`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Airport`.`Schedule` ;

CREATE TABLE IF NOT EXISTS `Airport`.`Schedule` (
  `idSchedule` INT NOT NULL,
  `flight` VARCHAR(45) NOT NULL,
  `classType` VARCHAR(45) NOT NULL,
  `Date` DATE NOT NULL,
  `idPlane` INT NOT NULL,
  `idRout` INT NOT NULL,
  PRIMARY KEY (`idSchedule`),
  INDEX `fk_idRout_idx` (`idRout` ASC) VISIBLE,
  INDEX `fk_idPlane_idx` (`idPlane` ASC) VISIBLE,
  CONSTRAINT `fk_idRout`
    FOREIGN KEY (`idRout`)
    REFERENCES `Airport`.`Rout` (`idRout`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_idPlane`
    FOREIGN KEY (`idPlane`)
    REFERENCES `Airport`.`Plane` (`idPlane`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Airport`.`Passenger`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Airport`.`Passenger` ;

CREATE TABLE IF NOT EXISTS `Airport`.`Passenger` (
  `PID` INT NOT NULL AUTO_INCREMENT,
  `FName` VARCHAR(35) NOT NULL,
  `LName` VARCHAR(45) NOT NULL,
  `birthdate` DATE NOT NULL,
  `sex` VARCHAR(1) NOT NULL,
  `passport` VARCHAR(45) NOT NULL,
  `telephone` CHAR(20) NULL,
  `address` VARCHAR(90) NULL,
  PRIMARY KEY (`PID`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Airport`.`Sale`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Airport`.`Sale` ;

CREATE TABLE IF NOT EXISTS `Airport`.`Sale` (
  `idSale` INT NOT NULL AUTO_INCREMENT,
  `count` INT NOT NULL,
  `cost` INT NOT NULL,
  `idSchedule` INT NOT NULL,
  PRIMARY KEY (`idSale`),
  INDEX `fk_idSchedule_idx` (`idSchedule` ASC) VISIBLE,
  CONSTRAINT `fk_idSchedule`
    FOREIGN KEY (`idSchedule`)
    REFERENCES `Airport`.`Schedule` (`idSchedule`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Airport`.`User`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Airport`.`User` ;

CREATE TABLE IF NOT EXISTS `Airport`.`User` (
  `idUser` INT NOT NULL AUTO_INCREMENT,
  `login` VARCHAR(45) NOT NULL,
  `password` VARCHAR(45) NOT NULL,
  `status` VARCHAR(45) NOT NULL,
  `FName` VARCHAR(45) NOT NULL,
  `LName` VARCHAR(45) NOT NULL,
  `passport` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idUser`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Airport`.`Ticket`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Airport`.`Ticket` ;

CREATE TABLE IF NOT EXISTS `Airport`.`Ticket` (
  `idTicket` INT NOT NULL AUTO_INCREMENT,
  `ticketsCount` INT NOT NULL,
  `seatCount` INT NOT NULL,
  `PID` INT NOT NULL,
  `idSale` INT NOT NULL,
  `idUser` INT NOT NULL,
  PRIMARY KEY (`idTicket`),
  INDEX `fk_PID_idx` (`PID` ASC) VISIBLE,
  INDEX `fk_idSale_idx` (`idSale` ASC) VISIBLE,
  INDEX `fk_idUser_idx` (`idUser` ASC) VISIBLE,
  CONSTRAINT `fk_PID`
    FOREIGN KEY (`PID`)
    REFERENCES `Airport`.`Passenger` (`PID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_idSale`
    FOREIGN KEY (`idSale`)
    REFERENCES `Airport`.`Sale` (`idSale`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_idUser`
    FOREIGN KEY (`idUser`)
    REFERENCES `Airport`.`User` (`idUser`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Airport`.`Airline`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Airport`.`Airline` ;

CREATE TABLE IF NOT EXISTS `Airport`.`Airline` (
  `idAirline` INT NOT NULL,
  `AirlineName` VARCHAR(90) NOT NULL,
  `idCity` INT NOT NULL,
  `email` VARCHAR(45) NULL,
  `telephone` CHAR(20) NULL,
  PRIMARY KEY (`idAirline`))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

-- -----------------------------------------------------
-- Data for table `Airport`.`City`
-- -----------------------------------------------------
START TRANSACTION;
USE `Airport`;
INSERT INTO `Airport`.`City` (`idCity`, `CityName`, `country`, `state`) VALUES (1, 'Moscow', 'Russia', NULL);
INSERT INTO `Airport`.`City` (`idCity`, `CityName`, `country`, `state`) VALUES (2, 'SaintPeterburg', 'Russia', NULL);
INSERT INTO `Airport`.`City` (`idCity`, `CityName`, `country`, `state`) VALUES (3, 'Kazan', 'Russia', NULL);

COMMIT;


-- -----------------------------------------------------
-- Data for table `Airport`.`Airport`
-- -----------------------------------------------------
START TRANSACTION;
USE `Airport`;
INSERT INTO `Airport`.`Airport` (`idAirport`, `AirportName`, `email`, `telephone`, `details`, `idCity`) VALUES (1, 'Domodedovo', 'MDomodedovo@gmail.com', NULL, NULL, 1);
INSERT INTO `Airport`.`Airport` (`idAirport`, `AirportName`, `email`, `telephone`, `details`, `idCity`) VALUES (2, 'Vnukovo', 'AVnukovo@gmail.com', NULL, NULL, 1);
INSERT INTO `Airport`.`Airport` (`idAirport`, `AirportName`, `email`, `telephone`, `details`, `idCity`) VALUES (3, 'Sheremetevo', 'SheremetevoM@yandex.ru', NULL, NULL, 1);
INSERT INTO `Airport`.`Airport` (`idAirport`, `AirportName`, `email`, `telephone`, `details`, `idCity`) VALUES (4, 'KazanAir', NULL, NULL, NULL, 3);

COMMIT;


-- -----------------------------------------------------
-- Data for table `Airport`.`Rout`
-- -----------------------------------------------------
START TRANSACTION;
USE `Airport`;
INSERT INTO `Airport`.`Rout` (`idRout`, `city_from`, `city_to`, `cost`, `flightTime`) VALUES (1, 'Москва', 'Казань', 10000, '1:50');
INSERT INTO `Airport`.`Rout` (`idRout`, `city_from`, `city_to`, `cost`, `flightTime`) VALUES (2, 'Москва', 'Самара', 8000, '2:20');

COMMIT;


-- -----------------------------------------------------
-- Data for table `Airport`.`Plane`
-- -----------------------------------------------------
START TRANSACTION;
USE `Airport`;
INSERT INTO `Airport`.`Plane` (`idPlane`, `model`, `seats`, `madeYear`, `boardNumb`) VALUES (1, 'boing 1225', 200, 2010, 'RA-89043');
INSERT INTO `Airport`.`Plane` (`idPlane`, `model`, `seats`, `madeYear`, `boardNumb`) VALUES (2, 'Ан-2', 16, 1990, 'RF-99023');

COMMIT;


-- -----------------------------------------------------
-- Data for table `Airport`.`Schedule`
-- -----------------------------------------------------
START TRANSACTION;
USE `Airport`;
INSERT INTO `Airport`.`Schedule` (`idSchedule`, `flight`, `classType`, `Date`, `idPlane`, `idRout`) VALUES (1, '122PW', 'эконом', '2021.02.20', 1, 1);
INSERT INTO `Airport`.`Schedule` (`idSchedule`, `flight`, `classType`, `Date`, `idPlane`, `idRout`) VALUES (2, '218AC', 'частный', '2021.03.16', 2, 2);

COMMIT;


-- -----------------------------------------------------
-- Data for table `Airport`.`Passenger`
-- -----------------------------------------------------
START TRANSACTION;
USE `Airport`;
INSERT INTO `Airport`.`Passenger` (`PID`, `FName`, `LName`, `birthdate`, `sex`, `passport`, `telephone`, `address`) VALUES (1, 'Aleksandr', 'Baranov', '2001.08.18', 'М', '4510 423 900', '+79853877323', 'М.Динамо');
INSERT INTO `Airport`.`Passenger` (`PID`, `FName`, `LName`, `birthdate`, `sex`, `passport`, `telephone`, `address`) VALUES (2, 'Vadim', 'Korolev', '2001.02.27', 'М', '4512 422 800', '+79038924671', 'М.Динамо');
INSERT INTO `Airport`.`Passenger` (`PID`, `FName`, `LName`, `birthdate`, `sex`, `passport`, `telephone`, `address`) VALUES (3, 'Egor', 'Bykov', '2002.12.21', 'М', '4513 421 700', '+74959258732', 'М.Динамо');
INSERT INTO `Airport`.`Passenger` (`PID`, `FName`, `LName`, `birthdate`, `sex`, `passport`, `telephone`, `address`) VALUES (4, 'Maria', 'Baranova', '2003.10.28', 'Ж', '4512 420 600', '+78018325442', 'М.Аэропорт');

COMMIT;


-- -----------------------------------------------------
-- Data for table `Airport`.`Sale`
-- -----------------------------------------------------
START TRANSACTION;
USE `Airport`;
INSERT INTO `Airport`.`Sale` (`idSale`, `count`, `cost`, `idSchedule`) VALUES (1, 50, 1000, 1);
INSERT INTO `Airport`.`Sale` (`idSale`, `count`, `cost`, `idSchedule`) VALUES (2, 60, 2000, 1);
INSERT INTO `Airport`.`Sale` (`idSale`, `count`, `cost`, `idSchedule`) VALUES (3, 45, 3000, 1);

COMMIT;


-- -----------------------------------------------------
-- Data for table `Airport`.`User`
-- -----------------------------------------------------
START TRANSACTION;
USE `Airport`;
INSERT INTO `Airport`.`User` (`idUser`, `login`, `password`, `status`, `FName`, `LName`, `passport`) VALUES (1, 'shush1k', '1234', 'admin', 'Aleksandr', 'Baranov', '423 900');
INSERT INTO `Airport`.`User` (`idUser`, `login`, `password`, `status`, `FName`, `LName`, `passport`) VALUES (2, 'vadimkkk', '3333', 'eco', 'Vadim', 'Korolev', '422 800');
INSERT INTO `Airport`.`User` (`idUser`, `login`, `password`, `status`, `FName`, `LName`, `passport`) VALUES (3, 'egorbykov', '1999', 'business', 'Egor', 'Bykov', '421 700');
INSERT INTO `Airport`.`User` (`idUser`, `login`, `password`, `status`, `FName`, `LName`, `passport`) VALUES (4, 'mariaB', '5263', 'eco', 'Maria', 'Baranova', '420 600');

COMMIT;


-- -----------------------------------------------------
-- Data for table `Airport`.`Ticket`
-- -----------------------------------------------------
START TRANSACTION;
USE `Airport`;
INSERT INTO `Airport`.`Ticket` (`idTicket`, `ticketsCount`, `seatCount`, `PID`, `idSale`, `idUser`) VALUES (1, 50, 48, 1, 1, 1);
INSERT INTO `Airport`.`Ticket` (`idTicket`, `ticketsCount`, `seatCount`, `PID`, `idSale`, `idUser`) VALUES (2, 60, 58, 2, 2, 2);
INSERT INTO `Airport`.`Ticket` (`idTicket`, `ticketsCount`, `seatCount`, `PID`, `idSale`, `idUser`) VALUES (3, 45, 43, 3, 3, 3);

COMMIT;

