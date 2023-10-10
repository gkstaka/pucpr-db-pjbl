USE psychiatric_ hospital;

-- 1.	Contar quantidade total de pacientes atendidos;

SELECT COUNT(*) FROM pacient;

-- 2.	Contar a quantidade de total de consultas realizadas;
SELECT COUNT(*) FROM consultation;

-- 3.	Contar a quantidade de total terapias realizadas;
SELECT COUNT(*) FROM therapy;

-- 4.	Listar profissionais por ordem de salário;
SELECT * FROM professional ORDER BY salary;
