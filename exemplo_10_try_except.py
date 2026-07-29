def exemplo_sem_tratamento():
    print("Divisão: ", 10 / 0)
    print("Mesagem depois div")


def exemplo_com_tratamento():
    try:
        print("Divisão: ", 10 / 0)
    except ZeroDivisionError:
        print("Cada dia mais bute")

    print("A butinagem cotinua ininterrupta")


def exemplo_com_tratamento_conversao():
    numero_digitado: str = "dois"
    try:
        #converter str pra int
        numero: int = int(numero_digitado)
        print("Número digitado: ", numero)
    except ValueError:
        print("Texto digitado não e numero valido pela lgvn")
        #print(conteudo)
    
    print("ACAbow")


def exemplo_com_multiplos_tratamentos():
    numero1_digitado = "28"
    numero2_digitado = "9"

    try:
        resultado: int = int(numero1_digitado) / int(numero2_digitado)
        print("Resultado: ", resultado)
    except ZeroDivisionError:
        print("Não quero dividir por 0")
    except ValueError:
        print("Erro, eu so gosto de numeros")
    print("Obrigado por obrigado")


def exemplo_mensagem_erro():
    try:
        aluno = {"nome": "Pedro", "nota1": 9}
        media_aluno = aluno["media"]
        print(media_aluno)
    except KeyError as erro: #'as' serve pra pegar a variavel do erro que ocorreu
        print("Mensagem de erro ao acessar chave:", erro)

#ponto de entrada da aplicação, deve ser unico na aplicação inteira
if __name__ == "__main__":
    exemplo_com_tratamento_conversao()
    exemplo_com_multiplos_tratamentos()