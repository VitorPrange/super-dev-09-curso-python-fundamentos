from abc import ABC, abstractmethod

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

    