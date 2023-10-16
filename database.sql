-- -----------------------------------------------------
-- Schema psychiatric_hospital
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `psychiatric_hospital`;
CREATE SCHEMA IF NOT EXISTS `psychiatric_hospital` DEFAULT CHARACTER SET utf8;

USE `psychiatric_hospital`;

-- -----------------------------------------------------
-- Table `psychiatric_hospital`.`person`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `psychiatric_hospital`.`person` (
    `id` MEDIUMINT UNSIGNED NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(200) NOT NULL,
    `birth_date` DATE NOT NULL,
    `sex` CHAR(1) NOT NULL,
    `cpf` CHAR(11) NOT NULL,
    `zip` CHAR(8) NULL,
    `street` VARCHAR(200) NULL,
    `street_number` INT NULL,
    `complement` VARCHAR(200) NULL,
    `neighborhood` VARCHAR(200) NULL,
    `city` VARCHAR(200) NULL,
    `state` CHAR(2) NULL,
    `country` CHAR(3) NULL,
    `phone` VARCHAR(14) NOT NULL,
    `email` VARCHAR(50) NOT NULL,
    PRIMARY KEY (`id`)
);



-- -----------------------------------------------------
-- Table `psychiatric_hospital`.`patient`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `psychiatric_hospital`.`patient` (
    `id` MEDIUMINT UNSIGNED NOT NULL,
    `weight` FLOAT NOT NULL,
    `marital_status` VARCHAR(200) NOT NULL,
    `profession` VARCHAR(200) NOT NULL,
    `emergency_contact_name` VARCHAR(200) NOT NULL,
    `emergency_contact_phone` VARCHAR(200) NOT NULL,
    `health_insurance` VARCHAR(50) NOT NULL,
    `hospitalization_date` DATETIME NOT NULL DEFAULT (NOW()),
    PRIMARY KEY (`id`),
    FOREIGN KEY (`id`) REFERENCES `psychiatric_hospital`.`person` (`id`)
);



-- -----------------------------------------------------
-- Table `psychiatric_hospital`.`professional`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `psychiatric_hospital`.`professional` (
    `id` MEDIUMINT UNSIGNED NOT NULL,
    `enrollment` CHAR(10) NOT NULL,
    `salary` FLOAT NOT NULL,
    `start_date` DATE NOT NULL,
    `working_range` VARCHAR(200) NOT NULL,
    `speciality` VARCHAR(200) NOT NULL,
    `consultation_fee` FLOAT NULL,
    PRIMARY KEY (`id`),
    UNIQUE (enrollment),
    FOREIGN KEY (`id`) REFERENCES `psychiatric_hospital`.`person` (`id`)
);



-- -----------------------------------------------------
-- Table `psychiatric_hospital`.`doctor`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `psychiatric_hospital`.`doctor` (
    `id` MEDIUMINT UNSIGNED NOT NULL,
    `crm` CHAR(10) NOT NULL,
    PRIMARY KEY (`id`),
    UNIQUE (`crm`),
    FOREIGN KEY (`id`) REFERENCES `psychiatric_hospital`.`professional` (`id`)
);


-- -----------------------------------------------------
-- Table `psychiatric_hospital`.`psychologist`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `psychiatric_hospital`.`psychologist` (
    `id` MEDIUMINT UNSIGNED NOT NULL,
    `crp` CHAR(10) NOT NULL,
    PRIMARY KEY (`id`),
    UNIQUE (`crp`),
    FOREIGN KEY (`id`) REFERENCES `psychiatric_hospital`.`professional` (`id`)
);


-- -----------------------------------------------------
-- Table `psychiatric_hospital`.`consultation`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `psychiatric_hospital`.`consultation` (
    `id` MEDIUMINT UNSIGNED NOT NULL AUTO_INCREMENT,
    `time` DATETIME NOT NULL DEFAULT (NOW()),
    `patient_id` MEDIUMINT UNSIGNED NOT NULL,
    `doctor_id` MEDIUMINT UNSIGNED NOT NULL,
    PRIMARY KEY (`id`),
    FOREIGN KEY (`patient_id`) REFERENCES `psychiatric_hospital`.`patient` (`id`),
    FOREIGN KEY (`doctor_id`) REFERENCES `psychiatric_hospital`.`doctor` (`id`)
);


