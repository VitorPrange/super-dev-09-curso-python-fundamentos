class Cachorro:
    def __init__(self, apelido: str, raca: str, cor: str, peso: float, idade: int):
        self.nome = apelido
        self.raca = raca
        self.cor = cor
        self.peso = peso
        self.idade = idade

    def apresentar_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Raça: {self.raca}")
        print(f"Cor: {self.cor}")
        print(f"Peso: {self.peso}")
        print(f"Idade: {self.idade}", end="\n\n\n")

    def fazer_aniversario(self):
        self.idade += 1
        print(f"{self.nome} fez aniversário e agora tem {self.idade} anos.")


tobi = Cachorro("Tobi", "Labrador", "Amarelo", 30.0, 5)
thor = Cachorro(apelido="Thor", raca="Pastor alemão", cor="Cinza e Branco", peso=25.0, idade=3)
mogli = Cachorro("Mogli", "Vira-lata", "Caramelo", 15.0, 2)

tobi.apresentar_dados()

thor.apresentar_dados()
thor.fazer_aniversario()

mogli.apresentar_dados()