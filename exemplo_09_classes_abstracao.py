from abc import ABC, abstractmethod
from math import pi

class Animal(ABC):
    def __init__(self, raca: str, idade: int):
        super().__init__()
        self.raca = raca
        self.idade = idade

    @abstractmethod
    def fazer_algazarra(self):
        pass

    
class Cachorro(Animal):
    def __init__(self, raca, idade, cor):
        super().__init__(raca, idade)
        self.cor = cor


    def fazer_algazarra(self):
        print("Algazarreando")


class FormaGeometrica(ABC):
    @abstractmethod
    def calcular_area(self) -> float:
        pass


class Circulo(FormaGeometrica):
    def __init__(self, raio: float):
        self.raio = raio

    def calcular_area(self) -> float:
        area = pi * self.raio ** 2
        return area
    
class Quadrado(FormaGeometrica):
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self) -> float:
        return self.lado * self.lado
        

circulo = Circulo(5)

quadrado = Quadrado(4)

print(f"Area circulo: {circulo.calcular_area()}")

print(f"Area quadrado: {quadrado.calcular_area()}")
            