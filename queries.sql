USE psychiatric_hospital;

-- 1.	Contar quantidade total de pacientes atendidos;

SELECT COUNT(*) 'Total patients' FROM patient;

-- 2.	Contar a quantidade de total de consultas realizadas;
SELECT COUNT(*) 'Total consultations' FROM consultation;

-- 3.	Contar a quantidade de total terapias realizadas;
SELECT COUNT(*) 'Total therapies' FROM therapy;

-- 4.   Listar todos os tratamentos em andamento;
SELECT t.*, p.`name` "Patient name" FROM treatment AS t
JOIN patient AS pt ON t.patient_id = pt.id
JOIN person AS p ON p.id = pt.id
WHERE NOW() < t.planned_end_date;

-- 5.	Listar profissionais por ordem de salário;
SELECT * FROM professional ORDER BY salary;

-- 6.   Agrupar e contar tratamentos com o mesmo tipo de transtorno;
SELECT d.`name` AS "Disorder name", COUNT(t.id) AS "Treatments count"
FROM disorder AS d
JOIN treatment_treats_disorder AS ttd ON ttd.disorder_id = d.id
JOIN treatment AS t ON t.id = ttd.treatment_id
GROUP BY d.`name`;

-- 7.	Encontrar a média de medicamentos tomados por total de pacientes;
SELECT COUNT(suggestion.id )/COUNT(mr.id) "Average medication taken" FROM suggestion
JOIN medical_record mr ON mr.id = suggestion.medical_record_id ;

-- 8.	Mostrar quantidade de internação separados por mês
SELECT COUNT(p.id) , MONTH(hospitalization_date) AS `month` FROM patient AS p
GROUP BY `month`
ORDER BY `month`;


-- 9.	Calcular a proporção de pacientes de específico sexo consultados por médicos de específico sexo;
SELECT ppt.sex "Patient sex", pdc.sex "Doctor sex", COUNT(*) "Total" FROM patient AS pt
NATURAL JOIN person AS ppt
JOIN consultation AS c ON c.patient_id = pt.id
JOIN doctor AS d ON c.doctor_id = d.id
JOIN person AS pdc ON d.id = pdc.id
GROUP BY ppt.sex, pdc.sex
ORDER BY pdc.sex;

-- 10.	Calcular a proporção de pacientes de específico sexo atendidos por psicólogos de específico sexo;
SELECT ppt.sex "Patient sex", ppsy.sex "Psychologist sex", COUNT(*) "" FROM patient AS pt
NATURAL JOIN person AS ppt
JOIN treatment AS t ON ppt.id = t.patient_id
JOIN psychologist_helps_treatment AS pht ON pht.treatment_id = t.id
JOIN psychologist AS psy ON pht.psychologist_id = psy.id
JOIN person AS ppsy ON psy.id = ppsy.id
GROUP BY ppt.sex, ppsy.sex
ORDER BY ppsy.sex;

-- 11.	Listar os transtornos em ordem de quais são podem ser mais comuns;
SELECT * FROM disorder
ORDER BY disorder.prevalence DESC;

-- 12.	Listar todos os pacientes e os profissionais (médicos e psicólogos) que os atendem;
SELECT p.id "ID paciente", p.`name` "Nome", doc_p.id "ID médico", doc_p.`name` "Médico", psy_p.id "Id psicólogo", psy_p.`name` "Psicólogo" FROM person AS p
NATURAL JOIN patient AS pa
JOIN treatment AS t ON t.patient_id = pa.id
LEFT JOIN doctor_suggest_treatment AS dt ON dt.treatment_id = t.id
JOIN doctor AS d ON dt.doctor_id = d.id
JOIN person AS doc_p ON d.id = doc_p.id
LEFT JOIN psychologist_helps_treatment AS pht ON pht.treatment_id = t.id
JOIN psychologist AS psy ON psy.id = pht.psychologist_id
JOIN person AS psy_p ON psy.id = psy_p.id; 

-- 13.	Calcular a média de tempo de tratamento agrupado por transtornos (avg, group by, join treatment_treats_disorder);
SELECT d.`name`, AVG(TIMESTAMPDIFF(DAY, t.start_date, t.planned_end_date)) "Average time" FROM treatment AS t
JOIN treatment_treats_disorder AS ttd ON ttd.treatment_id = t.id
JOIN disorder AS d ON ttd.disorder_id = d.id
GROUP BY d.`name`;


