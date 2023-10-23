USE psychiatric_hospital;
-- Procedures

-- 1. Inserir um novo paciente
DROP PROCEDURE IF EXISTS insert_patient;
DELIMITER $$
CREATE PROCEDURE insert_patient (
    IN _name VARCHAR(200),
    IN _birth_date DATE,
    IN _sex CHAR(1),
    IN _cpf CHAR(11),
    IN _zip CHAR(8),
    IN _street VARCHAR(200),
    IN _street_number INT,
    IN _complement VARCHAR(200),
    IN _neighborhood VARCHAR(200),
    IN _city VARCHAR(200),
    IN _state CHAR(2),
    IN _country CHAR(3),
    IN _phone VARCHAR(14),
    IN _email VARCHAR(50),
    IN _weight FLOAT,
    IN _marital_status VARCHAR(200),
    IN _profession VARCHAR(200),
    IN _emergency_contact_name VARCHAR(200),
    IN _emergency_contact_phone VARCHAR(14),
    IN _health_insurance VARCHAR(50)    
)
	BEGIN
		INSERT INTO person VALUES (NULL, _name, _birth_date, _sex, _cpf, _zip, _street, _street_number, _complement, _neighborhood, _city, _state, _country, _phone, _email);
        INSERT INTO patient VALUES (last_insert_id(), _weight, _marital_status, _profession, _emergency_contact_name, _emergency_contact_phone, _health_insurance, NOW());
        SELECT p.*, pt.* FROM person p
			NATURAL JOIN patient pt
            WHERE p.id = last_insert_id();
    END $$
DELIMITER ;


CALL insert_patient(
    'Alice Smith',
    '1990-01-01',
    'f',
    '12345671524',
    '12345678',
    'Maple Street',
    100,
    'Apt 12B',
    'Downtown',
    'New York',
    'NY',
    'USA',
    '+1234567890',
    'alice.smith@email.com',
    60.5,
    'single',
    'Software Engineer',
    'Bob Smith',
    '+0987654321',
    'MediCare'
);


-- 2. Calcular a proporção de internações de um determinado ano separada e ordenada por mês 
DROP PROCEDURE IF EXISTS hospitalization_proportion;
DELIMITER $$
CREATE PROCEDURE hospitalization_proportion (IN _year INT)
	BEGIN
		DECLARE total INT;
    SET total := (SELECT COUNT(id) FROM patient);
    IF total != 0 THEN -- para evitar divisoes por 0
		SELECT COUNT(*)/total AS "Distribution" , MONTH(hospitalization_date) "Month" FROM patient 
		WHERE YEAR(hospitalization_date) = _year
        GROUP BY MONTH(hospitalization_date)
		ORDER BY MONTH(hospitalization_date);
	ELSE SELECT "NaN";
	END IF;
    END $$
DELIMITER ;

CALL hospitalization_proportion(2023);

-- 3. Tentar vincular um paciente a uma terapia se estiver dentro da capacidade dela
DROP PROCEDURE IF EXISTS insert_mr_to_therapy;
DELIMITER $$
CREATE PROCEDURE insert_mr_to_therapy (IN _medical_record_id INT, IN _therapy_id INT)
	BEGIN
		-- busca a capacidade
        DECLARE cap INT;
        DECLARE cnt INT;
        SET cap := (SELECT capacity FROM therapy WHERE id = _therapy_id);
        SET cnt := (SELECT COUNT(*) FROM medical_record_included_therapy WHERE therapy_id = _therapy_id);
        IF cnt < cap THEN
			INSERT INTO medical_record_included_therapy VALUES (NULL, _medical_record_id, _therapy_id);
            SET cnt := (SELECT COUNT(*) FROM medical_record_included_therapy WHERE therapy_id = _therapy_id);
			SELECT cap, cnt;
		ELSE 
			SELECT CONCAT("No vacancy for therapy id = ", _therapy_id) "Warning";
        END IF;
    END $$
DELIMITER ;

CALL insert_mr_to_therapy(1,6);

-- Functions

-- 1.Retornar o número de consultas de um determinado médico realizado no período do último ano
DROP FUNCTION IF EXISTS n_consultation_doctor;
DELIMITER $$
CREATE FUNCTION n_consultation_doctor (_id INT) RETURNS INT DETERMINISTIC
BEGIN
	DECLARE n_consultation INT;
	SET n_consultation := (SELECT COUNT(*) FROM consultation 
						WHERE doctor_id = _id AND `time` BETWEEN DATE_SUB(NOW(), INTERVAL 1 YEAR) AND NOW() );
	RETURN n_consultation;
END $$
DELIMITER ;
SELECT n_consultation_doctor(4) "Consultations over the last year";

-- 2. Retorna a quantidade de atualizações (médicos e psicólogos) do prontuário de um determinado paciente
DROP FUNCTION IF EXISTS count_updates;
DELIMITER $$
CREATE FUNCTION count_updates (_patient_id INT) RETURNS INT DETERMINISTIC
	BEGIN
		DECLARE mr_id, cnt INT;
        SET mr_id := (SELECT id FROM medical_record WHERE patient_id = _patient_id);
        SET cnt := (SELECT COUNT(*) FROM doctor_update_record WHERE medical_record_id = mr_id);
        SET cnt := cnt + (SELECT COUNT(*) FROM psychologist_update_record WHERE medical_record_id = mr_id);
        RETURN cnt;
    END $$
