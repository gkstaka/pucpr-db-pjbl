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
(1,'Anxiety treatment','2022-07-15 00:00:00','2023-07-15 00:00:00',13),
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