import os
import requests
from bs4 import BeautifulSoup
import time
import zipfile
import shutil

URL = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
}
ANEXOS_DIR = 'anexos'
ZIP_FILE = os.path.join(ANEXOS_DIR,'anexos_compactados.zip')
NECESSARY_FILES = ['Anexo_I', 'Anexo_II']

def get_pdf_urls():
    response = requests.get(URL)
    if response.status_code != 200:
        print('Falha ao acessar o site')
        return []
    
    soup = BeautifulSoup(response.text, 'html.parser')
    pdf_links = soup.find_all('a', href = True)
    pdf_urls = [link['href'] for link in pdf_links if link['href'].endswith('.pdf')]

    return [url for url in pdf_urls if any(file in url for file in NECESSARY_FILES)]

def download_pdfs():
    pdf_urls = get_pdf_urls()
    
    if not pdf_urls:
        print('Nenhum PDF encontrado para download.')
        return None

    if not os.path.exists(ANEXOS_DIR):
        os.makedirs(ANEXOS_DIR)
    
    download_files = []
    for pdf_url in pdf_urls:
        pdf_name = os.path.join(ANEXOS_DIR, pdf_url.split('/')[-1])

        if os.path.exists(pdf_name):
            print(f'Já existe este arquivo: {pdf_name}')
            continue

        try:
            pdf_response = requests.get(pdf_url, headers=HEADERS, timeout=10)
            pdf_response.raise_for_status()

            with open(pdf_name, 'wb') as f:
                f.write(pdf_response.content)
            
            download_files.append(pdf_name)
            print(f'Download concluído: {pdf_name}')
        except requests.RequestException as e:
            print(f'Erro ao baixar {pdf_url}: {e}')
        
        time.sleep(1)
    
    if os.path.exists(pdf_name):
        return 'anexos'
    else:
        None

def turn_zip_file():
    downloaded_files = download_pdfs()

    if not downloaded_files:
        print('Nenhum arquivo baixado, compactação não realizada.')
        return
    if os.path.exists(ZIP_FILE):
        print('Os arquivos já estão compactados')
    else:
        with zipfile.ZipFile(ZIP_FILE, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, _, files in os.walk(ANEXOS_DIR):
                for file in files:
                    file_path = os.path.join(root, file)
                    if file_path != ZIP_FILE:
                        zipf.write(file_path, os.path.relpath(file_path, ANEXOS_DIR))           
        print(f'Arquivos compactados em {ZIP_FILE}')

turn_zip_file()
