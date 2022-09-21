import conta

conta1 = conta.Conta()
conta2 = conta.Conta()


def apresentacao():
    print("*********************************************")
    print("******* Bem vindos ao Banco Central *********")
    print("*********************************************\n\n")

def menu():
    print("Selecione a opção deseja no Menu: ")
    print("  [1] Abrir Nova conta\n  [2] Acessar sua conta\n  [3] Central de Atendimento\n")
    escolha = input("=========: ")
    if escolha == "1":
        conta1.abre_conta()

    elif escolha == "2":
        pass

    elif escolha == "3":
        print("Ligue para a Central pelo telefone 0800-0052 ou nos envie um email\nbanco-central@internetbanking.com.br")

    elif escolha != "1" and escolha != "2" and escolha != "3":
        print("Digite apenas os números correspondentes a opção desejada! \n")
        menu()

def administrar_conta():
    print("O que deseja fazer?")
    print(" [1] Depositar\n [2] Sacar\n [3] Transferir\n [4] Consultar Extrato\n [5] Consultar seus Dados\n [6] Alterar Dados\n")
    escolha = input("========:")
    if escolha == "1":
        valor = float(input("Qual Valor deseja Depositar? "))
        conta1.deposita(valor)
        administrar_conta()
    elif escolha == "2":
        valor = float(input("Qual valor deseja Sacar? "))
        conta1.saca(valor)
        administrar_conta()

    elif escolha == "3":
        valor = float(input("Qual valor deseja transferir? "))
        destino = conta2
        conta1.transfere(valor, destino)
        administrar_conta()

    elif escolha == "4":
        conta1.extrato()
        administrar_conta()

    elif escolha == "5":
        conta1.pega_dados()
        administrar_conta()

    elif escolha == "6":
        conta1.altera_dados()
        administrar_conta()

    else:
        print("Digite um valor correspondente a opção desejada!!")
        administrar_conta()




apresentacao()
menu()
administrar_conta()

