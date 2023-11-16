USE psychiatric_hospital;

INSERT INTO `person` (`id`,`name`,`birth_date`,`sex`,`cpf`,`zip`,`street`,`street_number`,`complement`,`neighborhood`,`city`,`state`,`country`,`phone`,`email`) 
VALUES 
(1,'Bruno Miglioretto','2013-02-01','m','06411448908','70040912','Rua dos santos',12,'APT 239','Boa vista','Curitiba','PR','BRL','+5541996438691','bruno@exemple.com'),
(2,'João da Silva','1985-07-15','m','31076567045','74120080','Rua 18',12,NULL,'Boa vista','Curitiba','PR','BRL','+5541396438691','joao@exemple.com'),
(3,'John Smith','1970-04-23','m','98765432109','543210','Maple Avenue',30,'Suite 101','Downtown','Metropolis','CA','USA','+5122334455','john@example.com'),
(4,'Maria Garcia','1970-04-23','f','34567891234','654321','Oak Street',55,'','West End','Riverside','CA','USA','+1987654321','maria@example.com'),
(5,'Luis Rodriguez','1992-11-10','m','78901234567','987654','Pine Street',88,'APT 305','East Side','Springfield','IL','USA','+1654321879','luis@example.com'),
(6,'Sophia Johnson','1982-05-30','f','56789012345','234567','Cedar Lane',18,'','North End','Hill Valley','CA','USA','+1555123456','sophia@example.com'),
(7,'Eva Johnson','1982-05-30','f','98765432100','543210','Willow Street',22,'Suite 301','Downtown','Metropolis','CA','USA','+1112334455','eva@example.com'),
(8,'Daniel Brown','1995-09-02','m','11122334455','332211','Chestnut Avenue',45,'','West End','Riverside','CA','USA','+1987614321','daniel@example.com'),
(9,'Sophie Miller','1970-04-23','f','22233445566','998877','Magnolia Street',78,'APT 205','East Side','Springfield','IL','USA','+1614321879','sophie@example.com'),
(10,'William Clark','1970-04-23','m','33344556677','112233','Maple Lane',13,'','North End','Hill Valley','CA','USA','+1555113456','william@example.com'),
(11,'Ava Baker','2013-02-01','f','44455667788','334455','Pine Drive',36,'','South Side','Springfield','IL','USA','+1444333222','ava@example.com'),
(12,'Liam Wilson','1970-04-23','m','55566677788','123456','Sunset Boulevard',99,'Suite 501','Hollywood Hills','Los Angeles','CA','USA','+1122334455','liam@example.com'),
(13,'Emma Davis','1970-04-23','f','66677788899','654321','Ocean Avenue',11,'','Beachfront','Santa Monica','CA','USA','+6987654321','emma@example.com'),
(14,'Noah Martinez','1992-11-10','f','77788899900','112233','Palm Street',22,'APT 102','Palm Beach','Miami','FL','USA','+1654321829','noah@example.com'),
(15,'Olivia Taylor','1982-05-30','f','88899900011','334455','Grove Avenue',55,'','Green Park','Orlando','FL','USA','+1555123156','olivia@example.com'),
(16,'James Johnson','1992-11-10','m','99900011222','998877','Hillside Drive',77,'Suite 303','Hilltop','Tampa','FL','USA','+1444333252','james@example.com'),
(17,'Isabella Brown','1985-07-15','f','00011122233','223344','Forest Road',33,'','Woodland','Jacksonville','FL','USA','+1888777666','isabella@example.com'),
(18,'Sophia Hernandez','1992-11-10','f','11223341156','223344','Oak Street',99,'APT 401','Downtown','Metropolis','CA','USA','+1111134455','sophiaa@example.com');


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

INSERT INTO `consultation` (`id`,`time`,`patient_id`, `doctor_id`) 
VALUES 
(1,'2022-07-15 00:00:00',13,3),
(2,'2023-05-15 00:00:00',14,4),
(3,'2023-09-15 00:00:00',15,2),
(4,'2021-05-01 00:00:00',16,1),
(5,'2022-03-10 00:00:00',17,5),
(6,'2020-01-01 00:00:00',18,6);

