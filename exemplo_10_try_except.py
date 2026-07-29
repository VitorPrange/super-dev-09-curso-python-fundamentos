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

#ponto de entrada da aplicação, deve ser unico na aplicação inteira
if __name__ == "__main__":
    exemplo_com_tratamento_conversao()