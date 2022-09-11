import Forca
import Adivinhacao


def entrar_menu():
    print("**********************************")
    print("Bem vindo ao Menu de jogos!")
    print("**********************************\n")
    print("Selecione seu jogo!\n")
    print("[1]-Adivinhação\n[2]-Forca")
    jogo = int(input("?: "))

    if(jogo == 1):
        print("Adivinhação")
        Adivinhacao.jogar_adivinhacao()
    elif(jogo == 2):
        print("Forca")
        Forca.jogar_forca()
    else:
        print("Jogo Invalido! Digite apenas 1 ou 2")