-- -----------------------------------------------------
-- Table `psychiatric_hospital`.`disorder`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `psychiatric_hospital`.`disorder` (
    `id` MEDIUMINT UNSIGNED NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(200) NOT NULL,
    `category` VARCHAR(200) NOT NULL,
    `symptoms` VARCHAR(200) NOT NULL,
    `risk_factor` VARCHAR(200) NOT NULL,
    `prevalence` VARCHAR(200) NOT NULL,
    PRIMARY KEY (`id`),
    UNIQUE (`name`)
);


-- -----------------------------------------------------
-- Table `psychiatric_hospital`.`dosage`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `psychiatric_hospital`.`dosage` (
    `id` MEDIUMINT UNSIGNED NOT NULL AUTO_INCREMENT,
    `dose_quantity` VARCHAR(50) NOT NULL,
    `dose_frequency` VARCHAR(50) NOT NULL,
    PRIMARY KEY (`id`)
);


-- -----------------------------------------------------
-- Table `psychiatric_hospital`.`medicine`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `psychiatric_hospital`.`medicine` (
    `id` MEDIUMINT UNSIGNED NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(200) NOT NULL,
    `composition` VARCHAR(200) NOT NULL,
    `usage_type` VARCHAR(50) NOT NULL,
    `indication` VARCHAR(200) NOT NULL,
    `contraindication` VARCHAR(200) NOT NULL,
    PRIMARY KEY (`id`),
    UNIQUE (`name`),
    UNIQUE (`composition`)
);


-- -----------------------------------------------------
-- Table `psychiatric_hospital`.`treatment`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `psychiatric_hospital`.`treatment` (
    `id` MEDIUMINT UNSIGNED NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(200) NOT NULL,
    `start_date` DATETIME NOT NULL DEFAULT NOW(),
    `planned_end_date` DATETIME NOT NULL DEFAULT (NOW()),
    `patient_id` MEDIUMINT UNSIGNED NOT NULL,
    PRIMARY KEY (`id`),
    FOREIGN KEY (`patient_id`) REFERENCES `psychiatric_hospital`.`patient` (`id`)
);


-- -----------------------------------------------------
-- Table `psychiatric_hospital`.`medical_record`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `psychiatric_hospital`.`medical_record` (
    `id` MEDIUMINT UNSIGNED NOT NULL AUTO_INCREMENT,
    `record_date` DATE NOT NULL DEFAULT (NOW()),
    `description` VARCHAR(200) NULL,
    `patient_id` MEDIUMINT UNSIGNED NOT NULL,
    `treatment_id` MEDIUMINT UNSIGNED NOT NULL,
    PRIMARY KEY (`id`),
    FOREIGN KEY (`patient_id`) REFERENCES `psychiatric_hospital`.`patient` (`id`),
    FOREIGN KEY (`treatment_id`) REFERENCES `psychiatric_hospital`.`treatment` (`id`)
);


-- -----------------------------------------------------
-- Table `psychiatric_hospital`.`therapy`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `psychiatric_hospital`.`therapy` (
    `id` MEDIUMINT UNSIGNED NOT NULL AUTO_INCREMENT,
    `time` DATETIME NOT NULL DEFAULT (NOW()),
    `purpose` VARCHAR(200) NOT NULL,
    `capacity` INT NOT NULL,
    `psychologist_id` MEDIUMINT UNSIGNED NOT NULL,
    PRIMARY KEY (`id`),
    UNIQUE(`purpose`),
    FOREIGN KEY (`psychologist_id`) REFERENCES `psychiatric_hospital`.`psychologist` (`id`)
);



-- -----------------------------------------------------
-- Table `psychiatric_hospital`.`treatment_treats_disorder`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `psychiatric_hospital`.`treatment_treats_disorder` (
    `id` MEDIUMINT UNSIGNED NOT NULL AUTO_INCREMENT,
    `treatment_id` MEDIUMINT UNSIGNED NOT NULL,
    `disorder_id` MEDIUMINT UNSIGNED NOT NULL,
    PRIMARY KEY (`id`),
    FOREIGN KEY (`treatment_id`) REFERENCES `psychiatric_hospital`.`treatment` (`id`),
    FOREIGN KEY (`disorder_id`) REFERENCES `psychiatric_hospital`.`disorder` (`id`)
);


