from rich.console import Console
from rich.table import Table



import requests


url_base = "https://api.franciscosensaulas.com"


def consultar_empresas():
    url = f"{url_base}/api/v1/empresa"

    resposta = requests.get(url)

    console = Console()

    table = Table(header_style="bold red", show_header=True, show_lines=True)
    table.add_column("ID")
    table.add_column("Nome")
    table.add_column("CNPJ")

    empresas = resposta.json()

    for empresa in empresas:
        table.add_row(str(empresa["id"]), empresa["nome"], empresa["cnpj"])

    console.print(table)

    print(f"Status code: {resposta.status_code}")


def consultar_empresa_por_id():
    id = int(input("Digite id da epresa a ser buscada: "))
    url = f"{url_base}/api/v1/empresa/{id}"

    resposta = requests.get(url)

    console = Console()

    empresa = resposta.json()

    table = Table(header_style="bold red", show_header=True, show_lines=True)
    table.add_column("ID")
    table.add_column("Nome")
    table.add_column("CNPJ")

    table.add_row(str(empresa["id"]), empresa["nome"], empresa["cnpj"])

    print(f"Status code: {resposta.status_code}")

    console.print(table)


def consultar_produtos():
    url = f"{url_base}/api/v1/empresa/produtos"

    resposta = requests.get(url)

    console = Console()

    table = Table(show_header=True, header_style="bold red", show_lines=True)
    table.add_column("ID")
    table.add_column("Nome")
    table.add_column("Preço")
    table.add_column("Categoria")

    produtos = resposta.json()

    for produto in produtos:
        table.add_row(str(produto["id"]), produto["nome"], str(produto["preco"]), produto["categoria"])
    
    print(f"Status code: {resposta.status_code}")

    console.print(table)


def consultar_produto_por_id():
    id = int(input("Digite id do produto a ser buscado: "))
    url = f"{url_base}/api/v1/empresa/produtos/{id}"

    resposta =  requests.get(url)

    if resposta.status_code == 404:
        print("Produto não encontrado")

    console =  Console()

    table = Table(show_header=True, header_style="bold red", show_lines=True)

    produto = resposta.json()

    table.add_column("ID")
    table.add_column("Nome")
    table.add_column("Preco")
    table.add_column("Categoria")

    table.add_row(str(produto["id"]), produto["nome"], str(produto["preco"]), produto["categoria"])

    console.print(table)

    print(f"Status code: {resposta.status_code}")



consultar_produto_por_id()