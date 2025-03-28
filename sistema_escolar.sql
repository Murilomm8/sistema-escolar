-- Criação do Banco de Dados
CREATE DATABASE SistemaEscolar;

-- Selecionar o Banco de Dados
USE SistemaEscolar;

-- Tabela Aluno
CREATE TABLE Aluno (
    id_aluno INT AUTO_INCREMENT PRIMARY KEY,
    nome_completo VARCHAR(255) NOT NULL,
    data_nascimento DATE NOT NULL,
    id_turma INT,
    nome_responsavel VARCHAR(255),
    telefone_responsavel VARCHAR(20),
    email_responsavel VARCHAR(100),
    informacoes_adicionais TEXT,
    FOREIGN KEY (id_turma) REFERENCES Turma(id_turma)
);

-- Tabela Turma
CREATE TABLE Turma (
    id_turma INT AUTO_INCREMENT PRIMARY KEY,
    nome_turma VARCHAR(50) NOT NULL,
    id_professor INT NOT NULL,
    horario VARCHAR(100) NOT NULL,
    FOREIGN KEY (id_professor) REFERENCES Professor(id_professor)
);

-- Tabela Professor
CREATE TABLE Professor (
    id_professor INT AUTO_INCREMENT PRIMARY KEY,
    nome_completo VARCHAR(255) NOT NULL,
    email VARCHAR(100) NOT NULL,
    telefone VARCHAR(20) NOT NULL
);

-- Tabela Pagamento
CREATE TABLE Pagamento (
    id_pagamento INT AUTO_INCREMENT PRIMARY KEY,
    id_aluno INT NOT NULL,
    data_pagamento DATE NOT NULL,
    valor_pago DECIMAL(10, 2) NOT NULL,
    forma_pagamento VARCHAR(50) NOT NULL,
    referencia VARCHAR(100) NOT NULL,
    status VARCHAR(20) NOT NULL,
    FOREIGN KEY (id_aluno) REFERENCES Aluno(id_aluno)
);

-- Tabela Presenca
CREATE TABLE Presenca (
    id_presenca INT AUTO_INCREMENT PRIMARY KEY,
    id_aluno INT NOT NULL,
    data_presenca DATE NOT NULL,
    presente BOOLEAN NOT NULL,
    FOREIGN KEY (id_aluno) REFERENCES Aluno(id_aluno)
);

-- Tabela Atividade
CREATE TABLE Atividade (
    id_atividade INT AUTO_INCREMENT PRIMARY KEY,
    descricao TEXT NOT NULL,
    data_realizacao DATE NOT NULL
);

-- Tabela Atividade_Aluno (Relação N:N entre Aluno e Atividade)
CREATE TABLE Atividade_Aluno (
    id_atividade INT NOT NULL,
    id_aluno INT NOT NULL,
    PRIMARY KEY (id_atividade, id_aluno),
    FOREIGN KEY (id_atividade) REFERENCES Atividade(id_atividade),
    FOREIGN KEY (id_aluno) REFERENCES Aluno(id_aluno)
);

-- Tabela Usuario
CREATE TABLE Usuario (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    login VARCHAR(50) UNIQUE NOT NULL,
    senha VARCHAR(255) NOT NULL,
    nivel_acesso VARCHAR(20) NOT NULL,
    id_professor INT,
    FOREIGN KEY (id_professor) REFERENCES Professor(id_professor)
);