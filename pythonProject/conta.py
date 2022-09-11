import pessoa
import random

class Conta(pessoa.Pessoa):

    def __init__(self):
        self.agencia = "0001"
        self.__saldo = 0
        self.__numero = random.randrange(1000, 2000)

    def get_saldo(self):
        return self.__saldo

    def get_dados(self):
        return print("Agencia: {0}\nNúmero da conta: {1}\nNome: {2}\nIdade: {3}\nSexo: {4}\nEstado Civil: {5}\n\n".format(self.agencia, self.__numero, self.nome, self.idade, self.sexo, self.estado_civil))

    def altera_dados(self):
        print("Qual dos dados deseja Alterar? \n")
        print("[1] Nome - [2] Idade - [3] Estado civil\n")
        escolha = input("=======:")
        if escolha == "1":
            novo_nome = input("Digite seu novo nome: ")
            if novo_nome.__len__() < 10:
                print("Digite o nome completo!")
                self.altera_dados()
            else:
                self.nome = novo_nome

        elif escolha == "2":
            nova_idade = int(input("Digite a nova idade: "))
            if nova_idade < 18:
                print("\nVocê não tem idade suficiente!\n")
                self.altera_dados()
            elif self.idade > 100:
                print("Idade Inválida!")
                self.altera_dados()
            else:
                self.idade = nova_idade

        elif escolha == "3":
            print("Escolha o novo Estado Civil!\n")
            print("[1] Solteiro - [2] Casado - [3] Viúvo\n")
            novo_estado_civil = input("=======:")
            if novo_estado_civil == "1":
                self.estado_civil = "Solteiro"
            elif novo_estado_civil == "2":
                self.estado_civil = "Casado"
            elif novo_estado_civil == "3":
                self.estado_civil = "Viúvo"
            else:
                print("Entrada inválida!")
                self.altera_dados()

        else:
            print("Número inválido!!\n")
            self.altera_dados()

    def deposita(self, valor):
        self.__saldo += valor
        print("Você depositou {} na conta de {}\n".format(valor, self.nome.upper()))

    def saca(self, valor):
        if self.__saldo < valor:
            print("Você não tem saldo suficinte!\n")
        else:
            self.__saldo -= valor
            print("Você sacou {}\nSaldo Atual: {}\n".format(valor, self.get_saldo()))

    def extrato(self):
        print("Seus dados:\nAgencia: {0}\nConta: {1}\nTitular: {2}\nSaldo: {3}\n".format(self.agencia, self.__numero, self.nome.upper(), self.__saldo))

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)
        print("Transferencia Realizada de {0} Para {1}\n".format(self.nome.upper(), destino.nome))

    def abre_conta(self):
        print("Vamos Abrir sua Conta. \nEntre com os dados solicitados!\n")

        self.nome = input("Digite seu nome Completo: ")
        if self.nome.isdigit():
            print("\nNome inválido, Não utilize números.\nVamos começar outra vez\n")
            self.abre_conta()
        elif self.nome.__len__() < 10:
            print("Digite o nome completo!")
            self.abre_conta()

        self.idade = int(input("Digite a sua idade: "))
        if self.idade < 18:
            print("\nVocê não tem idade para abrir uma conta!\nRetornando ao Início\n")
            self.abre_conta()
        elif self.idade > 100:
            print("Idade Inválida!")
            self.abre_conta()

        print("Qual seu sexo? \n" )
        print("[1] Masculinho - [2] Feminino\n")
        sexo = input("=======:")
        if sexo == "1":
            self.sexo = "Masculino"
        elif sexo == "2":
            self.sexo = "Feminino"
        else:
            print("Entrada inválida!")
            self.abre_conta()

        print("Qual seu Estado Civil: \n")
        print("[1] Solteiro - [2] Casado - [3] Viúvo\n")
        estado_civil = input("=======:")
        if estado_civil == "1":
            self.estado_civil = "Solteiro"
        elif estado_civil == "2":
            self.estado_civil = "Casado"
        elif estado_civil == "3":
            self.estado_civil = "Viúvo"
        else:
            print("Entrada inválida!")
            self.abre_conta()

        print("\nParabens, Você abriu a sua conta!\nO Banco Central agradece a sua preferência\n")
        print("Seus dados:\nAgencia: {0}\nConta: {1}\nTitular: {2}\nSaldo: {3}\n".format(self.agencia, self.__numero, self.nome.upper(), self.__saldo))




