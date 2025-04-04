USE dados_ans;

CREATE TABLE despesas_operadoras (
    id INT AUTO_INCREMENT PRIMARY KEY,
    data DATE NOT NULL,
    reg_ans INT NOT NULL,
    cd_conta_contabil VARCHAR(10) NOT NULL,
    descricao TEXT,
    vl_saldo_inicial DECIMAL(15,2),
    vl_saldo_final DECIMAL(15,2)
);
drop table despesas_operadoras;

LOAD DATA INFILE 'D:\\intuitivecare\\anexos\\dados_ans\\1T2024\\1T2024.csv' INTO TABLE despesas_operadoras
FIELDS TERMINATED BY ';' ENCLOSED BY '"' LINES TERMINATED BY '\n' IGNORE 1 ROWS
(@data, @reg_ans, @cd_conta_contabil, @descricao, @vl_saldo_inicial, @vl_saldo_final)
SET data = STR_TO_DATE(@data, '%Y-%m-%d'), reg_ans = CAST(@reg_ans AS UNSIGNED), cd_conta_contabil = @cd_conta_contabil,
descricao = @descricao, vl_saldo_inicial = CAST(REPLACE(@vl_saldo_inicial, ',', '.') AS DECIMAL(15,2)),
vl_saldo_final = CAST(REPLACE(@vl_saldo_final, ',', '.') AS DECIMAL(15,2));

LOAD DATA INFILE 'D:\\intuitivecare\\anexos\\dados_ans\\2T2024\\2T2024.csv' INTO TABLE despesas_operadoras
FIELDS TERMINATED BY ';' ENCLOSED BY '"' LINES TERMINATED BY '\n' IGNORE 1 ROWS
(@data, @reg_ans, @cd_conta_contabil, @descricao, @vl_saldo_inicial, @vl_saldo_final)
SET data = STR_TO_DATE(@data, '%Y-%m-%d'), reg_ans = CAST(@reg_ans AS UNSIGNED), cd_conta_contabil = @cd_conta_contabil,
descricao = @descricao, vl_saldo_inicial = CAST(REPLACE(@vl_saldo_inicial, ',', '.') AS DECIMAL(15,2)),
vl_saldo_final = CAST(REPLACE(@vl_saldo_final, ',', '.') AS DECIMAL(15,2));

LOAD DATA INFILE 'D:\\intuitivecare\\anexos\\dados_ans\\3T2024\\3T2024.csv' INTO TABLE despesas_operadoras
FIELDS TERMINATED BY ';' ENCLOSED BY '"' LINES TERMINATED BY '\n' IGNORE 1 ROWS
(@data, @reg_ans, @cd_conta_contabil, @descricao, @vl_saldo_inicial, @vl_saldo_final)
SET data = STR_TO_DATE(@data, '%Y-%m-%d'), reg_ans = CAST(@reg_ans AS UNSIGNED), cd_conta_contabil = @cd_conta_contabil,
descricao = @descricao, vl_saldo_inicial = CAST(REPLACE(@vl_saldo_inicial, ',', '.') AS DECIMAL(15,2)),
vl_saldo_final = CAST(REPLACE(@vl_saldo_final, ',', '.') AS DECIMAL(15,2));

LOAD DATA INFILE 'D:\\intuitivecare\\anexos\\dados_ans\\4T2024\\4T2024.csv' INTO TABLE despesas_operadoras
FIELDS TERMINATED BY ';' ENCLOSED BY '"' LINES TERMINATED BY '\n' IGNORE 1 ROWS
(@data, @reg_ans, @cd_conta_contabil, @descricao, @vl_saldo_inicial, @vl_saldo_final)
SET data = STR_TO_DATE(@data, '%Y-%m-%d'), reg_ans = CAST(@reg_ans AS UNSIGNED), cd_conta_contabil = @cd_conta_contabil,
descricao = @descricao, vl_saldo_inicial = CAST(REPLACE(@vl_saldo_inicial, ',', '.') AS DECIMAL(15,2)),
vl_saldo_final = CAST(REPLACE(@vl_saldo_final, ',', '.') AS DECIMAL(15,2));

SELECT 
    cd_conta_contabil, 
    SUM(vl_saldo_final) AS total_despesa
FROM 
    despesas_operadoras
WHERE 
    REPLACE(TRIM(descricao), '  ', ' ') = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR'
    AND data >= DATE_SUB((SELECT MAX(data) FROM despesas_operadoras), INTERVAL 3 MONTH)
GROUP BY 
    cd_conta_contabil
ORDER BY 
    total_despesa DESC
LIMIT 10;

SELECT 
    cd_conta_contabil, 
    SUM(vl_saldo_final) AS total_despesa
FROM 
    despesas_operadoras
WHERE 
    REPLACE(TRIM(descricao), '  ', ' ') = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR'
    AND data >= DATE_SUB((SELECT MAX(data) FROM despesas_operadoras), INTERVAL 1 YEAR)
GROUP BY 
    cd_conta_contabil
ORDER BY 
    total_despesa DESC
LIMIT 10;

select * from despesas_operadoras where descricao = 'Planos Individuais/Familiares antes da Lei';

SELECT data, COUNT(*) as qtd_registros
FROM despesas_operadoras
GROUP BY data
ORDER BY data DESC;

