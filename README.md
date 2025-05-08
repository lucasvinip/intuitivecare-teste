# Projeto ANS - Extração, Processamento e Visualização de Dados

Este projeto realiza um fluxo completo de obtenção, tratamento e visualização de dados da ANS (Agência Nacional de Saúde Suplementar), integrando Python, MySQL e Vue.js para facilitar a análise de dados relacionados às operadoras de planos de saúde.

---

## ✅ Etapas Concluídas

### 1. Web Scraping dos Anexos I e II

- **Objetivo**: Acessar o site da ANS, baixar os PDFs dos Anexos I e II e compactar em .zip.
- **Tecnologias**: `requests`, `BeautifulSoup`, `zipfile`
- **Status**: Finalizado com ajustes no caminho de salvamento na pasta principal.

### 2. Extração de tabela do Anexo I

- **Objetivo**: Extrair a tabela do PDF, substituir abreviações por textos completos, salvar em CSV e compactar.
- **Tecnologias**: `pdfplumber`, `pandas`, `zipfile`
- **Status**: Finalizado com ajustes no caminho.

### 3. Coleta de Dados Abertos da ANS

- **Objetivo**: Acessar diretórios públicos da ANS, baixar arquivos .zip dos anos de 2023 e 2024, e arquivos .csv, e extrair para pastas.
- **Tecnologias**: `requests`, `BeautifulSoup`, `zipfile`
- **Status**: Finalizado, com pasta `dados_ans` salva corretamente.

### 4. Frontend com Vue.js + Backend em Python

- **Objetivo**: Criar uma interface frontend que se comunica com a API Flask.
- **Tecnologias**: Vue 3, Flask, Postman
- **Status**:
  - Backend: ✅ Concluído
  - Postman: ✅ Concluído
  - Frontend: ✅ Concluído com Vue CLI

---

## 🧪 Testes de Consulta SQL

> **Importante**: Altere o caminho dos arquivos de acordo com o seu sistema.

**Exemplos**:
```sql
LOAD DATA INFILE 'D:/seu-caminho/Relatorio_cadop.csv';

LOAD DATA INFILE 'D:\\seu-caminho\\anexos\\dados_ans\\1T2024\\1T2024.csv';
LOAD DATA INFILE 'D:\\seu-caminho\\anexos\\dados_ans\\2T2024\\2T2024.csv';
LOAD DATA INFILE 'D:\\seu-caminho\\anexos\\dados_ans\\3T2024\\3T2024.csv';
LOAD DATA INFILE 'D:\\seu-caminho\\anexos\\dados_ans\\4T2024\\4T2024.csv';
```

⚠️ **Observação importante:**
Se ao executar o `LOAD DATA INFILE` ocorrer erro de permissão, verifique se o MySQL está com o carregamento de arquivos habilitado. Caso necessário, comente ou remova a linha `secure-file-priv` no arquivo `my.ini` do MySQL (normalmente localizado em `C:\ProgramData\MySQL\MySQL Server X.X\my.ini`), reinicie o serviço do MySQL e tente novamente.

---

## 📦 Dependências Python

Instale com:
```bash
pip install -r requirements.txt
```

Ou manualmente:
```bash
pip install requests beautifulsoup4 pdfplumber pandas flask mysql-connector-python python-dotenv
```

---

## ▶️ Execução dos Módulos Python

### Rodar `1-web-scraping`
```powershell
python 1-web-scraping\scraping.py
```

### Rodar `2-transformacao-dados`
```powershell
python 2-transformacao-dados\transformacao_dados.py
```

### Rodar `3-banco-de-dados`
```powershell
python 3-banco-de-dados\banco_de_dados.py
```

### Rodar `4-api`
```powershell
python 4-api\backend\server.py
```

---

## 🌐 Execução do Frontend (Vue.js)

Se quiser rodar o frontend a partir do diretório pai (fora da pasta Vue):
```bash
cd 4-api/frontend
npm run serve
```

Ou de qualquer local:
```bash
npm --prefix ./4-api/frontend run serve
```

---

