import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# URL da página que contém as imagens
url = 'https://didatica.tech/tutorial-de-beautiful-soup-para-iniciantes-aprenda-agora/#:~:text=Abra%20o%20terminal%20ou%20linha,XML%20que%20você%20deseja%20raspar.'

# Pasta para armazenar o HTML e as imagens
output_folder = 'output'
html_file_path = os.path.join(output_folder, 'pagina.html')
images_folder = os.path.join(output_folder, 'imagens')

# Criar pastas para armazenar o HTML e as imagens
os.makedirs(images_folder, exist_ok=True)
os.makedirs(output_folder, exist_ok=True)

# Obter o conteúdo da URL
response = requests.get(url)

# Verificar se a requisição foi bem-sucedida
if response.status_code == 200:
    # Salvar o HTML em um arquivo
    with open(html_file_path, 'w', encoding='utf-8') as file:
        file.write(response.text)
    print(f'HTML salvo em {html_file_path}')

    # Analisar o conteúdo com Beautiful Soup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Encontrar todas as imagens
    for img_tag in soup.find_all('img'):
        # Obter o URL da imagem
        img_url = img_tag.get('src')
        if not img_url:
            continue

        # Construir o URL completo da imagem
        img_url = urljoin(url, img_url)

        # Obter o nome da imagem a partir da URL
        img_name = os.path.basename(img_url)

        # Caminho onde a imagem será salva
        img_path = os.path.join(images_folder, img_name)

        # Baixar e salvar a imagem
        try:
            img_response = requests.get(img_url)
            if img_response.status_code == 200:
                with open(img_path, 'wb') as file:
                    file.write(img_response.content)
                print(f'Imagem salva em {img_path}')
            else:
                print(f'Falha ao baixar a imagem {img_url}. Status code: {img_response.status_code}')
        except Exception as e:
            print(f'Erro ao baixar a imagem {img_url}: {e}')
else:
    print(f'Falha ao acessar a URL. Status code: {response.status_code}')