INSERT INTO `disorder` (`id`,`name`,`category`,`symptoms`,`risk_factors`,`prevalence`) 
VALUES 
(1,'Anxiety','Anxiety disorders','Excessive worry, restlessness, fatigue, difficulty concentrating, irritability, sleep problems','Trauma, stress due to an illness, stress buildup, personality',0.89),
(2,'Depression','Mood disorders','Sadness, loss of interest, feelings of guilt or low self-worth, disturbed sleep or appetite, tiredness, poor concentration','Childhood trauma, other mental disorders, abuse of alcohol or recreational drugs, personal problems, poverty or isolation',0.76),
(3,'Bipolar disorder','Mood disorders','Mood changes, elevated mood, high energy, sleep problems, loss of appetite, psychosis','Genetic, environmental, brain structure and function',0.35),
(4,'Schizophrenia','Psychotic disorders','Delusions, hallucinations, disorganized thinking, lack of motivation, speaking little','Genetic, environmental, brain chemistry, substance abuse',0.01),
(5,'Autism','Neurodevelopmental disorders','Difficulty with communication and interaction with other people, restricted interests and repetitive behaviors','Genetic, environmental',0.12),
(6,'ADHD','Neurodevelopmental disorders','Difficulty paying attention, hyperactivity, impulsivity','Genetic, environmental',0.06);

INSERT INTO `dosage` (`id`,`dose_quantity`,`dose_frequency`) 
VALUES 
(1,'30','400'),
(2,'10','40'),
(3,'300','90'),
(4,'20','300'),
(5,'220','10'),
(6,'30','300');

INSERT INTO `medicine` (`id`,`name`,`composition`,`usage_type`,`indication`,`contraindication`) 
VALUES 
(1,'Paracetamol','Magnesium stearate, cellulose, docusate sodium and sodium benzoate or sodium lauryl sulfate, starch, hydroxypropyl methylcellulose, propylene glycol','Oral use','Adults','Kids'),
(2,'Ibuprofen','Croscarmellose sodium, colloidal silicon dioxide, hypromellose, iron oxide, polyethylene glycol','Oral use','Pain relief, fever reduction, anti-inflammatory','Patients with a history of allergic reactions to aspirin or NSAIDs'),
(3,'Amoxicillin','Colloidal silicon dioxide, polyethylene glycol, starch, sodium lauryl sulfate, titanium dioxide','Oral use','Bacterial infections','Patients with a history of allergic reactions to penicillin'),
(4,'Omeprazole','Crospovidone, hypromellose, magnesium stearate, mannitol, sodium lauryl sulfate','Oral use','Gastric acid reduction','Patients with hypersensitivity to proton pump inhibitors'),
(5,'Loratadine','Calcium phosphate, lactose, magnesium stearate, corn starch','Oral use','Allergy relief','Patients with severe kidney disorders'),
(6,'Aspirin','Corn starch, hypromellose, powdered cellulose, triacetin','Oral use','Pain relief, fever reduction, anti-inflammatory','Patients with a history of bleeding disorders');	

INSERT INTO `treatment` (`id`,`name`,`start_date`,`planned_end_date`,`patient_id`) 
VALUES 
(1,'Anxiety treatment','2021-07-15 00:00:00','2023-07-15 00:00:00',13),
(2,'Depression treatment','2023-05-15 00:00:00','2024-05-15 00:00:00',14),
(3,'Bipolar disorder treatment','2023-09-15 00:00:00','2024-09-15 00:00:00',15),
(4,'Schizophrenia treatment','2021-05-01 00:00:00','2022-05-01 00:00:00',16),
(5,'Autism treatment','2022-03-10 00:00:00','2023-03-10 00:00:00',17),
(6,'ADHD treatment','2020-01-01 00:00:00','2021-01-01 00:00:00',18);

INSERT INTO `medical_record` (`id`,`record_date`,`description`,`patient_id`,`treatment_id`) 
VALUES 
(1,'2022-07-15 00:00:00','Patient is suffering from anxiety disorder', 13, 1),
(2,'2023-05-15 00:00:00','Patient is suffering from depression', 14, 2),
(3,'2023-09-15 00:00:00','Patient is suffering from bipolar disorder', 15, 3),
(4,'2021-05-01 00:00:00','Patient is suffering from schizophrenia',16, 4),
(5,'2022-03-10 00:00:00','Patient is suffering from autism', 17, 5),
(6,'2020-01-01 00:00:00','Patient is suffering from ADHD',18, 6);

INSERT INTO `therapy` (`id`,`time`,`purpose`,`capacity`,`psychologist_id`) 
VALUES 
(1,'1900-01-01 01:00:00','Cognitive behavioral therapy (CBT) is a form of psychological treatment.',1,12),
(2,'1900-01-01 02:00:00','Dialectical behavior therapy (DBT) is a specific type of cognitive-behavioral psychotherapy.',1,7),
(3,'1900-01-01 03:00:00','Interpersonal therapy (IPT) is a time-limited treatment.',1,11),
(4,'1900-01-01 04:00:00','Psychodynamic therapy is a form of therapy with a focus on a holistic perspective of the client.',1,9),
(5,'1900-01-01 05:00:00','Family therapy is a type of psychological counseling (psychotherapy) that helps family members.',1,8),
(6,'1900-01-01 06:00:00','Couple therapy is a type of psychological therapy that helps couples of all types.',2,10);

