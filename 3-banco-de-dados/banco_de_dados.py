import os
import requests
import zipfile
from bs4 import BeautifulSoup

# Caminho do script atual
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# Caminho da pasta-mãe (intuitivecare)
PARENT_DIR = os.path.dirname(SCRIPT_DIR)

# Diretórios de destino
ANEXOS_DIR = os.path.join(PARENT_DIR, "anexos")
DATA_DIR = os.path.join(ANEXOS_DIR, "dados_ans")

# URLs dos arquivos
ZIP_URLS = [
    "https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/2023/",
    "https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/2024/",
]
CSV_URL = "https://dadosabertos.ans.gov.br/FTP/PDA/operadoras_de_plano_de_saude_ativas/"

# Verifica se já foi feito
if os.path.exists(DATA_DIR):
    print('Pasta dados_ans já existe')
    exit()
else:
    os.makedirs(DATA_DIR, exist_ok=True)

def get_files_from_page(url, extensions=(".zip", ".csv")):
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Erro ao acessar {url}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    file_links = [url + a["href"] for a in soup.find_all("a", href=True) if a["href"].endswith(extensions)]
    return file_links

def download_file(url, save_path):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(save_path, "wb") as file:
            for chunk in response.iter_content(chunk_size=1024):
                file.write(chunk)
        print(f"Arquivo baixado: {save_path}")
    else:
        print(f"Erro ao baixar {url}")

def extract_zip(zip_path, extract_to):
    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(extract_to)
    print(f"Extraído: {zip_path} → {extract_to}")
    os.remove(zip_path)

def main():
    for base_url in ZIP_URLS:
        zip_files = get_files_from_page(base_url, extensions=(".zip",))
        for zip_url in zip_files:
            zip_name = os.path.basename(zip_url)
            zip_path = os.path.join(DATA_DIR, zip_name)
            
            if not os.path.exists(zip_path):
                download_file(zip_url, zip_path)
            
            extracted_folder = os.path.join(DATA_DIR, zip_name.replace(".zip", ""))
            if not os.path.exists(extracted_folder):
                os.makedirs(extracted_folder, exist_ok=True)
                extract_zip(zip_path, extracted_folder)

    csv_files = get_files_from_page(CSV_URL, extensions=(".csv",))
    for csv_url in csv_files:
        csv_name = os.path.basename(csv_url)
        csv_path = os.path.join(DATA_DIR, csv_name)
        if not os.path.exists(csv_path):
            download_file(csv_url, csv_path)

main()
