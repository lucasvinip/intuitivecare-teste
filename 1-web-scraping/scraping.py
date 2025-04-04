import os
import requests
from bs4 import BeautifulSoup
import time
import zipfile

# URL do site da ANS com os anexos
URL = 'https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos'

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
}

NECESSARY_FILES = ['Anexo_I', 'Anexo_II']

# Caminho da pasta do script atual
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# Caminho da pasta-mãe (um nível acima do script)
PARENT_DIR = os.path.dirname(SCRIPT_DIR)

# Diretório onde serão salvos os anexos
ANEXOS_DIR = os.path.join(PARENT_DIR, 'anexos')
ZIP_FILE = os.path.join(ANEXOS_DIR, 'anexos_compactados.zip')

def get_pdf_urls():
    response = requests.get(URL, headers=HEADERS)
    if response.status_code != 200:
        print('Falha ao acessar o site')
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    pdf_links = soup.find_all('a', href=True)
    pdf_urls = []

    for link in pdf_links:
        href = link['href']
        if href.endswith('.pdf') and any(file in href for file in NECESSARY_FILES):
            if href.startswith('/'):
                href = 'https://www.gov.br' + href
            pdf_urls.append(href)

    return pdf_urls

def download_pdfs():
    pdf_urls = get_pdf_urls()

    if not pdf_urls:
        print('Nenhum PDF encontrado para download.')
        return None

    if not os.path.exists(ANEXOS_DIR):
        os.makedirs(ANEXOS_DIR)

    zip_temp = zipfile.ZipFile(ZIP_FILE, 'w', zipfile.ZIP_DEFLATED)

    for pdf_url in pdf_urls:
        pdf_name = pdf_url.split('/')[-1]
        try:
            pdf_response = requests.get(pdf_url, headers=HEADERS, timeout=10)
            pdf_response.raise_for_status()

            zip_temp.writestr(pdf_name, pdf_response.content)
            print(f'Download e compactação concluídos: {pdf_name}')
        except requests.RequestException as e:
            print(f'Erro ao baixar {pdf_url}: {e}')

        time.sleep(1)

    zip_temp.close()
    return ZIP_FILE

def main():
    if os.path.exists(ZIP_FILE):
        print('Os arquivos já estão compactados.')
    else:
        zip_path = download_pdfs()
        if zip_path:
            print(f'Arquivos compactados em {zip_path}')
        else:
            print('Nenhum arquivo foi baixado e compactado.')

if __name__ == '__main__':
    main()