INSERT INTO `suggestion` (`id`,`medicine_id`,`dosage_id`,`medical_record_id`) 
VALUES (1,1,1,1),
(2,2,2,2),
(3,3,3,3),
(4,4,4,4),
(5,5,5,5),
(6,6,6,6);

INSERT INTO `doctor_suggest_treatment` (`id`,`doctor_id`,`treatment_id`) 
VALUES 
(1,3,1),
(2,4,2),
(3,2,3),
(4,1,4),
(5,5,5),
(6,6,6);

INSERT INTO `doctor_update_record` (`id`,`doctor_id`,`medical_record_id`) 
VALUES 
(1,3,1),
(2,4,2),
(3,2,3),
(4,1,4),
(5,5,5),
(6,6,6);

INSERT INTO `medical_record_included_therapy` (`id`,`medical_record_id`,`therapy_id`) 
VALUES 
(1,1,1),
(2,2,2),
(3,3,3),
(4,4,4),
(5,5,5),
(6,6,6);

INSERT INTO `psychologist_helps_treatment` (`id`,`psychologist_id`,`treatment_id`) 
VALUES 
(1,12,1),
(2,7,2),
(3,11,3),
(4,9,4),
(5,8,5),
(6,10,6);

INSERT INTO `psychologist_update_record` (`id`,`psychologist_id`,`medical_record_id`) 
VALUES 
(1,12,1),
(2,7,2),
(3,11,3),
(4,9,4),
(5,8,5),
(6,10,6);

INSERT INTO `treatment_treats_disorder` (`id`,`treatment_id`, `disorder_id`) 
VALUES 
(1,1,1),
(2,2,2),
(3,3,3),
(4,4,4),
(5,5,5),
(6,6,6);

-- MORE INSERTS 
INSERT INTO `person` (`id`,`name`,`birth_date`,`sex`,`cpf`,`zip`,`street`,`street_number`,`complement`,`neighborhood`,`city`,`state`,`country`,`phone`,`email`) 
VALUES 
(19,'Lucas White','1987-05-12','m','11022334456','756734','Rose Street',15,'','South End','San Diego','CA','USA','+1255123456','lucas@example.com'),
(20,'Mia Thompson','1995-12-22','f','21123445567','987623','Tulip Lane',26,'APT 201','Central','San Francisco','CA','USA','+1425234567','mia@example.com'),
(21,'Ella Harris','1980-09-08','f','31234556678','623187','Blossom Drive',35,'','East District','Seattle','WA','USA','+1155123756','ella@example.com'),
(22,'Benjamin Clark','1975-01-14','m','41345667789','654128','Daisy Avenue',44,'APT 101','West Zone','Dallas','TX','USA','+1234123456','benjamin@example.com'),
(23,'Charlotte Evans','1992-04-16','f','51456778890','897612','Lily Road',53,'','North Side','Austin','TX','USA','+1345123856','charlotte@example.com'),
(24,'Jacob Wright','1989-10-25','m','61567889901','654298','Sunflower Street',62,'','Downtown','Boston','MA','USA','+1255123956','jacob@example.com'),
(25,'Amelia Green','1978-06-21','f','71678900012','129876','Jasmine Way',71,'Suite 101','Old Town','New York','NY','USA','+1456123456','amelia@example.com'),
(26,'Michael King','1990-08-03','m','81789001123','654120','Violet Lane',80,'','South Park','Philadelphia','PA','USA','+1555123056','michael@example.com'),
(27,'Emily Hill','1982-12-15','f','91890112234','321654','Rosemary Drive',89,'APT 202','Midtown','Chicago','IL','USA','+1655123156','emily@example.com'),
(28,'Daniel Lee','1977-03-19','m','10190123345','654312','Orchid Street',98,'','Uptown','Houston','TX','USA','+1755123256','daniel@example.com'),
(29,'Lily Turner','1998-02-28','f','11090234456','789065','Gardenia Way',107,'','City Center','Phoenix','AZ','USA','+1855123356','lily@example.com'),
(30,'Ethan Foster','1985-05-17','m','12190245567','876542','Lavender Avenue',116,'APT 303','Suburb','Los Angeles','CA','USA','+1955123456','ethan@example.com'),
(31,'Sophie Reed','1979-11-11','f','13290256678','654213','Daffodil Drive',125,'','Countryside','Denver','CO','USA','+2055123556','sophie@example.com'),
(32,'Jack Robinson','1993-09-23','m','14390267789','987651','Cherry Blossom Way',134,'','Metropolitan','Nashville','TN','USA','+2155123656','jack@example.com'),
(33,'Isla Baker','1987-04-29','f','15490278890','345678','Lilac Road',143,'Suite 102','Urban','Indianapolis','IN','USA','+2255123756','isla@example.com'),
(34,'Oscar Cooper','1996-08-08','m','16590289901','234567','Pansy Street',152,'','Coastal','Miami','FL','USA','+2355123856','oscar@example.com'),
(35,'Isabelle Ward','1983-01-03','f','17690300012','123456','Petunia Lane',161,'','Rural','Columbus','OH','USA','+2455123956','isabelle@example.com'),
(36,'Charlie Lewis','1994-10-13','m','18790311123','567890','Dahlia Drive',170,'APT 204','Historic','Charlotte','NC','USA','+2555124056','charlie@example.com'),
(37,'Ava Gray','1988-07-24','f','19890322234','765432','Marigold Street',179,'','Downtown','Jacksonville','FL','USA','+2655124156','ava@example.com'),
(38,'George Wood','1986-12-06','m','20990333345','123789','Magnolia Avenue',188,'','Suburban','Detroit','MI','USA','+2755124256','george@example.com');