-- -----------------------------------------------------
-- Table `psychiatric_hospital`.`doctor_suggest_treatment`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `psychiatric_hospital`.`doctor_suggest_treatment` (
    `id` MEDIUMINT UNSIGNED NOT NULL AUTO_INCREMENT,
    `doctor_id` MEDIUMINT UNSIGNED NOT NULL,
    `treatment_id` MEDIUMINT UNSIGNED NOT NULL,
    PRIMARY KEY (`id`),
    FOREIGN KEY (`doctor_id`) REFERENCES `psychiatric_hospital`.`doctor` (`id`),
    FOREIGN KEY (`treatment_id`) REFERENCES `psychiatric_hospital`.`treatment` (`id`)
);


-- -----------------------------------------------------
-- Table `psychiatric_hospital`.`psychologist_helps_treatment`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `psychiatric_hospital`.`psychologist_helps_treatment` (
    `id` MEDIUMINT UNSIGNED NOT NULL AUTO_INCREMENT,
    `psychologist_id` MEDIUMINT UNSIGNED NOT NULL,
    `treatment_id` MEDIUMINT UNSIGNED NOT NULL,
    PRIMARY KEY (`id`),
    FOREIGN KEY (`psychologist_id`) REFERENCES `psychiatric_hospital`.`psychologist` (`id`),
    FOREIGN KEY (`treatment_id`) REFERENCES `psychiatric_hospital`.`treatment` (`id`)
);



-- -----------------------------------------------------
-- Table `psychiatric_hospital`.`medicines_suggestion`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `psychiatric_hospital`.`medicine_suggestion` (
    `medicine_id` MEDIUMINT UNSIGNED NOT NULL,
    `dosage_id` MEDIUMINT UNSIGNED NOT NULL,
    `medical_record_id` MEDIUMINT UNSIGNED NOT NULL,
    `id` MEDIUMINT UNSIGNED NOT NULL AUTO_INCREMENT,
    PRIMARY KEY (`id`),
    FOREIGN KEY (`medicine_id`) REFERENCES `psychiatric_hospital`.`medicine` (`id`),
    FOREIGN KEY (`dosage_id`) REFERENCES `psychiatric_hospital`.`dosage` (`id`),
    FOREIGN KEY (`medical_record_id`) REFERENCES `psychiatric_hospital`.`medical_record` (`id`)
);


-- -----------------------------------------------------
-- Table `psychiatric_hospital`.`medical_record_included_therapy`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `psychiatric_hospital`.`medical_record_included_therapy` (
	`id` MEDIUMINT UNSIGNED NOT NULL AUTO_INCREMENT,
    `medical_record_id` MEDIUMINT UNSIGNED NOT NULL,
    `therapy_id` MEDIUMINT UNSIGNED NOT NULL,
    PRIMARY KEY (`id`),
    FOREIGN KEY (`medical_record_id`) REFERENCES `psychiatric_hospital`.`medical_record` (`id`),
    FOREIGN KEY (`therapy_id`) REFERENCES `psychiatric_hospital`.`therapy` (`id`)
);


-- -----------------------------------------------------
-- Table `psychiatric_hospital`.`doctor_update_record`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `psychiatric_hospital`.`doctor_update_record` (
    `id` MEDIUMINT UNSIGNED NOT NULL AUTO_INCREMENT,
    `doctor_id` MEDIUMINT UNSIGNED NOT NULL,
    `medical_record_id` MEDIUMINT UNSIGNED NOT NULL,
    PRIMARY KEY (`id`),
    FOREIGN KEY (`doctor_id`) REFERENCES `psychiatric_hospital`.`doctor` (`id`),
    FOREIGN KEY (`medical_record_id`) REFERENCES `psychiatric_hospital`.`medical_record` (`id`)
);


-- -----------------------------------------------------
-- Table `psychiatric_hospital`.`psychologist_update_record`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `psychiatric_hospital`.`psychologist_update_record` (
    `id` MEDIUMINT UNSIGNED NOT NULL AUTO_INCREMENT,
    `psychologist_id` MEDIUMINT UNSIGNED NOT NULL,
    `medical_record_id` MEDIUMINT UNSIGNED NOT NULL,
    PRIMARY KEY (`id`),
    FOREIGN KEY (`psychologist_id`) REFERENCES `psychiatric_hospital`.`psychologist` (`id`),
    FOREIGN KEY (`medical_record_id`) REFERENCES `psychiatric_hospital`.`medical_record` (`id`)
);

