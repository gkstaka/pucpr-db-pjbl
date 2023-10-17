USE psychiatric_hospital;

-- 1.	Contar quantidade total de pacientes atendidos;

SELECT COUNT(*) 'Total patients' FROM patient;

-- 2.	Contar a quantidade de total de consultas realizadas;
SELECT COUNT(*) 'Total consultations' FROM consultation;

-- 3.	Contar a quantidade de total terapias realizadas;
SELECT COUNT(*) 'Total therapies' FROM therapy;

-- 4.   Listar todos os tratamentos em andamento;
SELECT p.id "ID paciente", p.`name` "Nome do Paciente", doc_p.id "ID médico", doc_p.`name` "Nome do Médico", psy_p.id "ID psicólogo", psy_p.`name` "Nome do Psicólogo"
FROM person AS p
NATURAL JOIN patient AS pa
JOIN treatment AS t ON t.patient_id = pa.id
JOIN person AS doc_p ON t.doctor_id = doc_p.id
LEFT JOIN person AS psy_p ON t.psychologist_id = psy_p.id
WHERE NOW() < t.end_date;

-- 5.	Listar profissionais por ordem de salário;
SELECT * FROM professional ORDER BY salary;

-- 6.   Agrupar e contar pacientes com o mesmo tipo de transtorno;
SELECT d.`type` AS "Tipo de Transtorno", COUNT(p.id) AS "Quantidade de Pacientes"
FROM patient AS p
JOIN disorder AS d ON p.disorder_id = d.id
GROUP BY d.`type`;

-- 12.	Listar todos os pacientes e os profissionais (médicos e psicólogos) que os atendem;
SELECT p.id "ID paciente", p.`name` "Nome", doc_p.id "ID médico", doc_p.`name` "Médico", psy_p.id "Id psicólogo", psy_p.`name` "Psicólogo" FROM person AS p
NATURAL JOIN patient AS pa
JOIN treatment AS t ON t.patient_id = pa.id
JOIN person AS doc_p ON t.doctor_id = doc_p.id
LEFT JOIN person AS psy_p ON t.psychologist_id = psy_p.id; 

-- 14.  Verificar quais transtornos estão sendo tratados atualmente;
SELECT d.`type` AS "Tipo de Transtorno"
FROM treatment AS t
JOIN disorder AS d ON t.disorder_id = d.id
WHERE NOW() < t.end_date;

-- 16.  Listar todos os pacientes que receberam ajuda por nome do psicólogo;
SELECT p.`name` AS "Nome do Paciente", psy.`name` AS "Nome do Psicólogo"
FROM patient AS p
JOIN medical_record AS mr ON p.medical_record_id = mr.id
JOIN medical_record_included_therapy AS mrit ON mr.id = mrit.medical_record_id
JOIN therapy AS t ON mrit.therapy_id = t.id
JOIN psychologist AS psy ON t.psychologist_id = psy.id
GROUP BY psy.`name`
ORDER BY psy.`name`;

-- 19.  Listar os psicólogos que mais atualizaram o prontuário;
SELECT p.`name` AS "Nome do Psicólogo", COUNT(du.id) AS "Quantidade de Atualizações"
FROM psychologist AS p
JOIN doctor_update_record AS du ON p.id = du.psychologist_id
GROUP BY p.`name`
ORDER BY COUNT(du.id) DESC;
