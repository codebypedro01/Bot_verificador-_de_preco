# Bot Verificador de Preço

Este projeto é um bot simples em Python que busca preços de produtos no Mercado Livre e salva os dados em uma planilha Excel.

## Funcionalidades

- Pesquisa o nome do produto no Mercado Livre.
- Extrai nome, preço e link dos primeiros resultados.
- Salva os dados em uma planilha Excel (.xlsx).
- Remove acentuação do nome do arquivo para evitar problemas no sistema de arquivos.

## Tecnologias usadas

- Python 3
- Requests
- BeautifulSoup
- Openpyxl
- Unicodedata (para remover acentos)

## Como usar

1. Clone o repositório:

```bash
git clone https://github.com/codebypedro01/Bot_verificador-_de_preco.git
```
2. Instale as dependências:
```bash
pip install requests beautifulsoup4 openpyxl
```

3. Execute o script:

```bash
python busca_preco.py
```
4. Quando solicitado, digite o nome do produto que deseja buscar.

5. O arquivo Excel com os resultados será salvo com o nome precos_<produto>.xlsx.