def exercicios():

    def exercicio_01_mensagens():
        print("Ola, seja bem vindo")
        print("Estou aprendendo a programar em python")
        print("Pyhton pode ser usado para criar varios tipos de programas")

    def exercicio_02_variaveis():
        nome: str = "prange"
        idade: int = 18
        cidade: str = "Blumenau"

        print(f"Nome: {nome}\nIdade: {idade}\nCidade: {cidade}")

    def exercicio_03_input_nome():
        nome: str = input("Digite seu nome: ")

        print(f"Ola, {nome} seja bem vindo ao sistema!")

    def exercicio_04_dados_pessoais():
        nome: str = input("Digite seu nome: ").capitalize()
        bairro: str = input("Digite o seu bairro: ")
        cidade: str = input("Digite a sua cidade: ")

        print(f"{nome} mora no bairro {bairro}, na cidade de {cidade}")

    def exercicio_05_idade_int():
        idade: str = int(input("Digite a sua idade: "))
        bairro: str = input("Digite o seu bairro: ")
        cidade: str = input("Digite a sua cidade: ")

        print(f"Voce tem {idade} anos")

    def exercicio_06_idade_proximo_ano():
        nome: str = input("Digite seu nome: ").capitalize()
        idade: str = int(input("Digite a sua idade: "))

        print(f"{nome}, No proximo ano voce tera {idade + 1}")

    def exercicio_07_dobro_numero_inteiro():
        numero: str = int(input("Digite o numero: "))

        print(f"O dobro de {numero} é {numero*2}")

    def exercicio_08_maioridade():
        idade: str = int(input("Digite a sua idade: "))

        if idade >= 18:
            print("Voce é maior de idade")
        else:
            print("Voce é menor de idade")

    def exercicio_09_numero_positivo():
        numero: str = int(input("Digite o numero: "))

        if numero > 0:
            print("O numero é positivo")
        else:
            print("O numero não é positivo")

    def exercicio_10_entrada_evento():
        nome: str = input("Digite seu nome: ").capitalize()
        idade: str = int(input("Digite a sua idade: "))

        if idade >= 16:
            print(f"{nome} voce pode entrar no evento")
        else:
            print(f"{nome} voce não pode entrar no evento")

    def exercicio_11_verificar_nota():
        nota: float = float(input("Digite a nota: "))

        if nota >= 7:
            print("Aluno aprovado")
        else:
            print("Aluno reprovado")

    def exercicio_12_verificar_saldo():
        saldo: float = float(input("Digite o saldo: "))
        valor: float = float(input("Digite o valor: "))

        if valor > saldo:
            print("Saldo insuficiente")
        else:
            print("Compra aprovada")

    def exercicio_13_aprovacao_nota_frequencia():
        nota: float = float(input("Digite a nota: "))
        frequencia: int = int(input("Digite a frequencia: "))

        if nota >= 7 and frequencia >= 75:
            print("Aluno aprovado")
        else:
            print("Aluno reprovado")

    def exercicio_14_entrada_gratuita():
        idade: str = int(input("Digite a sua idade: "))

        if idade < 6 or idade >= 60:
            print("Entrada gratuita")
        else:
            print("Entrada paga")

    def exercicio_15_login_simples():
        usuario: str = input("Digite o seu usuario: ")
        senha: str = input("Digite a sua senha: ")

        if usuario == "admin" and senha == "1234":
            print("Login realizado com sucesso")
        else:
            print("Usuario ou senha incorretos")

    def exercicio_16_mensagem_varias_vezes():
        index: int = 1

        while index < 6:
            print("Estou aprendedo Python")

            index += 1

    def exercicio_17_numeros_pares():
        numero: int = 0

        while numero < 20:
            numero = numero + 2
            print(numero)
    def exercicio_18_repetir_mensagem():
        mensagem: str = str(input("Digite a mensagem"))
        vezes: int = int(input("Digite o numero de repetições"))

        while vezes > 0:
            print(mensagem)

            vezes -= 1

    def exercicio_19_somar_1_ate_n():
        numero: int = int(input("Digite um número: "))
        contador: int = 1
        soma: int = 0

        while contador <= numero:
            soma = soma + contador
            contador += 1

        print(f"A soma é {soma}")

    def exercicio_20_senha_while():
        senha: str = str(input("Digite a senha"))

        while senha != "1234":
            senha = input("Senha incorreta, digite novamente")
        print("Senha correta")

    def exercicio_extra_fatorial():
            numero: int = int(input("Digite o numero "))
            contador: int = 1
            soma: int = 1

            while contador <= numero:
                soma = soma * contador
                contador += 1
            print(soma)

    def exercicio_22_tabuada_while():
        i: int = 1
        numero_tabuada: int = int(input("Digite o numero: "))

        while i <= 10:
            print(f"{i} X {numero_tabuada} = {i * numero_tabuada}")
            i += 1

    def exercicio_23_somar_ate_zero():
        numero: int = int(input("Digite o numero: "))
        soma: int = 0

        while numero != 0:
            soma = soma + numero
            numero: int = int(input("Digite o numero: "))
        print(f"Soma: {soma}")

    def exercicio_24_contar_positivos():
        numero: int = int(input("Digite o numero: "))
        positivo: int = 0

        while numero != 0:
            if numero > 0:
                positivo += 1
            numero: int = int(input("Digite o numero: "))
        print(f"Numeros positivos: {positivo}")

    def exercicio_25_maior_numero():
        i: int = 0
        maior: int = 0

        while i < 5:
            numero: int = int(input("Digite o numero: "))
            if i == 0:
                maior= numero
            elif numero > maior:
                maior = numero
            i += 1
        print(f"Maior Numero: {maior}")

    def exercicio_26_media_notas_while():
        i: int = 1
        soma: int = 0

        while i <= 4:
            nota:float = float(input(f"Digite a {i} nota: "))
            soma = soma + nota
            i += 1
        print(f"A media do aluno é {soma / 4}")

    def exercicio_27_senha_tentativas():
        senha: str = input("Digite a senha: ")
        tentativas: int = 0

        while tentativas < 3:
            if senha == "1234":
                print("Acesso liberado")
                return
            else:
                print(f"Senha incorreta, Voce tem {3 - tentativas} restantes")
                tentativas += 1
                senha: str = input("Digite a senha: ")
        print("Acesso bloqueado")

    def exercicio_28_validar_idade():
        idade: int = int(input("Digite a idade: "))

        while idade < 0 or idade > 120:
            idade: int = int(input("Digite uma idade valida: "))
        print("Idade cadastrada com sucesso!")

    def exercicio_29_adivinhar_numero():
        numero: int = int(input("Tente adivinhar o numero secreto: "))

        while numero != 9:
            if numero > 9:
                print("O numero secreto é menor")
                numero: int = int(input("Tente adivinhar o numero secreto: "))
            elif numero < 9:
                print("O numero secreto é maior")
                numero: int = int(input("Tente adivinhar o numero secreto: "))
        print("Parabens voce acertou")

    def exercicio_30_menu_operacoes():

        opcao: int = int(input("""Digite a opção:
1 - Somar dois números
2 - Subtrair dois números
3 - Multiplicar dois números
0 - Sair
"""))

        while opcao != 0:

            if opcao == 1:
                numero1: int = int(input("Digite o primeiro numero: "))
                numero2: int = int(input("Digite o segundo numero: "))

                print(f"A soma dos dois numeros é {numero1 + numero2}")
            elif opcao == 2:
                numero1: int = int(input("Digite o primeiro numero: "))
                numero2: int = int(input("Digite o segundo numero: "))

                print(f"A subtração dos dois numeros é {numero1 - numero2}")
            elif opcao == 3:
                numero1: int = int(input("Digite o primeiro numero: "))
                numero2: int = int(input("Digite o segundo numero: "))

                print(f"A multiplicação dos dois numeros é {numero1 * numero2}")
            else:
                print("Numero invalido")

            opcao: int = int(input("""Digite a opção:
1 - Somar dois números
2 - Subtrair dois números
3 - Multiplicar dois números
0 - Sair
"""))
        print("Programa Encerrado")
    
    def exercicio_31_triangulos():
        lado1: int = int(input("Digite o primeiro lado: "))
        lado2: int = int(input("Digite o segundo lado: "))
        lado3: int = int(input("Digite o terceiro lado: "))

        opcao: int = int(input("1 - Equilatero\n2 - Escaleno\n 3 - Isóceles\n0 - Sair"))

        while opcao != 0:
            if opcao == 1:
                if lado1 == lado2 and lado2 == lado3:
                    print("Equilatero")
                else:
                    print("Não é Equilatero")
            elif opcao == 2:
                if lado1 != lado2 and lado2 != lado3 and lado1 != lado3:
                    print("Escaleno")
                else:
                    print("Não é Escaleno")
            elif opcao == 3:
                if (lado1 == lado2 and lado2 != lado3) or (lado2 == lado3 and lado3 != lado1) or (lado3 == lado1 and lado1 != lado2):
                   print("Isóceles")
                else:
                   print("Não é Isóceles")
            opcao: int = int(input("1 - Equilatero\n2 - Escaleno\n 3 - Isóceles\n0 - Sair"))



    def exercicio_21_menu_simples():

        opcao: str = input("Digite o numero da atividade que deseja executar [1-20] ou digite 0 pra sair: ")

        while opcao != "0":
            if opcao == "1":
                exercicio_01_mensagens()
            elif opcao == "2":
                exercicio_02_variaveis()
            elif opcao == "3":
                exercicio_03_input_nome()
            elif opcao == "4":
                exercicio_04_dados_pessoais()
            elif opcao == "5":
                exercicio_05_idade_int()
            elif opcao == "6":
                exercicio_06_idade_proximo_ano()
            elif opcao == "7":
                exercicio_07_dobro_numero_inteiro()
            elif opcao == "8":
                exercicio_08_maioridade()
            elif opcao == "9":
                exercicio_09_numero_positivo()
            elif opcao == "10":
                exercicio_10_entrada_evento()
            elif opcao == "11":
                exercicio_11_verificar_nota()
            elif opcao == "12":
                exercicio_12_verificar_saldo()
            elif opcao == "13":
                exercicio_13_aprovacao_nota_frequencia()
            elif opcao == "14":
                exercicio_14_entrada_gratuita()
            elif opcao == "15":
                exercicio_15_login_simples()
            elif opcao == "16":
                exercicio_16_mensagem_varias_vezes()
            elif opcao == "17":
                exercicio_17_numeros_pares()
            elif opcao == "18":
                exercicio_18_repetir_mensagem()
            elif opcao == "19":
                exercicio_19_somar_1_ate_n()
            elif opcao == "20":
                exercicio_20_senha_while()
            elif opcao == "22":
                exercicio_22_tabuada_while()
            elif opcao == "23":
                exercicio_23_somar_ate_zero()
            elif opcao == "24":
                exercicio_24_contar_positivos()
            elif opcao == "25":
                exercicio_25_maior_numero()
            elif opcao == "26":
                exercicio_26_media_notas_while()
            elif opcao == "27":
                exercicio_27_senha_tentativas()
            elif opcao == "28":
                exercicio_28_validar_idade()
            elif opcao == "29":
                exercicio_29_adivinhar_numero()
            elif opcao == "30":
                exercicio_30_menu_operacoes()
            elif opcao == "31":
                exercicio_31_triangulos()
            elif opcao == "extra":
                exercicio_extra_fatorial()
            else:
                print("Opção inválida")

            opcao = input("Digite o numero da atividade que deseja executar [1-31 ou escreva extra pro fatorial] ou digite 0 pra sair: ")

        



    exercicio_21_menu_simples()

exercicios()