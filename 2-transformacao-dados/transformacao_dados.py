import os
import pandas as pd
import zipfile
import pdfplumber

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

PARENT_DIR = os.path.dirname(SCRIPT_DIR)

ANEXOS_DIR = os.path.join(PARENT_DIR, 'anexos')
CSV_FILENAME = 'tabela_anexo_I_extraida.csv'
CSV_PATH = os.path.join(ANEXOS_DIR, CSV_FILENAME)
ZIP_FILENAME = os.path.join(ANEXOS_DIR, 'Teste_Lucas_Vinicius.zip')
ZIP_ANEXO = os.path.join(ANEXOS_DIR, 'anexos_compactados.zip')

ABREVIACOES = {
    "OD": "Seg. Odontológica",
    "AMB": "Seg. Ambulatorial"
}

if os.path.exists(ZIP_FILENAME):
    print('A tabela já existe')
    exit()

def extract_pdf_from_zip():
    if not os.path.exists(ZIP_ANEXO):
        print('Primeiro executar o projeto scraping.py')
        return None
    
    with zipfile.ZipFile(ZIP_ANEXO, 'r') as zip_ref:
        for file in zip_ref.namelist():
            if 'Anexo_I' in file and file.endswith('.pdf'):
                extracted_path = os.path.join(ANEXOS_DIR, file)
                zip_ref.extract(file, ANEXOS_DIR)
                print(f'PDF extraído: {extracted_path}')
                return extracted_path
    
    print('Anexo I não encontrado no ZIP.')
    return None

def extract_table_from_pdf(pdf_file):
    data = []
    
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            table = page.extract_table()
            if table:
                for row in table:
                    if any(row):
                        data.append(row)
    
    return data

def replace_abbreviations(data_frame):
    return data_frame.replace(ABREVIACOES)

def save_to_csv(data, output_file):
    if not data:
        print('Nenhuma tabela foi extraída, o CSV não será salvo.')
        return None
    
    data_frame = pd.DataFrame(data)
    data_frame = replace_abbreviations(data_frame)
    data_frame.to_csv(output_file, index=False, encoding='utf-8-sig')
    print(f'Dados salvos em: {output_file}')
    
    return output_file

def compress_csv(csv_file, zip_file):
    if not os.path.exists(csv_file):
        print(f'O arquivo {csv_file} não foi encontrado')
        return
    
    with zipfile.ZipFile(zip_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(csv_file, os.path.basename(csv_file))
    
    print(f'Arquivo compactado como {zip_file}')
    os.remove(csv_file)
    print(f'Arquivo {csv_file} removido após a compactação.')

pdf_path = extract_pdf_from_zip()

if pdf_path:
    extracted_data = extract_table_from_pdf(pdf_path)
    
    if extracted_data:
        csv_file = save_to_csv(extracted_data, CSV_PATH)
        if csv_file:
            compress_csv(csv_file, ZIP_FILENAME)
            os.remove(pdf_path)
    else:
        print('Nenhuma tabela encontrada no PDF')