INSERT INTO `professional` (`id`,`enrollment`,`salary`,`start_date`,`working_range`,`speciality`,`consultation_fee`) 
VALUES 
(19,'LUCW78901',11500,'2023-10-20','Senior','Pulmonology',110),
(20,'MIAT23456',11800,'2023-10-21','Mid-Level','Urology',95),
(21,'ELLAH7890',9700,'2023-10-22','Junior','Hematology',80),
(22,'BENJ9801',12000,'2023-10-23','Senior','Radiology',105),
(23,'CHAR5678',9900,'2023-10-24','Mid-Level','Endocrinology',90),
(24,'JACW4567',11600,'2023-10-25','Senior','Allergology',115),
(25,'AMG6789',9800,'2023-10-26','Junior','Rheumatology',85),
(26,'MIK2345',11300,'2023-10-27','Mid-Level','Nephrology',100),
(27,'EMH1234',11400,'2023-10-28','Senior','Otorhinolaryngology',110),
(28,'DANL5678',9600,'2023-10-29','Junior','Geriatrics',80);

INSERT INTO `doctor` (`id`,`crm`) 
VALUES 
(19,'4567890'),
(20,'5678901'),
(21,'6789012'),
(22,'7890123'),
(23,'8901234');

INSERT INTO `psychologist` (`id`,`crp`) 
VALUES 
(24,'asdf0123'),
(25,'qwer1234'),
(26,'zxcv2345'),
(27,'erty3456'),
(28,'fghj4567');

INSERT INTO `patient` (`id`,`weight`,`marital_status`,`profession`,`emergency_contact_name`,`emergency_contact_phone`,`health_insurance`,`hospitalization_date`) 
VALUES 
(29,65,'Single','Engineer','Liam Turner','+1855123357','Blue Shield','2023-01-10'),
(30,72,'Married','Musician','Eva Foster','+1955123457','Aetna','2023-02-11'),
(31,59,'Divorced','Teacher','Evan Reed','+2055123557','Kaiser Permanente','2023-03-12'),
(32,78,'Single','Architect','Grace Robinson','+2155123657','Cigna','2023-04-13'),
(33,66,'Widowed','Nurse','Noah Baker','+2255123757','UnitedHealth','2023-05-14'),
(34,70,'Married','Programmer','Zoe Cooper','+2355123857','Humana','2023-06-15'),
(35,60,'Single','Dentist','Oliver Ward','+2455123957','Anthem','2023-07-16'),
(36,75,'Married','Physicist','Emma Lewis','+2555124057','Molina Healthcare','2023-08-17'),
(37,64,'Divorced','Artist','William Gray','+2655124157','Health Net','2023-09-18'),
(38,73,'Single','Scientist','Mia Wood','+2755124257','Centene Corporation','2023-10-19');


