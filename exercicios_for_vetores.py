def exercicio09():
    nomes = []
    nomes.append("Vitor")
    nomes.append("Vitor2")
    nomes.append("Vitor3")
    nomes.append("Vitor4")
    nomes.append("Vitor5")

    for i in range(0, len(nomes)):
        print(nomes[i])


def exercicio10():
    frutas = []

    for i in range(0, 5):
        fruta = input("Digite a fruta: ")
        frutas.append(fruta)

    for i in range(len(frutas)):
        print(frutas[i])
    


def exercicio11():
    numeros = []
    soma = 0
    for i in range(0, 5):
        numero = int(input("Digite o numero: "))
        numeros.append(numero)

    for i in range(len(numeros)):
        soma = soma + numeros[i]


def exercicio12():
    numeros = []
    contador = 0

    for i in range(0, 6):
        numero = int(input("Digite o numero: "))
        numeros.append(numero)
    for i in range(len(numeros)):
        if numeros[i] % 2:
            contador += 1
    print(contador)


def exercicio13():
    notas = []
    soma = 0

    for i in range(0, 4):
        nota = int(input("Digite o numero: "))
        notas.append(nota)
    for i in range(len(notas)):
        soma = soma + notas[i]
    media = soma / 4

    for i in notas:
        print(i)

    print(media)

    if media < 7:
        print("Alonu reprovado")
    else:
        print("Aluno aprovado")
    

    