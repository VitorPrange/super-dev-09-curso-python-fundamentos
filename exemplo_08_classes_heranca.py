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

exemplo_funcionario()

    