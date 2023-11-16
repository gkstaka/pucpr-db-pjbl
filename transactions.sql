USE psychiatric_hospital;

-- Adiciona novo médico
SET autocommit = FALSE;
START TRANSACTION;
INSERT INTO person VALUES(NULL, "Gustavo Takahashi", "2000-01-01", "m", "12323434545", "11111112", "Rua das Flores", 1234, "", "Portao", "Curitiba", "PR", "BRL", "12312312", "email@email.com");
INSERT INTO professional VALUES (last_insert_id(),"AAAAASSSSA", 10000, NOW(), "Range12", "Specialty 1", 300);
INSERT INTO doctor VALUES(last_insert_id(),"2364344");
COMMIT;

-- Adiciona um novo psicólogo
START TRANSACTION;
INSERT INTO person VALUES(NULL, "João Manuel", "2000-01-01", "m", "12323434645", "11111112", "Rua das Flores", 1234, "", "Portao", "Curitiba", "PR", "BRL", "12312312", "email@email.com");
INSERT INTO professional VALUES (last_insert_id(),"AAAAASSSbb", 10000, NOW(), "Range12", "Specialty 1", 300);
INSERT INTO psychologist VALUES(last_insert_id(),"44");
COMMIT;

-- Adiciona um novo paciente
START TRANSACTION;
INSERT INTO person VALUES(NULL, "Agata Cristina", "2000-01-01", "f", "12323333545", "11111112", "Rua das Flores", 1234, "", "Portao", "Curitiba", "PR", "BRL", "12312312", "email@email.com");
INSERT INTO patient VALUES(last_insert_id(), 55, "solteiro", "dev", "nome1", "98877987", "Unimed", NOW());
COMMIT;

-- Associa um tratamento a um transtorno
START TRANSACTION;
SET @id_disorder = (SELECT id FROM disorder WHERE name = "Depression");
SET @id_treatment = (SELECT id from treatment WHERE patient_id = 13);
INSERT INTO treatment_treats_disorder VALUES (NULL, @id_treatment, @id_disorder);
COMMIT; 


-- Reverte uma atualização no prontuário médico
START TRANSACTION;
UPDATE medical_record SET record_date = DATE(NOW()), description = "Patient is suffering from ...." WHERE id = 1;
ROLLBACK;

-- Reverte inserção de medicamento com sugestão
START TRANSACTION;
INSERT INTO medicine VALUES (NULL, "Medicine1", "Composition1", "Usage1", "Indication1", "Contraindication1");
SET @id_medicine := (SELECT last_insert_id());
INSERT INTO dosage VALUES (NULL, "100mg", "2x dia");
SET @id_dosage := (SELECT last_insert_id());
INSERT INTO suggestion VALUES (@id_medicine, @id_dosage, 1, NULL);
ROLLBACK;

-- Reverte inserção erronea de médico
START TRANSACTION;
INSERT INTO person VALUES(NULL, "Castro Nunes da Rocha", "2000-01-01", "m", "22323333545", "11111112", "Rua das Flores", 1234, "", "Portao", "Curitiba", "PR", "BRL", "12312312", "email@email.com");
SET @last_id = (SELECT last_insert_id());
INSERT INTO professional VALUES (@last_id,"AsAAASSSSA", 10000, NOW(), "Range13", "Specialty 4", 350);
INSERT INTO doctor VALUES(@last_id, "1231232");
ROLLBACK;

-- Reverte uma atualização do tratamento que deveria ter o ano após a data atual
START TRANSACTION;
UPDATE treatment SET planned_end_date = "2022-02-05" WHERE id = 2;
ROLLBACK;


-- Commit ou rollback to save point caso a data de hospitalização de um paciente for maior que a data atual. Ainda deixara salvo a inserção da pessoa
START TRANSACTION;
DELIMITER $$
CREATE PROCEDURE hospitalization()
BEGIN
	DECLARE last_id INT;
	INSERT INTO person VALUES(NULL, "Maria Julia", "2000-01-01", "f", "12323553545", "11211112", "Rua das Flores", 1234, "", "Portao", "Curitiba", "PR", "BRL", "12312312", "email@email.com");
	SET last_id := (SELECT last_insert_id);
    SAVEPOINT person_sp;
    INSERT INTO patient VALUES(last_insert_id(), 55, "solteiro", "dev", "nome1", "98877987", "Unimed", "2025-05-05");
    IF (SELECT hospitalization_date FROM patient WHERE id = last_id) > DATE(NOW()) THEN
		ROLLBACK TO SAVEPOINT person_cp;
	ELSE 
		COMMIT;
	END IF;
END $$
DELIMITER ;
CALL hospitalization();

-- Insert de prontuário e colocação em uma terapia com rollback na inserção pois terapia já está lotada
START TRANSACTION;
INSERT INTO medical_record VALUES(NULL, DATE(NOW()), "Descriçao 1", 14, 2);
SET @last_id = (SELECT last_insert_id());
SAVEPOINT medical_record_sp;
INSERT INTO medical_record_included_therapy VALUES(NULL, @last_id, 3);
UPDATE therapy SET capacity = (SELECT capacity FROM therapy WHERE id = 3) WHERE id = 3;
ROLLBACK TO medical_record_sp;
COMMIT;
