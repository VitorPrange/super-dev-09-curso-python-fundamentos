from typing import Dict, List


def exercicio01():
    paciente: Dict[str, str|float|int|bool] = {}

    paciente["nome_paciente"] = "Amanda"
    paciente["idade"] = 28

    print("Paciente: ", paciente["nome_paciente"])
    print("Idade: ", paciente["idade"])


def exercicio02():
    aluno: Dict[str, str|int] = {}

    aluno["nome"] = "NomeAluno"
    aluno["idade"] = 18
    aluno["turma"] = "turma 1"
    aluno["curso"] = "curso b"

    for chave in aluno.keys():
        print(chave)



def exercicio03():
    produtos: Dict[str, str|float|int] = {}

    produtos["nome"] = "Peru"
    produtos["preco"] = 19991991919.03
    produtos["estoque"] = 987654321
    produtos["categoria"] = "Incategorizavel"

    for valor in produtos.values():
        print(valor)


def exercicio04():
    funcionario: Dict[str, float|str] = {}

    funcionario["nome"] = "seila"
    funcionario["cargo"] = "seila"
    funcionario["salario"] = 735873458735873587.2
    funcionario["setor"] = "pq tu e bote"

    for chave, valor in funcionario.items():
        print(chave)
        print(valor)


def exercicio05():
    titulo: str = input("Digite o titulo do livro: ")
    autor: str = input("Digite o nome do autor: ")
    ano_publicacao: str = input("Digite o ano de publicação: ")
    quantidade_paginas: int = int(input("Digite a quantidade de paginas: "))

    livro: Dict[str, int|str] = {}

    livro["titulo"] = titulo
    livro["autor"] = autor
    livro["ano_publicacao"] = ano_publicacao
    livro["quantidade_paginas"] = quantidade_paginas

    print("\nDados do livro: ")
    for chave, valor in livro.items():
        print(f"{chave}: {valor}")


def exercicio06():
    jogos: List[Dict[str, str|int]] = [
        {
            "nome_jogo": "Minecraft",
            "genero": "AMENTEJIKARA",
            "ano_lancamento": "2000",
            "preco": 0

        },
        {
            "nome_jogo": "craftmine",
            "genero": "AMENTEJIKARA",
            "ano_lancamento": "200-1",
            "preco": 1

        }
    ]

    for i in jogos:
        jogo = i.items()
        
        for chave, valor in jogo:
            if chave == "nome_jogo":
                chave = "Nome do jogo"
            elif chave == "ano_lancamento":
                chave = "Ano de lançamento"
            elif chave == "genero":
                chave = "Gênero"
            else:
                chave = "Preço"
            print(f"{chave}: {valor}")
        print("\n")
 

def exercicio07():
    produtos: List[Dict[str, float|int|str]] = [
        {
            "id": 1,
            "nome": "Notebook Gamer",
            "categoria": "Eletrônicos",
            "preco": 4599.90,
            "estoque": 12
        },
        {
            "id": 2,
            "nome": "Mouse sem Fio",
            "categoria": "Periféricos",
            "preco": 89.90,
            "estoque": 150
        },
        {
            "id": 3,
            "nome": "Cadeira Ergonômica",
            "categoria": "Móveis",
            "preco": 1299.00,
            "estoque": 8
        },
        {
            "id": 4,
            "nome": "Monitor 27 polegadas",
            "categoria": "Eletrônicos",
            "preco": 1899.50,
            "estoque": 20
        },
        {
            "id": 5,
            "nome": "Teclado Mecânico",
            "categoria": "Periféricos",
            "preco": 349.90,
            "estoque": 45
        }
    ]

    nomes = obter_nomes_produtos(produtos)
    print(f"Nomes dos produtos: {nomes}")

    nome_produtos_com_estoque_baixo = obter_produtos_com_estoque_baixo(produtos)
    print(f"Nomes dos produtos com estoque baixo: {nome_produtos_com_estoque_baixo}")

    categoria_pesquisada: str = input("Digite a categoria a ser pesquisada: ")

    nomes_produtos_por_categoria = obter_produtos_por_categoria(produtos, categoria_pesquisada)
    print(f"Nomes dos produtos filtrados pela categoria {categoria_pesquisada}: {nomes_produtos_por_categoria}")

    preco_min = float(input("Digite o preco minimo: "))

    nomes_produtos_por_preco_minimo = obter_produtos_acima_do_preco(produtos, preco_min)
    print(f"Nomes dos produtos filtrados pelo preco minimo {preco_min}: {nomes_produtos_por_preco_minimo}")

    soma_valor_total_estoque = somar_valor_total_estoque(produtos)
    print(f"Soma dos preços dos produtos: {soma_valor_total_estoque}")



def obter_nomes_produtos(produtos: List[Dict[str, float|int|str]]) -> List:

    nomes = []

    for i in produtos:
        produto = i["nome"]
        nomes.append(produto)
    return nomes


def obter_produtos_com_estoque_baixo(produtos: List[Dict[str, float|int|str]]) -> List:

    produtos_abaixo_estoque = []

    for produto in produtos:
        if produto["estoque"] < 10:
            produtos_abaixo_estoque.append(produto["nome"])
    return produtos_abaixo_estoque


def obter_produtos_por_categoria(produtos: List[Dict[str, float|int|str]], categoria_pesquisada: str):
    produtos_filtrados: List = []

    for produto in produtos:
        if produto["categoria"] == categoria_pesquisada:
            produtos_filtrados.append(produto["nome"])
    return produtos_filtrados
        


def obter_produtos_acima_do_preco(produtos: List[Dict[str, float|int|str]], preco_min: float):
    produtos_filtrados: List = []
    for produto in produtos:
        if produto["preco"] > preco_min:
            produtos_filtrados.append(produto["nome"])
    return produtos_filtrados


def somar_valor_total_estoque(produtos: List[Dict[str, float|int|str]]) -> float:
    soma = 0

    for produto in produtos:
        soma += (produto["preco"] * produto["estoque"])

    return soma




exercicio07()