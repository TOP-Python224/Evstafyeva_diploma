-- MySQL Script generated by MySQL Workbench
-- Sun Apr  9 18:55:25 2023
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema nutrition_db
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema nutrition_db
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `nutrition_db` DEFAULT CHARACTER SET utf8 ;
USE `nutrition_db` ;

-- -----------------------------------------------------
-- Table `nutrition_db`.`User`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `nutrition_db`.`User` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `username` VARCHAR(100) NOT NULL,
  `password` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `username_UNIQUE` (`username` ASC) VISIBLE,
  UNIQUE INDEX `password_UNIQUE` (`password` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `nutrition_db`.`UserData`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `nutrition_db`.`UserData` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `full_name` VARCHAR(50) NOT NULL,
  `age` TINYINT(2) UNSIGNED NOT NULL,
  `height` TINYINT(3) UNSIGNED NOT NULL,
  `sex` ENUM('Мужской', 'Женский') NOT NULL,
  `purpose` ENUM('Похудение', 'Набор мышечной массы', 'Поддержание веса') NOT NULL,
  `activity_level` ENUM('Низкий', 'Умеренный', 'Высокий', 'Интенсивный') NOT NULL,
  `User_id` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_UserData_User1_idx` (`User_id` ASC) VISIBLE,
  CONSTRAINT `User_id`
    FOREIGN KEY (`User_id`)
    REFERENCES `nutrition_db`.`User` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `nutrition_db`.`WeightChange`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `nutrition_db`.`WeightChange` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `date` DATE NOT NULL,
  `weight` DECIMAL(4,1) NOT NULL,
  `bmi` DECIMAL(3,1) NOT NULL,
  `UserData_id` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_WeightChange_UserData1_idx` (`UserData_id` ASC) VISIBLE,
  CONSTRAINT `UserData_id`
    FOREIGN KEY (`UserData_id`)
    REFERENCES `nutrition_db`.`UserData` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `nutrition_db`.`Product`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `nutrition_db`.`Product` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `product_name` VARCHAR(50) NOT NULL,
  `calories` SMALLINT(5) UNSIGNED NOT NULL,
  `proteins` SMALLINT(3) UNSIGNED NOT NULL,
  `fats` SMALLINT(3) UNSIGNED NOT NULL,
  `carbohydrates` SMALLINT(3) UNSIGNED NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `product_name_UNIQUE` (`product_name` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `nutrition_db`.`Activity`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `nutrition_db`.`Activity` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `activity_name` VARCHAR(50) NOT NULL,
  `burned_calories` SMALLINT(4) UNSIGNED NOT NULL,
  `runtime` TINYINT(3) UNSIGNED NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `activity_name_UNIQUE` (`activity_name` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `nutrition_db`.`Reports`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `nutrition_db`.`Reports` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `date` DATE NOT NULL,
  `water` DECIMAL(2,1) NOT NULL,
  `UserData_id` INT UNSIGNED NOT NULL,
  `Product_id` INT UNSIGNED NOT NULL,
  `Activity_id` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `user_data_id_idx` (`UserData_id` ASC) VISIBLE,
  INDEX `fk_Reports_Product1_idx` (`Product_id` ASC) VISIBLE,
  INDEX `fk_Reports_Activity1_idx` (`Activity_id` ASC) VISIBLE,
  CONSTRAINT `UserData_id`
    FOREIGN KEY (`UserData_id`)
    REFERENCES `nutrition_db`.`UserData` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `Product_id`
    FOREIGN KEY (`Product_id`)
    REFERENCES `nutrition_db`.`Product` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `Activity_id`
    FOREIGN KEY (`Activity_id`)
    REFERENCES `nutrition_db`.`Activity` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `nutrition_db`.`userdata_product`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `nutrition_db`.`userdata_product` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `UserData_id` INT UNSIGNED NOT NULL,
  `Product_id` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `userdata_id_idx` (`UserData_id` ASC) VISIBLE,
  INDEX `product_id_idx` (`Product_id` ASC) VISIBLE,
  CONSTRAINT `UserData_id`
    FOREIGN KEY (`UserData_id`)
    REFERENCES `nutrition_db`.`UserData` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `Product_id`
    FOREIGN KEY (`Product_id`)
    REFERENCES `nutrition_db`.`Product` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `nutrition_db`.`userdata_activity`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `nutrition_db`.`userdata_activity` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `UserData_id` INT UNSIGNED NOT NULL,
  `Activity_id` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `userdata_id_idx` (`UserData_id` ASC) VISIBLE,
  INDEX `activity_id_idx` (`Activity_id` ASC) VISIBLE,
  CONSTRAINT `UserData_id`
    FOREIGN KEY (`UserData_id`)
    REFERENCES `nutrition_db`.`UserData` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `Activity_id`
    FOREIGN KEY (`Activity_id`)
    REFERENCES `nutrition_db`.`Activity` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;