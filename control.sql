/*-------------------------PJBL fase 3---------------------*/

-- Criação dos usuários
CREATE USER IF NOT EXISTS 'andre.souza'@'localhost' IDENTIFIED BY 'senha123';
CREATE USER IF NOT EXISTS 'bruno.miglioretto'@'localhost' IDENTIFIED BY 'senha123';
CREATE USER IF NOT EXISTS 'gustavo.takahashi'@'localhost' IDENTIFIED BY 'senha123';
CREATE USER IF NOT EXISTS 'nicolas.zamprogno'@'localhost' IDENTIFIED BY 'senha123';
CREATE USER IF NOT EXISTS 'user.teste1'@'localhost' IDENTIFIED BY 'senha123';
CREATE USER IF NOT EXISTS 'user.teste2'@'localhost' IDENTIFIED BY 'senha123';

-- Criação dos papéis
CREATE ROLE IF NOT EXISTS admin;
CREATE ROLE IF NOT EXISTS manager;
CREATE ROLE IF NOT EXISTS patient;
CREATE ROLE IF NOT EXISTS secretary;
CREATE ROLE IF NOT EXISTS doctor;

-- Concessão dos papéis
-- Admin tem todos os privilégios para todas as tabelas
GRANT ALL PRIVILEGES ON *.* TO admin;

-- Manager pode selecionar, inserir e atualizar dados em todas as tabelas
GRANT SELECT, INSERT, UPDATE ON *.* TO manager;

-- Paciente pode ver alguns dados
GRANT SELECT ON psychiatric_hospital.consultation TO patient;
GRANT SELECT ON psychiatric_hospital.medical_record TO patient;
GRANT SELECT ON psychiatric_hospital.suggestion TO patient;
GRANT SELECT ON psychiatric_hospital.therapy TO patient;
GRANT SELECT ON psychiatric_hospital.treatment TO patient;

-- Secretário pode atualizar todas as tabelas do banco de dados do hospital psiquiátrico
GRANT ALL PRIVILEGES ON psychiatric_hospital.* TO secretary;

-- Médicos podem atualizar suas informações livremente no banco de dados
GRANT SELECT, INSERT, UPDATE ON psychiatric_hospital.doctor TO doctor;

-- Atribuição dos papéis criados anteriormente
GRANT secretary TO 'andre.souza'@'localhost';
GRANT manager TO 'bruno.miglioretto'@'localhost';
GRANT admin TO 'gustavo.takahashi'@'localhost';
GRANT doctor TO 'nicolas.zamprogno'@'localhost';
GRANT patient TO 'user.teste1'@'localhost';
GRANT patient TO 'user.teste2'@'localhost';