-- 14.  Verificar quais transtornos estão sendo tratados atualmente;
SELECT d.`name` AS "Transtorno", COUNT(t.id) "quantidade" 
FROM treatment AS t
JOIN treatment_treats_disorder AS ttd ON ttd.treatment_id = t.id
JOIN disorder AS d ON ttd.disorder_id = d.id
WHERE NOW() < t.planned_end_date
GROUP BY d.`name`;

-- 15.	Contar os profissionais na equipe agrupado por especialização 
SELECT speciality "Speciality", COUNT(*) "Quantity" FROM professional GROUP BY speciality;

-- 16.  Listar todos os pacientes que receberam ajuda por nome do psicólogo;
SELECT ppsy.`name` "Psychologist name", p.`name` "Patient name" FROM person AS p
NATURAL JOIN patient AS pt
JOIN treatment AS t ON pt.id = t.patient_id
JOIN psychologist_helps_treatment AS pht ON pht.treatment_id = t.id
JOIN psychologist AS psy ON pht.psychologist_id = psy.id
JOIN person AS ppsy ON pht.id = ppsy.id
ORDER BY ppsy.`name`; 

-- 17.	Contar pacientes de acordo com o estado civil
SELECT marital_status , COUNT(*) FROM patient
GROUP BY marital_status;



-- 18.	Listar os médicos que mais atualizaram o prontuário (select doctor, count(doctor_update_record) from doctor join doctor_update_record group by doctor)
SELECT p.`name` "Name", COUNT(dur.id) "Medical records updated" FROM doctor_update_record AS dur
JOIN doctor AS d ON d.id = dur.doctor_id
JOIN professional AS pr ON pr.id = d.id
JOIN person AS p ON p.id = pr.id
GROUP BY d.id
ORDER BY COUNT(dur.id) DESC;
describe doctor_update_record;


-- 19.  Listar os psicólogos que mais atualizaram o prontuário;
SELECT p.`name` AS "Nome do Psicólogo", COUNT(pur.id) AS "Quantidade de Atualizações"
FROM psychologist AS psy
JOIN professional AS pf ON pf.id = psy.id
JOIN person AS p ON p.id = pf.id
JOIN psychologist_update_record AS pur ON p.id = pur.psychologist_id
GROUP BY p.`name`
ORDER BY COUNT(pur.id) DESC;


-- 20.	Encontrar o médico que mais atendeu consultas agrupados por mês (count consultation join doctor group by month group by doctor order by count desc limit 1)
SELECT p.`name`, COUNT(c.id) "Consultation stats" FROM doctor AS d
NATURAL JOIN professional
NATURAL JOIN person AS p
JOIN consultation AS c ON c.doctor_id = d.id
GROUP BY p.`name`
LIMIT 1;


-- Views
-- 1. Listar todos os dados de todos os pacientes
CREATE OR REPLACE VIEW view_patients AS	
		SELECT p.*, pt.weight, pt.marital_status, pt.profession, pt.emergency_contact_name, pt.emergency_contact_phone, pt.health_insurance, pt.hospitalization_date FROM person p
        NATURAL JOIN patient pt
        ORDER BY pt.hospitalization_date;
SELECT * FROM view_patients;

-- 2. Listar diagnósticos de pacientes 
CREATE OR REPLACE VIEW diagnosis AS
	SELECT pt.id "patient id", pt.weight, pt.marital_status, pt.profession, pt.health_insurance, pt.hospitalization_date, d.`name` "disorder" FROM patient AS pt
    JOIN treatment AS t ON t.patient_id = pt.id
    JOIN treatment_treats_disorder AS ttd ON ttd.treatment_id = t.id
    JOIN disorder AS d ON d.id = ttd.disorder_id;
SELECT * FROM diagnosis;

-- 3. Mostrar coquetel de remédios de cada prontuário médico
CREATE OR REPLACE VIEW misc_medicine_info AS
	SELECT mr.id "Medical record id", m.`name` , d.dose_quantity, d.dose_frequency FROM medical_record AS mr
	JOIN suggestion AS s ON s.medical_record_id = mr.id
    JOIN medicine AS m ON m.id = s.medicine_id
    JOIN dosage AS d ON d.id = s.dosage_id
    ORDER BY mr.id;
SELECT * FROM misc_medicine_info;