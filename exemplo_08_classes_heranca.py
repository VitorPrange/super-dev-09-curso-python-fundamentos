class Pessoa():
    def __init__(self, nome: str, sobrenome: str):
        self.nome = nome
        self.sobrenome = sobrenome

    def gerar_nome_completo(self):
        return f"{self.nome} {self.sobrenome}"
    

class Funcionario(Pessoa):
    def __init__(self, nome: str, sobrenome: str, cargo: str):
        super().__init__(nome, sobrenome)
        self.cargo = cargo
    

def exemplo_funcionario():
    pessoa = Pessoa("Ronaldo", " Femomemo")
    print(f"Nome completo: {pessoa.gerar_nome_completo()}")

    funcionario = Funcionario("Lionel", "Messi")
    print(f"Nome completo do funcionario: {funcionario.gerar_nome_completo()}")


class Pessoa2():
    def __init__(self, nome: str, telefone: str, email: str):
        self.nome = nome
        self.telefone = telefone
        self.email = email

    def apresentar_dados(self):
        print("\n--------------------------------")
        print(f"Nome: {self.nome}")
        print(f"Telefone: {self.telefone}")
        print(f"E-mail: {self.email}")
    

class Aluno(Pessoa2):
    def __init__(self, nome, telefone, email, nota1: float, nota2: float, nota3: float):
        super().__init__(nome, telefone, email)
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3

    def apresentar_dados(self):
        super().apresentar_dados()
        print(f"Nota 1: {self.nota1}")
        print(f"Nota 2: {self.nota2}")
        print(f"Nota 3: {self.nota3}")

    def apresentar_media(self):
        media: float = (self.nota1 + self.nota2 + self.nota3) / 3

        print(f"Média: {media}")


class Professor(Pessoa2):
    def __init__(self, nome, telefone, email, salario: float):
        super().__init__(nome, telefone, email)
        self.salario = salario

    def apresentar_dados(self):
        super().apresentar_dados()
        print(f"Salário: {self.salario}")


def exemplo_aluno_professor():
    aluno1 = Aluno("Aluno1", "Telefone", "Email", 10, 9, 8)
    aluno2 = Aluno("Aluno2", "Telefone2", "Email2", 7, 6, 5)

    aluno1.apresentar_dados()
    aluno1.apresentar_media()

    aluno2.apresentar_dados()
    aluno2.apresentar_media()

    professor1 = Professor("Professor1", "TelefoneProfessor1", "EmailProfessor1", 1200)
    professor2 = Professor("Professor2", "TelefoneProfessor2", "EmailProfessor2", 999999999999)

    professor1.apresentar_dados()
    professor2.apresentar_dados()


class Carro():
    def __init__(self, marca: str, modelo: str, ano: str, quantidade_rodas: int):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.quantidade_rodas = quantidade_rodas

    def apresentar_dados(self):
        print("-"*20)
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.ano}")
        print(f"Quantidade de rodas: {self.quantidade_rodas}")

    def ligar(self):
        print("VROOOOOOOOOO VROOOOooooooooooooOOOOooooooOOooooOopkójihwargbknzkmslf,sa.d")
    


class CarroLuxo(Carro):
    def __init__(self, marca: str, modelo: str, ano: str, quantidade_rodas: int, quantidade_porta: int):
        super().__init__(marca, modelo, ano, quantidade_rodas)
        self.quantidade_porta = quantidade_porta

    def apresentar_dados(self):
        super().apresentar_dados()
        print(f"Quantidade de portas: {self.quantidade_porta}")


class CarroLuxoEsportivo(CarroLuxo):
    def __init__(self, marca, modelo, ano, quantidade_rodas, quantidade_porta, cilindradas):
        super().__init__(marca, modelo, ano, quantidade_rodas, quantidade_porta)
        self.cilindradas = cilindradas

    def apresentar_dados(self):
        super().apresentar_dados()
        print(f"Cilidradas: {self.cilindradas}")

exemplo_aluno_professor()
    