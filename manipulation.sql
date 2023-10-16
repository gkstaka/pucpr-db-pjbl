USE psychiatric_hospital;

INSERT INTO `person` (`name`,`birth_date`,`sex`,`cpf`,`zip`,`street`,`street_number`,`complement`,`neighborhood`,`city`,`state`,`country`,`phone`,`email`) 
VALUES 
('Bruno Miglioretto','2013-02-01','m','06411448908','70040912','Rua dos santos',12,'APT 239','Boa vista','Curitiba','PR','BRL','+5541996438691','bruno@exemple.com'),
('João da Silva','1985-07-15','m','31076567045','74120080','Rua 18',12,NULL,'Boa vista','Curitiba','PR','BRL','+5541396438691','joao@exemple.com'),
('John Smith','1970-04-23','m','98765432109','543210','Maple Avenue',30,'Suite 101','Downtown','Metropolis','CA','USA','+5122334455','john@example.com'),
('Maria Garcia','1970-04-23','f','34567891234','654321','Oak Street',55,'','West End','Riverside','CA','USA','+1987654321','maria@example.com'),
('Luis Rodriguez','1992-11-10','m','78901234567','987654','Pine Street',88,'APT 305','East Side','Springfield','IL','USA','+1654321879','luis@example.com'),
('Sophia Johnson','1982-05-30','f','56789012345','234567','Cedar Lane',18,'','North End','Hill Valley','CA','USA','+1555123456','sophia@example.com'),
('Eva Johnson','1982-05-30','f','98765432100','543210','Willow Street',22,'Suite 301','Downtown','Metropolis','CA','USA','+1112334455','eva@example.com'),
('Daniel Brown','1995-09-02','m','11122334455','332211','Chestnut Avenue',45,'','West End','Riverside','CA','USA','+1987614321','daniel@example.com'),
('Sophie Miller','1970-04-23','f','22233445566','998877','Magnolia Street',78,'APT 205','East Side','Springfield','IL','USA','+1614321879','sophie@example.com'),
('William Clark','1970-04-23','m','33344556677','112233','Maple Lane',13,'','North End','Hill Valley','CA','USA','+1555113456','william@example.com'),
('Ava Baker','2013-02-01','f','44455667788','334455','Pine Drive',36,'','South Side','Springfield','IL','USA','+1444333222','ava@example.com'),
('Liam Wilson','1970-04-23','m','55566677788','123456','Sunset Boulevard',99,'Suite 501','Hollywood Hills','Los Angeles','CA','USA','+1122334455','liam@example.com'),
('Emma Davis','1970-04-23','f','66677788899','654321','Ocean Avenue',11,'','Beachfront','Santa Monica','CA','USA','+6987654321','emma@example.com'),
('Noah Martinez','1992-11-10','f','77788899900','112233','Palm Street',22,'APT 102','Palm Beach','Miami','FL','USA','+1654321829','noah@example.com'),
('Olivia Taylor','1982-05-30','f','88899900011','334455','Grove Avenue',55,'','Green Park','Orlando','FL','USA','+1555123156','olivia@example.com'),
('James Johnson','1992-11-10','m','99900011222','998877','Hillside Drive',77,'Suite 303','Hilltop','Tampa','FL','USA','+1444333252','james@example.com'),
('Isabella Brown','1985-07-15','f','00011122233','223344','Forest Road',33,'','Woodland','Jacksonville','FL','USA','+1888777666','isabella@example.com'),
('Sophia Hernandez','1992-11-10','f','11223341156','223344','Oak Street',99,'APT 401','Downtown','Metropolis','CA','USA','+1111134455','sophiaa@example.com');

