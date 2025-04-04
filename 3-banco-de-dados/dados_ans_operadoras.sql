create database dados_ans;
use dados_ans;

create table operadoras (
    Registro_ANS int not null primary key,
    CNPJ varchar(14) not null,
    Razao_Social varchar(255) not null,
    Nome_Fantasia varchar(255),
    Modalidade varchar(100) not null,
    Logradouro varchar(255) not null,
    Numero varchar(20),
    Complemento varchar(255),
    Bairro varchar(100),
    Cidade varchar(100) not null,
    UF char(2) not null,
    CEP varchar(8),
    DDD char(2),
    Telefone varchar(20),
    Fax varchar(15),
    Endereco_eletronico varchar(255),
    Representante varchar(255),
    Cargo_Representante varchar(255),
    Regiao_de_Comercializacao int,
    Data_Registro_ANS date
);

load data infile 'D:\\intuitivecare\\anexos\\dados_ans\\Relatorio_cadop.csv'
into table operadoras
fields terminated by ';'
enclosed by '"'
lines terminated by '\n'
ignore 1 rows
(Registro_ANS, CNPJ, Razao_Social, Nome_Fantasia, Modalidade, Logradouro, Numero, Complemento, Bairro, Cidade, UF, CEP, DDD, Telefone, Fax, Endereco_eletronico, Representante, Cargo_Representante, @Regiao_de_Comercializacao, Data_Registro_ANS)
set Regiao_de_Comercializacao = NULLIF(@Regiao_de_Comercializacao, '');

select * from operadoras LIMIT 10;

select * from operadoras WHERE Regiao_de_Comercializacao IS NULL;

Select * from operadoras Modalidade;


select Registro_ANS, CNPJ, Razao_Social, Modalidade, Cidade, UF, Representante from operadoras where Nome_Fantasia like 'ALLIANZ';




