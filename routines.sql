USE psychiatric_hospital;

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

DROP PROCEDURE IF EXISTS hospitalization_proportion;
DELIMITER $$
CREATE PROCEDURE hospitalization_proportion (IN _year INT)
	BEGIN
		DECLARE total INT;
    SET total := (SELECT COUNT(id) FROM patient);
    IF total != 0 THEN
		SELECT COUNT(*)/total AS "Distribution" , MONTH(hospitalization_date) "Month" FROM patient 
		WHERE YEAR(hospitalization_date) = _year
        GROUP BY MONTH(hospitalization_date)
		ORDER BY MONTH(hospitalization_date);
	ELSE SELECT total "Total";
	END IF;
    END $$
DELIMITER ;

CALL hospitalization_proportion(2023);