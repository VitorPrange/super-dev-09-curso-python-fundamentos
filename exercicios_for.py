def exercicio01():
    for i in range(0, 5):
        print("Bem vindo!")


def exercicio02():
    for i in range(15, 31):
        print(i)


def exercicio03():
    numero = int(input("Digite o numero: "))

    for i in range(1,11):
        print(f"{i} X {numero} = {i * numero}")


def exercicio04():
    soma = 0
    for i in range(0, 5):
        numero = int(input("Digite o numero: "))
        soma = soma + numero
    print(soma)

exercicio04()