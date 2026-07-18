class Motor():
    def __init__(self, potencia, combustivel: str):
        self.potencia = potencia
        self.combustivel = combustivel


class Carro():
    def __init__(self, modelo: str, ano_lancamento: int, motor: Motor):
        self.modelo = modelo
        self.ano_lancamento = ano_lancamento
        self.motor = motor


def exemplo_carro():
    motor_golf_tsi = Motor(150, "Gasolina")
    golf_tsi = Carro("Fusca", 1970, motor_golf_tsi)

    print("\n-------------------------")
    print(f"Modelo: {golf_tsi.modelo}")
    print(f"Ano de lançamento: {golf_tsi.ano_lancamento}")
    print(f"Potência do motor: {golf_tsi.motor.potencia}")
    print(f"Combustível do motor: {golf_tsi.motor.combustivel}")


class Bateria():
    def __init__(self, capacidade: float):
        self.capacidade = capacidade
        self.carga = 100.0  # Carga inicial da bateria em porcentagem

    def utilizar(self, consumo: int):
       self.carga = self.carga - consumo

    def apresentar_dados(self):
        print("\n-------------------------")
        print("Bateria:")
        print(f"Capacidade: {self.capacidade} kWh")
        print(f"Carga atual: {self.carga} %")


class Armazenamento():
    def __init__(self, capacidade: int):
        self.capacidade = capacidade

    def apresentar_dados(self):
        print("\n-------------------------")
        print("Armazenamento:")
        print(f"Capacidade: {self.capacidade}GB")


class Celular():
    def __init__(self, modelo: str, preco: float, cor: str, bateria: Bateria, armazenamento: Armazenamento):
        self.modelo = modelo
        self.preco = preco
        self.cor = cor
        self.bateria = bateria
        self.armazenamento = armazenamento

    def navegar_youtube(self, consumo: int):
        print("Navegando no youtube")
        descarregamento_por_minuto = 2
        nivel_consumo = consumo * descarregamento_por_minuto
        self.bateria.utilizar(nivel_consumo)

    def apresentar_dados(self):
        print("\n-------------------------")
        print(f"Modelo: {self.modelo}")
        print(f"Preço: R${self.preco}")
        print(f"Cor: {self.cor}")
        self.bateria.apresentar_dados()
        self.armazenamento.apresentar_dados()


def exemplo_celular():
    bateria_iphone = Bateria(capacidade=3349.0)
    armazenamento_iphone = Armazenamento(128)
    iphone = Celular("iPhone 13", 5000.0, "Preto", bateria_iphone, armazenamento_iphone)

    iphone.apresentar_dados()
    iphone.navegar_youtube(10)
    iphone.apresentar_dados()