INSERT INTO `consultation` (`id`,`time`,`patient_id`, `doctor_id`) 
VALUES 
(7,'2023-11-01 00:00:00',29,1),
(8,'2023-11-02 00:00:00',30,2),
(9,'2023-11-03 00:00:00',31,3),
(10,'2023-11-04 00:00:00',32,4),
(11,'2023-11-05 00:00:00',33,5),
(12,'2023-11-06 00:00:00',34,6),
(13,'2023-11-07 00:00:00',35,19),
(14,'2023-11-08 00:00:00',36,20),
(15,'2023-11-09 00:00:00',37,21),
(16,'2023-11-10 00:00:00',38,22),
(17,'2023-11-11 00:00:00',13,23),
(18,'2023-11-12 00:00:00',14,6),
(19,'2023-11-13 00:00:00',15,1),
(20,'2023-11-14 00:00:00',16,2),
(21,'2023-11-15 00:00:00',17,3),
(22,'2023-11-16 00:00:00',18,4),
(23,'2023-11-17 00:00:00',29,5),
(24,'2023-11-18 00:00:00',30,6),
(25,'2023-11-19 00:00:00',31,1),
(26,'2023-11-20 00:00:00',32,2);

INSERT INTO `suggestion` (`id`, `medicine_id`, `dosage_id`, `medical_record_id`)
VALUES
    (7, 1, 4, 6),
    (8, 2, 2, 2),
    (9, 3, 6, 5),
    (10, 3, 5, 1),
    (11, 4, 5, 3),
    (12, 5, 4, 2),
    (13, 6, 2, 6),
    (14, 4, 3, 5),
    (15, 6, 1, 3),
    (16, 1, 3, 4),
    (17, 2, 5, 1);
    
INSERT INTO `treatment` (`id`,`name`,`start_date`,`planned_end_date`,`patient_id`) 
VALUES 
(7,'Obsessive-compulsive disorder treatment','2022-06-01 00:00:00','2023-06-01 00:00:00',29),
(8,'Post-traumatic stress disorder treatment','2023-11-20 00:00:00','2024-11-20 00:00:00',30),
(9,'Eating disorders treatment','2021-04-05 00:00:00','2022-04-05 00:00:00',31),
(10,'Addiction treatment','2019-12-01 00:00:00','2020-12-01 00:00:00',32),
(11,'Dissociative disorders treatment','2020-07-07 00:00:00','2021-07-07 00:00:00',33),
(12,'Sleep disorders treatment','2022-11-01 00:00:00','2023-11-01 00:00:00',34),
(13,'Somatic symptom disorders treatment','2021-08-15 00:00:00','2022-08-15 00:00:00',35),
(14,'Elimination disorders treatment','2023-10-05 00:00:00','2024-10-05 00:00:00',36),
(15,'Gender dysphoria treatment','2022-02-20 00:00:00','2023-02-20 00:00:00',37),
(16,'Impulse control disorders treatment','2021-06-12 00:00:00','2022-06-12 00:00:00',38),
(17,'Substance-related disorders treatment','2020-03-05 00:00:00','2021-03-05 00:00:00',29),
(18,'Neurocognitive disorders treatment','2019-10-01 00:00:00','2020-10-01 00:00:00',30),
(19,'Personality disorders treatment','2023-02-15 00:00:00','2024-02-15 00:00:00',31),
(20,'Paraphilic disorders treatment','2021-09-09 00:00:00','2022-09-09 00:00:00',32),
(21,'Factitious disorders treatment','2019-05-05 00:00:00','2020-05-05 00:00:00',33);




/*-------------------------UPDATES-------------------------*/

UPDATE treatment SET start_date = NOW(), planned_end_date = "2025-05-03" WHERE id = 2;

UPDATE consultation SET `time` = "2023-07-30" WHERE id = 1;

UPDATE dosage SET dose_frequency = "every 8 hours", dose_quantity = "150mg" WHERE id = 3;

UPDATE professional SET salary = 15000 WHERE id = 4;

UPDATE medical_record SET record_date = "2022-04-11" WHERE id = 2;

UPDATE therapy SET capacity = 5 WHERE id = 6;

UPDATE medical_record SET record_date = "2024-08-01" WHERE id = 3;

/*-------------------------DELETES-------------------------*/

DELETE FROM medical_record_included_therapy WHERE id = 2; -- necessário para deletar a terapia abaixo

DELETE FROM therapy WHERE id = 2;

DELETE FROM doctor_update_record WHERE id = 3;

SET SQL_SAFE_UPDATES = 0;
DELETE FROM consultation WHERE `time` < "2023-07-01";
SET SQL_SAFE_UPDATES = 1;
select * from consultation;
SET FOREIGN_KEY_CHECKS = 0;
DELETE FROM patient WHERE id = 13;
SET FOREIGN_KEY_CHECKS = 1;