DELIMITER ;
SELECT count_updates(13) "Total updates in medical record";

-- 3.	Calcular a progressão do tratamento baseado na data de início, a data da última atualização do prontuário e a data planejada do fim do tratamento
DROP FUNCTION IF EXISTS progression;
DELIMITER $$
CREATE FUNCTION progression (_medical_record_id INT) RETURNS FLOAT DETERMINISTIC
	BEGIN
    -- DECLARE pt_id INT;
    DECLARE t_id INT;
    DECLARE str_date, last_update_date, finish_date DATE;
    DECLARE result FLOAT;
    -- SET pt_id := (SELECT patient_id FROM medical_record WHERE id = _medical_record_id);
    SET t_id := (SELECT treatment_id FROM medical_record WHERE id = _medical_record_id);
    /*SET str_date := (SELECT DATE(start_date) FROM treatment WHERE id = t.id);
    SET finish_date := (SELECT DATE(start_date) FROM treatment WHERE id = t.id);*/
    SELECT DATE(start_date), DATE(planned_end_date) INTO str_date, finish_date FROM treatment WHERE id = t_id;
    SET last_update_date := (SELECT record_date FROM medical_record WHERE id = _medical_record_id);
    SET result := (
		CASE
			WHEN last_update_date < str_date THEN 0
            WHEN last_update_date > finish_date THEN 1
            ELSE DATEDIFF(last_update_date, str_date)/DATEDIFF(finish_date, str_date)
		END
	);
    RETURN result;
    END $$
DELIMITER ;
SELECT CONCAT(progression(1)*100, "%") "Progression";

-- Triggers 

-- 1. Atualizar o prontuário médico após a criação de um novo doctor_update record ou psychologist_update_record com o tempo atual
DROP TRIGGER IF EXISTS update_time_doctor;
DELIMITER $$
CREATE TRIGGER update_time_doctor AFTER INSERT ON doctor_update_record
	FOR EACH ROW
		BEGIN
			UPDATE medical_record SET record_date = NOW() WHERE id = NEW.medical_record_id;
        END $$
DELIMITER ;

DROP TRIGGER IF EXISTS update_time_psychologist;
DELIMITER $$
CREATE TRIGGER update_time_psychologist AFTER INSERT ON psychologist_update_record
	FOR EACH ROW
		BEGIN
			UPDATE medical_record SET record_date = NOW() WHERE id = NEW.medical_record_id;
        END $$
DELIMITER ;

SELECT * FROM (doctor_update_record);
SELECT * FROM medical_record;
INSERT INTO doctor_update_record VALUES (NULL, 4, 6);
SELECT * FROM (doctor_update_record);
SELECT * FROM medical_record;

-- 2. Deletar profissional apagando todos os outros registros que possam causar erro de constraint
DROP TRIGGER IF EXISTS delete_professional;
DELIMITER $$
CREATE TRIGGER delete_professional BEFORE DELETE ON professional
	FOR EACH ROW
	BEGIN
		IF EXISTS (SELECT 1 FROM doctor WHERE id = OLD.id) THEN
			DELETE FROM consultation WHERE doctor_id = OLD.id;
			DELETE FROM doctor_suggest_treatment WHERE doctor_id = OLD.id;
			DELETE FROM doctor_update_record WHERE doctor_id = OLD.id;
			DELETE FROM doctor WHERE id = OLD.id;
        ELSEIF (SELECT 1 FROM psychologist WHERE id = OLD.id) THEN
			DELETE FROM psychologist_helps_treatment WHERE psychologist_id = OLD.id;
            DELETE FROM psychologist_update_record WHERE psychologist_id = OLD.id;
            DELETE FROM medical_record_included_therapy WHERE therapy_id = (SELECT id FROM therapy WHERE psychologist_id = OLD.id);
            DELETE FROM therapy WHERE psychologist_id = OLD.id;
            DELETE FROM psychologist WHERE id = OLD.id;
		END IF;	
    END $$
DELIMITER ;

SELECT id FROM doctor;
SELECT id FROM psychologist;
DELETE FROM professional WHERE id = 3;
DELETE FROM professional WHERE id = 12;
-- 3. Corrigir data do fim do tratamento para a ultima atualização no prontuário caso a atualização do prontuário seja maior que o fim
DROP TRIGGER IF EXISTS update_planned_end_date;
DELIMITER $$
CREATE TRIGGER update_planned_end_date AFTER UPDATE ON medical_record
	FOR EACH ROW
    BEGIN
		DECLARE t_id INT;
		DECLARE treatment_end_date DATETIME;
        SET t_id := OLD.treatment_id;
        SET treatment_end_date := (SELECT planned_end_date FROM treatment WHERE id = t_id);
		IF treatment_end_date < CAST(NEW.record_date AS DATETIME) THEN
			UPDATE treatment SET planned_end_date = NEW.record_date WHERE id = t_id;
        END IF ;
    END $$
DELIMITER ;
SELECT * FROM treatment;
UPDATE medical_record SET record_date = "2030-01-01" WHERE id = 1;
