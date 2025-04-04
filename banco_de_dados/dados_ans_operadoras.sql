CREATE DATABASE dados_ans;
USE dados_ans;

CREATE TABLE operadoras (
    Registro_ANS INT NOT NULL PRIMARY KEY,
    CNPJ VARCHAR(14) NOT NULL,
    Razao_Social VARCHAR(255) NOT NULL,
    Nome_Fantasia VARCHAR(255),
    Modalidade VARCHAR(100) NOT NULL,
    Logradouro VARCHAR(255) NOT NULL,
    Numero VARCHAR(20),
    Complemento VARCHAR(255),
    Bairro VARCHAR(100),
    Cidade VARCHAR(100) NOT NULL,
    UF CHAR(2) NOT NULL,
    CEP VARCHAR(8),
    DDD CHAR(2),
    Telefone VARCHAR(20),
    Fax VARCHAR(15),
    Endereco_eletronico VARCHAR(255),
    Representante VARCHAR(255),
    Cargo_Representante VARCHAR(255),
    Regiao_de_Comercializacao INT,
    Data_Registro_ANS DATE
);

LOAD DATA INFILE 'D:\\intuitivecare\\anexos\\dados_ans\\Relatorio_cadop.csv'
INTO TABLE operadoras
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(Registro_ANS, CNPJ, Razao_Social, Nome_Fantasia, Modalidade, Logradouro, Numero, Complemento, Bairro, Cidade, UF, CEP, DDD, Telefone, Fax, Endereco_eletronico, Representante, Cargo_Representante, @Regiao_de_Comercializacao, Data_Registro_ANS)
SET Regiao_de_Comercializacao = NULLIF(@Regiao_de_Comercializacao, '');

SELECT * FROM operadoras LIMIT 10;

SELECT * FROM operadoras WHERE Regiao_de_Comercializacao IS NULL;

CREATE TABLE despesas_operadoras (
    id INT AUTO_INCREMENT PRIMARY KEY,
    data DATE NOT NULL,
    reg_ans INT NOT NULL,
    cd_conta_contabil VARCHAR(10) NOT NULL,
    descricao VARCHAR(255) NOT NULL,
    vl_saldo_inicial VARCHAR(50),
    vl_saldo_final VARCHAR(50)
);



