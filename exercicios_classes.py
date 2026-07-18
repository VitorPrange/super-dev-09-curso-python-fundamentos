class Aluno():
    def __init__(self, nome: str, nota1: float, nota2: float):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2

    def apresentar_dados(self):
        print("\n------------------------------------------")
        print(f"Nome: {self.nome}")
        print(f"Nota 1: {self.nota1}")
        print(f"Nota 2: {self.nota2}")
        

    def calcular_media(self):
        media: float = (self.nota1 + self.nota2) / 2
        print(f"Média: {media}")

    def apresentar_situacao(self):
        media: float = (self.nota1 + self.nota2) / 2
        if media < 7:
            print("Reprovado")
        else:
            print("Aprovado")


def exemplo_aluno():
    aluno1 = Aluno("Aluno1", 9.8, 7.7)
    aluno2 = Aluno("Aluno2", 8.8, 5.7)
    aluno3 = Aluno("Aluno3", 9.2, 6.7)

    aluno1.apresentar_dados()
    aluno1.calcular_media()
    aluno1.apresentar_situacao()

    
    aluno2.apresentar_dados()
    aluno2.calcular_media()
    aluno2.apresentar_situacao()

    
    aluno3.apresentar_dados()
    aluno3.calcular_media()
    aluno3.apresentar_situacao()


class Triangulo():
    def __init__(self, base: float, altura: float, lado1: float, lado2: float, lado3: float):
        self.base = base
        self.altura = altura
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def apresentar_dados(self):
        print("\n--------------------------------")
        print(f"Base: {self.base}")
        print(f"Altura: {self.altura}")
        print(f"Lado 1: {self.lado1}")
        print(f"Lado 2: {self.lado2}")
        print(f"Lado 3: {self.lado3}")

    def calcular_area(self):
        area: float = ((self.base * self.altura) / 2)
        print(f"Area: {area}")

    def verificar_equilatero(self):
        if self.lado1 == self.lado2 and self.lado2 == self.lado3:
            print("Equilatero")


def exemplo_triangulo():
    triangulo1 = Triangulo(10, 10, 9, 9 ,9)
    triangulo2 = Triangulo(16, 19, 15, 16 ,19)

    triangulo1.apresentar_dados()
    triangulo1.calcular_area()
    triangulo1.verificar_equilatero()


    triangulo2.apresentar_dados()
    triangulo2.calcular_area()
    triangulo2.verificar_equilatero()


class Quadrado():
    def __init__(self, lado: float):
        self.lado = lado
    
    def apresentar_dados(self):
        print("\n------------------------------")
        print(f"Lado: {self.lado}")

    def calcular_area(self):
        area: float = self.lado * self.lado
        print(f"Area: {area}")

    def calcular_perimetro(self):
        perimetro:float = self.lado * 4
        print(f"Perimetro: {perimetro}")


def exemplo_quadrado():
    quadrado1 = Quadrado(19)
    quadrado2 = Quadrado(29)

    quadrado1.apresentar_dados()
    quadrado1.calcular_area()
    quadrado1.calcular_perimetro()


    quadrado2.apresentar_dados()
    quadrado2.calcular_area()
    quadrado2.calcular_perimetro()


class Retangulo():  
    def __init__(self, base: float, altura: float):
        self.base = base
        self.altura = altura
    
    def apresentar_dados(self):
        print("\n-----------------------------")
        print(f"Base: {self.base}")
        print(f"Altura: {self.altura}")

    def calcular_area(self):
        area: float = self.base * self.altura
        print(f"Area: {area}")

    def calcular_perimetro(self):
        perimetro: float = 2 * (self.base + self.altura)
        print(f"Perimetro: {perimetro}")


def exemplo_retangulo():
    retangulo1 = Retangulo(10, 15)
    retangulo2 = Retangulo(15, 25)

    retangulo1.apresentar_dados()
    retangulo1.calcular_area()
    retangulo1.calcular_perimetro()

    retangulo2.apresentar_dados()
    retangulo2.calcular_area()
    retangulo2.calcular_perimetro()


class Circulo():
    def __init__(self, raio: float):
        self.raio = raio

    def apresentar_dados(self):
        print("\n-------------------------")
        print(f"Raio: {self.raio}")

    def calcular_area(self):
        area = 3.14 * (self.raio * self.raio)
        print(f"Area: {area}")

    def calcular_circunferencia(self):
        circunferencia: float = 2 * 3.14 * self.raio
        print(f"Circunferencia: {circunferencia}")


def exemplo_circulo():
    circulo1 = Circulo(5)
    circulo1.apresentar_dados()
    circulo1.calcular_area()
    circulo1.calcular_circunferencia()

    circulo2 = Circulo(8)
    circulo2.apresentar_dados()
    circulo2.calcular_area()
    circulo2.calcular_circunferencia()


class Personagem():
    def __init__(self, nome: str, vida: float, ataque: float):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque

    def apresentar_dados(self):
        print("\n-------------------------")
        print(f"Nome: {self.nome}")
        print(f"Vida: {self.vida}")
        print(f"Ataque: {self.ataque}")

    def atacar(self, outro_personagem):
        outro_personagem.vida = outro_personagem.vida - self.ataque
        print(f"\n{self.nome} atacou {outro_personagem.nome} causando {self.ataque} de dano.\nVida atual de {outro_personagem.nome}: {outro_personagem.vida}")


def exemplo_personagem():
    personagem1 = Personagem("Guerreiro", 100, 15)
    personagem2 = Personagem("Mago", 80, 25)

    personagem1.apresentar_dados()
    personagem2.apresentar_dados()

    personagem1.atacar(personagem2)
    personagem2.atacar(personagem1)
    
exemplo_personagem()













class Retangulo():
    pass
class Circulo():
    pass

