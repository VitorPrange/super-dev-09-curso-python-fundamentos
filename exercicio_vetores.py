def exercicio01():
    nomes = []

    nomes.append("vitor")
    nomes.append("Samuel")
    nomes.append("Matheus")
    nomes.append("Gustavo")

    print(nomes[0])
    print(nomes[1])
    print(nomes[2])
    print(nomes[3])


def exercicio02():
    frutas = []
    fruta = input("Digite o nome da fruta: ")
    frutas.append(fruta)
    fruta = input("Digite o nome da fruta: ")
    frutas.append(fruta)
    fruta = input("Digite o nome da fruta: ")
    frutas.append(fruta)
    print(frutas[0])
    print(frutas[1])
    print(frutas[2])


def exercicio03():
    numeros = []

    numero = int(input("Digite o numero: "))
    numeros.append(numero)
    numero = int(input("Digite o numero: "))
    numeros.append(numero)
    numero = int(input("Digite o numero: "))
    numeros.append(numero)
    numero = int(input("Digite o numero: "))
    numeros.append(numero)
    print(numeros[0])
    print(numeros[1])
    print(numeros[2])
    print(numeros[3])


def exercicio04():
    notas = []
    soma = 0
    nota = float(input("Digite a nota: "))
    notas.append(nota)
    soma = soma + nota
    nota = float(input("Digite a nota: "))
    notas.append(nota)
    soma = soma + nota
    nota = float(input("Digite a nota: "))
    notas.append(nota)
    soma = soma + nota
    nota = float(input("Digite a nota: "))
    notas.append(nota)
    soma = soma + nota

    print(notas[0])
    print(notas[1])
    print(notas[2])
    print(notas[3])

    print(notas[0])

    print(notas[3])

    notas[1] = 10

    notas.remove(notas[2])

    print(len(notas))

    media = (notas[0] + notas[1] + notas[2]) / 3

    print(media)

    print(notas[0])
    print(notas[1])
    print(notas[2])

    print(media)

exercicio04()