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
SELECT d.`name` AS "Tipo de Transtorno", COUNT(t.id) AS "Quantidade de Tratamentos"
FROM disorder AS d
JOIN treatment_treats_disorder AS ttd ON ttd.disorder_id = d.id
JOIN treatment AS t ON t.id = ttd.treatment_id
GROUP BY d.`name`;

/*-- 10.	Calcular a proporção de pacientes de específico sexo atendidos por psicólogos de específico sexo (count(person.sexo) from person join patient join psychoilogist [buscar a terapia via prontuario], group by patient-psychologist);
SELECT ppt.sex, COUNT(*) FROM patient AS pt
NATURAL JOIN person AS ppt
GROUP BY ppt.sex;
*/


-- 12.	Listar todos os pacientes e os profissionais (médicos e psicólogos) que os atendem;
SELECT p.id "ID paciente", p.`name` "Nome", doc_p.id "ID médico", doc_p.`name` "Médico", psy_p.id "Id psicólogo", psy_p.`name` "Psicólogo" FROM person AS p
NATURAL JOIN patient AS pa
JOIN treatment AS t ON t.patient_id = pa.id
JOIN person AS doc_p ON t.doctor_id = doc_p.id
LEFT JOIN person AS psy_p ON t.psychologist_id = psy_p.id; 

-- 13.	Calcular a média de tempo de tratamento agrupado por transtornos (avg, group by, join treatment_treats_disorder);
SELECT d.`name`, AVG(TIMESTAMPDIFF(DAY, t.start_date, t.planned_end_date)) "Average time" FROM treatment AS t
JOIN treatment_treats_disorder AS ttd ON ttd.treatment_id = t.id
JOIN disorder AS d ON ttd.disorder_id = d.id
GROUP BY d.`name`;


-- 14.  Verificar quais transtornos estão sendo tratados atualmente;
SELECT d.`type` AS "Tipo de Transtorno"
FROM treatment AS t
JOIN disorder AS d ON t.disorder_id = d.id
WHERE NOW() < t.end_date;

-- 15.	Contar os profissionais na equipe agrupado por especialização 
SELECT speciality "Speciality", COUNT(*) "Quantity"FROM professional GROUP BY speciality;

-- 16.  Listar todos os pacientes que receberam ajuda por nome do psicólogo;
SELECT p.`name` AS "Nome do Paciente", psy.`name` AS "Nome do Psicólogo"
FROM patient AS p
JOIN medical_record AS mr ON p.medical_record_id = mr.id
JOIN medical_record_included_therapy AS mrit ON mr.id = mrit.medical_record_id
JOIN therapy AS t ON mrit.therapy_id = t.id
JOIN psychologist AS psy ON t.psychologist_id = psy.id
GROUP BY psy.`name`
ORDER BY psy.`name`;

SELECT p.`name` "Patient name", ppsy.`name` "Psychologist name" FROM person AS p
NATURAL JOIN patient AS pt
JOIN treatment AS t ON pt.id = t.patient_id
JOIN psychologist_helps_treatment AS pht ON pht.treatment_id = t.id
JOIN psychologist AS psy ON pht.psychologist_id = psy.id
JOIN person AS ppsy ON pht.id = ppsy.id; 
;

;
select * from psychologist_helps_treatment;
insert into psychologist_helps_treatment (psychologist_id, treatment_id)VALUES (7,3);
describe psychologist_helps_treatment;


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

describe consultation;