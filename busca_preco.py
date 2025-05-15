import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook 
import unicodedata

# Função para remover acentos
def remover_acentos(texto):
    return ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn')

# Termo para buscar no mercado livre
produto = input('Digite o nome do produto que deseja buscar: ')
url = f'https://lista.mercadolivre.com.br/{produto}'

# Enviando requisição para o site
headers = {
    'User-Agent': 'Mozilla/5.0'
}
response = requests.get(url, headers=headers)

# Verificando se a página está respondendo normalmente
if response.status_code != 200:
    print('Erro ao acessar o site!')
    exit()

# Analisando o HTML da página
soup = BeautifulSoup(response.text, 'html.parser')

# Encontrando os itens da busca
itens = soup.select('div.ui-search-result__wrapper')
print(f"{len(itens)} produtos encontrados")

# Criando a planilha
wb = Workbook()
ws = wb.active
ws.title = 'Preços'
ws.append(['Nome', 'Preço', 'Link'])

# Extraindo informações dos itens
for item in itens:
    preco_inteiro_tag = item.find('span', class_='andes-money-amount__fraction')
    preco_centavos_tag = item.find('span', class_='andes-money-amount__cents')
    link_tag = item.find('a', href=True)

    if preco_inteiro_tag and link_tag:
        nome = nome = link_tag.text.strip()
        preco = preco_inteiro_tag.text.strip()
        if preco_centavos_tag:
            preco += ',' + preco_centavos_tag.text.strip() 
        link = link_tag['href']
        ws.append([nome, preco, link])

# Limpando nome do arquivo
nome_arquivo = remover_acentos(produto.strip().replace(' ', '_').lower())

# Salvando arquivo
wb.save(f'precos_{nome_arquivo}.xlsx')
print(f'Planilha precos_{nome_arquivo}.xlsx criada com sucesso!')