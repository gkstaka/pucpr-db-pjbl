USE psychiatric_hospital;

-- 1.	Contar quantidade total de pacientes atendidos;

SELECT COUNT(*) 'Total patients' FROM patient;

-- 2.	Contar a quantidade de total de consultas realizadas;
SELECT COUNT(*) 'Total consultations' FROM consultation;

-- 3.	Contar a quantidade de total terapias realizadas;
SELECT COUNT(*) 'Total therapies' FROM therapy;

-- 5.	Listar profissionais por ordem de salário;
SELECT * FROM professional ORDER BY salary;

-- 12.	Listar todos os pacientes e os profissionais (médicos e psicólogos) que os atendem
SELECT p.id "ID paciente", p.`name` "Nome", doc_p.id "ID médico", doc_p.`name` "Médico", psy_p.id "Id psicólogo", psy_p.`name` "Nome" FROM person AS p
NATURAL JOIN patient AS pa
JOIN treatment AS t ON t.patient_id = pa.id
JOIN person AS doc_p ON t.doctor_id = doc_p.id
LEFT JOIN person AS psy_p ON t.psychologist_id = psy_p.id; 