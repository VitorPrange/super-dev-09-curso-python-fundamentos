import questionary
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


def cadastrar_empresa():
    nome: str = questionary.text("Digite o nome da empresa: ").ask()
    cnpj: str = questionary.text("Digite o CNPJ da empresa: ").ask()

    url = f"{url_base}/api/v1/empresa"

    dados = {
        "nome": nome,
        "cnpj": cnpj
    }

    resposta = requests.post(url, json=dados)

    print(f"Status code: {resposta.status_code}")


def cadastrar_produto():
    nome: str = questionary.text("Digite o nome do produto: ").ask()
    preco: float = float(questionary.text("Digite o preço do produto: ").ask())
    categoria: str = questionary.text("Digite a categoria do produto: ").ask()

    url = f"{url_base}/api/v1/empresa/produtos"

    dados = {
        "nome": nome,
        "preco": preco,
        "categoria": categoria
    }

    resposta = requests.post(url, json=dados)

    print(f"Status code: {resposta.status_code}")


def editar_empresa():
    id: int = int(questionary.text("Digite o id da empresa a ser editada: ").ask())
    nome: str = questionary.text("Digite o novo nome da empresa: ").ask()
    cnpj: str = questionary.text("Digite o novo CNPJ da empresa: ").ask()

    url = f"{url_base}/api/v1/empresa/{id}"

    dados = {
        "nome": nome,
        "cnpj": cnpj
    }

    resposta = requests.put(url, json=dados)

    print(f"Status code: {resposta.status_code}")


def editar_produto():
    id: int = int(questionary.text("Digite o id do produto a ser editado: ").ask())
    nome: str = questionary.text("Digite o novo nome do produto: ").ask()
    preco: float = float(questionary.text("Digite o novo preço do produto: ").ask())
    categoria: str = questionary.text("Digite a nova categoria do produto: ").ask()

    url = f"{url_base}/api/v1/empresa/produtos/{id}"

    dados = {
        "nome": nome,
        "preco": preco,
        "categoria": categoria
    }

    resposta = requests.put(url, json=dados)

    print(f"Status code: {resposta.status_code}")


def apagar_empresa():
    id: int = int(questionary.text("Digite o id da empresa a ser apagada: ").ask())

    url = f"{url_base}/api/v1/empresa/{id}"

    resposta = requests.delete(url)

    print(f"Status code: {resposta.status_code}")


def apagar_produto():
    id: int = int(questionary.text("Digite o id do produto a ser apagado: ").ask())

    url = f"{url_base}/api/v1/empresa/produtos/{id}"

    resposta = requests.delete(url)

    print(f"Status code: {resposta.status_code}")


def limpar_terminal():
    import os
    os.system('cls')


def crud_completo_empresa():
    escolha = questionary.select(
        "Escolha uma opção:",
        choices=[
            "Consultar todas as empresas",
            "Consultar empresa por ID",
            "Cadastrar empresa",
            "Editar empresa",
            "Apagar empresa",
            "Sair"
        ]
    ).ask()
    while escolha != "Sair":
        if escolha == "Consultar todas as empresas":
            consultar_empresas()
        elif escolha == "Consultar empresa por ID":
            consultar_empresa_por_id()
        elif escolha == "Cadastrar empresa":
            cadastrar_empresa()
        elif escolha == "Editar empresa":
            editar_empresa()
        elif escolha == "Apagar empresa":
            apagar_empresa()

        questionary.press_any_key_to_continue("Pressione qualquer tecla para continuar...").ask()

        limpar_terminal()

        escolha = questionary.select(
            "Escolha uma opção:",
            choices=[
                "Consultar todas as empresas",
                "Consultar empresa por ID",
                "Cadastrar empresa",
                "Editar empresa",
                "Apagar empresa",
                "Sair"
            ]
        ).ask()


def crud_completo_produto():
    escolha = questionary.select(
        "Escolha uma opção:",
        choices=[
            "Consultar todos os produtos",
            "Consultar produto por ID",
            "Cadastrar produto",
            "Editar produto",
            "Apagar produto",
            "Sair"
        ]
    ).ask()
    while escolha != "Sair":
        if escolha == "Consultar todos os produtos":
            consultar_produtos()
        elif escolha == "Consultar produto por ID":
            consultar_produto_por_id()
        elif escolha == "Cadastrar produto":
            cadastrar_produto()
        elif escolha == "Editar produto":
            editar_produto()
        elif escolha == "Apagar produto":
            apagar_produto()

        questionary.press_any_key_to_continue("Pressione qualquer tecla para continuar...").ask()

        limpar_terminal()

        escolha = questionary.select(
            "Escolha uma opção:",
            choices=[
                "Consultar todos os produtos",
                "Consultar produto por ID",
                "Cadastrar produto",
                "Editar produto",
                "Apagar produto",
                "Sair"
            ]
        ).ask()


def menu():
    escolha = questionary.select(
        "Escolha uma opção:",
        choices=[
            "CRUD completo de empresas",
            "CRUD completo de produtos",
            "Sair"
        ]
    ).ask()

    while escolha != "Sair":
        if escolha == "CRUD completo de empresas":
            crud_completo_empresa()
        elif escolha == "CRUD completo de produtos":
            crud_completo_produto()

        limpar_terminal()

        escolha = questionary.select(
            "Escolha uma opção:",
            choices=[
                "CRUD completo de empresas",
                "CRUD completo de produtos",
                "Sair"
            ]
        ).ask()



menu()