INSERT INTO `professional` (`id`,`enrollment`,`salary`,`start_date`,`working_range`,`speciality`,`consultation_fee`) 
VALUES 
(1,'AKDFJKKKD',10000,'2023-10-16','Junior','Cardio',80),
(2,'JKLFJSDFE',12000,'2023-10-16','Senior','Neurology',100),
(3,'IODFJNSDF',9500,'2023-10-16','Mid-Level','Dermatology',90),
(4,'ALSKDFJSD',11000,'2023-10-16','Junior','Oncology',85),
(5,'POIUERLKJ',11500,'2023-10-16','Senior','Orthopedics',110),
(6,'QWERTYUIO',10500,'2023-10-16','Mid-Level','Gynecology',95),
(7,'KDFJNSDF1',9500,'2023-10-16','Junior','Pediatrics',85),
(8,'DFJNSKDF2',11000,'2023-10-16','Senior','Ophthalmology',90),
(9,'KJDFNSDF3',10500,'2023-10-16','Mid-Level','Dentistry',80),
(10,'KJDFNSDF4',10000,'2023-10-16','Junior','Psychiatry',95),
(11,'SKDFNSDF5',11500,'2023-10-16','Senior','Gastroenterology',100),
(12,'KJDFNSDF6',9800,'2023-10-16','Mid-Level','Dermatology',88);

INSERT INTO `doctor` (`id`,`crm`) 
VALUES 
(1,'39489'),
(2,'340809'),
(3,'20398'),
(4,'32322311'),
(5,'3948939'),
(6,'39489999');

INSERT INTO `psychologist` (`id`,`crp`) 
VALUES 
(7,'0as9d8f9'),
(8,'asdf90909'),
(9,'98sd7f897'),
(10,'asdf976'),
(11,'23498dgfs'),
(12,'0as1d8f9');

INSERT INTO `patient` (`id`,`weight`,`marital_status`,`profession`,`emergency_contact_name`,`emergency_contact_phone`,`health_insurance`,`hospitalization_date`) 
VALUES 
(13,56,'single','Programmer','Alice','390809384','Unimed','2023-10-03 00:00:00'),
(14,70,'married','Teacher','John','123456789','BlueCross','2023-09-20 00:00:00'),
(15,85,'divorced','Doctor','Sarah','987654321','Aetna','2023-11-05 00:00:00'),
(16,62,'single','Engineer','Michael','555123456','Cigna','2023-10-15 00:00:00'),
(17,75,'married','Nurse','Emily','678987654','Humana','2023-09-10 00:00:00'),
(18,68,'single','Artist','Oliver','9122334455','Kaiser','2023-10-25 00:00:00');

INSERT INTO `consultation` (`id`,`time`,`patient_id`) 
VALUES 
(1,'2022-07-15 00:00:00',13),
(2,'2023-05-15 00:00:00',14),
(3,'2023-09-15 00:00:00',15),
(4,'2021-05-01 00:00:00',16),
(5,'2022-03-10 00:00:00',17),
(6,'2020-01-01 00:00:00',18);

INSERT INTO `medicine` (`id`,`name`,`composition`,`usage_type`,`indication`,`contraindication`) 
VALUES 
(1,'Paracetamol','Magnesium stearate, cellulose, docusate sodium and sodium benzoate or sodium lauryl sulfate, starch, hydroxypropyl methylcellulose, propylene glycol','Oral use','Adults','Kids'),
(2,'Ibuprofen','Croscarmellose sodium, colloidal silicon dioxide, hypromellose, iron oxide, polyethylene glycol','Oral use','Pain relief, fever reduction, anti-inflammatory','Patients with a history of allergic reactions to aspirin or NSAIDs'),
(3,'Amoxicillin','Colloidal silicon dioxide, polyethylene glycol, starch, sodium lauryl sulfate, titanium dioxide','Oral use','Bacterial infections','Patients with a history of allergic reactions to penicillin'),
(4,'Omeprazole','Crospovidone, hypromellose, magnesium stearate, mannitol, sodium lauryl sulfate','Oral use','Gastric acid reduction','Patients with hypersensitivity to proton pump inhibitors'),
(5,'Loratadine','Calcium phosphate, lactose, magnesium stearate, corn starch','Oral use','Allergy relief','Patients with severe kidney disorders'),
(6,'Aspirin','Corn starch, hypromellose, powdered cellulose, triacetin','Oral use','Pain relief, fever reduction, anti-inflammatory','Patients with a history of bleeding disorders');	

