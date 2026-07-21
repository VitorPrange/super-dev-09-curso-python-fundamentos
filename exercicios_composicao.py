class Autor():
    def __init__(self, nome: str, nacionalidade: str, ano_nascimento: int):
        self.nome = nome
        self.nacionalidade = nacionalidade
        self.ano_nascimento = ano_nascimento

    def apresentar_dados(self):
        print("\n-------------------------")
        print("Autor:")
        print(f"Nome: {self.nome}")
        print(f"Nacionalidade: {self.nacionalidade}")
        print(f"Ano de nascimento: {self.ano_nascimento}")

    def obter_descricao(self):
        return f"{self.nome} {self.nacionalidade}"
    

class Livro():
    def __init__(self, titulo: str, quantidade_paginas: int, ano_publicacao: int, autor: Autor):
        self.titulo = titulo
        self.quantidade_paginas = quantidade_paginas
        self.ano_publicacao = ano_publicacao
        self.autor = autor

    def apresentar_dados(self):
        print("\n-------------------------")
        print("Livro:")
        print(f"Título: {self.titulo}")
        print(f"Quantidade de páginas: {self.quantidade_paginas}")
        print(f"Ano de publicação: {self.ano_publicacao}")
        print(f"Autor: {self.autor.obter_descricao()}")


def exemplo_livro_autor():
    autor1 = Autor("George Orwell", "Britânico", 1903)
    livro1 = Livro("1984", 328, 1949, autor1)

    autor2 = Autor("J.K. Rowling", "Britânica", 1965)
    livro2 = Livro("Harry Potter e a Pedra Filosofal", 223, 1997, autor2)

    autor1.apresentar_dados()
    livro1.apresentar_dados()

    autor2.apresentar_dados()
    livro2.apresentar_dados()


class Endereco():
    def __init__(self, rua: str, numero: int, bairro: str, cidade: str, estado: str):
        self.rua = rua
        self.numero = numero
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado

    def apresentar_dados(self):
        print("\n-------------------------")
        print("Endereço:")
        print(f"Rua: {self.rua}")
        print(f"Número: {self.numero}")
        print(f"Bairro: {self.bairro}")
        print(f"Cidade: {self.cidade}")
        print(f"Estado: {self.estado}")

    def obter_endereco_completo(self):
        return f"{self.rua}, {self.numero} - {self.bairro}, {self.cidade} - {self.estado}"
    

class Pessoa():
    def __init__(self, nome: str, idade: int, telefone: str, endereco: Endereco):
        self.nome = nome
        self.idade = idade
        self.telefone = telefone
        self.endereco = endereco

    def apresentar_dados(self):
        print("\n-------------------------")
        print("Pessoa:")
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Telefone: {self.telefone}")
        print(f"Endereço: {self.endereco.obter_endereco_completo()}")

    def verificar_maioridade(self):
        if self.idade >= 18:
            print("Pessoa maior de idade")
        else:
            print("Pessoa menor de idade")


def exemplo_endereco_pessoa():
    endereco1 = Endereco("Rua A", 123, "Bairro X", "Cidade Y", "Estado Z")
    pessoa1 = Pessoa("João", 25, "123456789", endereco1)

    endereco2 = Endereco("Rua B", 456, "Bairro W", "Cidade V", "Estado U")
    pessoa2 = Pessoa("Maria", 15, "987654321", endereco2)

    endereco1.apresentar_dados()
    pessoa1.apresentar_dados()
    pessoa1.verificar_maioridade()

    endereco2.apresentar_dados()
    pessoa2.apresentar_dados()
    pessoa2.verificar_maioridade()


class Cliente():
    def __init__(self, nome: str, cpf: str, email:str):
        self.nome = nome
        self.cpf = cpf
        self.email = email

    def apresentar_dados(self):
        print("\n-------------------------")
        print("Cliente:")
        print(f"Nome: {self.nome}")
        print(f"CPF: {self.cpf}")
        print(f"E-mail: {self.email}")

    def obter_identificacao(self):
        return f"{self.nome} {self.cpf}"
    

class Pedido():
    def __init__(self, numero: int, produto: str, quantidade: int, valor_unitario:float, cliente: Cliente):
        self.numero = numero
        self.produto = produto
        self.quantidade = quantidade
        self.valor_unitario = valor_unitario
        self.cliente = cliente

    def apresentar_dados(self):
        print("\n-------------------------")
        print("Pedido:")
        print(f"Número: {self.numero}")
        print(f"Produto: {self.produto}")
        print(f"Quantidade: {self.quantidade}")
        print(f"Valor unitário: R${self.valor_unitario}")
        print(f"Cliente: {self.cliente.obter_identificacao()}")

    def calcular_total(self) -> float:
        return self.quantidade * self.valor_unitario

    def apresentar_total(self):
        total = self.calcular_total()
        print(f"Total do pedido: R${total:.2f}")


def exemplo_cliente_pedido():
    cliente1 = Cliente("João Silva", "123.456.789-00", "joao.silva@email.com")
    cliente2 = Cliente("Maria Souza", "987.654.321-00", "maria.souza@email.com")

    pedido1 = Pedido(1, "Notebook", 1, 3500.00, cliente1)
    pedido2 = Pedido(2, "Mouse", 3, 89.90, cliente2)

    cliente1.apresentar_dados()
    cliente2.apresentar_dados()

    pedido1.apresentar_dados()
    pedido2.apresentar_dados()

    pedido1.apresentar_total()
    pedido2.apresentar_total()


class Professor():
    def __init__(self, nome: str, espexialidade: str, tempo_experiencia: int):
        self.nome = nome
        self.especialidade = espexialidade
        self.tempo_experiencia = tempo_experiencia

    def apresentar_dados(self):
        print("\n-------------------------")
        print("Professor:")
        print(f"Nome: {self.nome}")
        print(f"Especialidade: {self.especialidade}")
        print(f"Tempo de experiência: {self.tempo_experiencia} anos")

    def obter_apresentacao(self):
        return f"{self.nome} {self.especialidade}"
    

class Curso():
    def __init__(self, nome: str, carga_horaria: int, quantidade_alunos: int, professor: Professor):
        self.nome = nome
        self.carga_horaria = carga_horaria
        self.quantidade_alunos = quantidade_alunos
        self.professor = professor

    def apresentar_dados(self):
        print("\n-------------------------")
        print("Curso:")
        print(f"Nome: {self.nome}")
        print(f"Carga Horaria: {self.carga_horaria}")
        print(f"Quantidade de alunos: {self.quantidade_alunos}")
        print(f"Professor: {self.professor.obter_apresentacao()}")

    def verificar_duracao(self):
        if self.carga_horaria < 40:
            print("Curso de curta duração")
        else:
            print("Curso de longa duração")


def exemplo_professor_curso():

    professor1 = Professor("Carlos Mendes", "Programação", 10)
    professor2 = Professor("Ana Ribeiro", "Banco de Dados", 5)

    curso1 = Curso("Python Avançado", 60, 25, professor1)
    curso2 = Curso("SQL Básico", 20, 30, professor2)

    professor1.apresentar_dados()
    professor2.apresentar_dados()

    curso1.apresentar_dados()
    curso2.apresentar_dados()

    curso1.verificar_duracao()
    curso2.verificar_duracao()

