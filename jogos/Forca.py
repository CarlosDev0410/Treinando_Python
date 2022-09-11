import Menu_jogos
import random

def verifica_entradas(resposta):
    while resposta.type() == str:
        print("Digite apenas 1 ou 2.")
        continue

def carrega_abertura():
    print("***************************")
    print("Bem vindo ao jogo de Forca")
    print("***************************\n")
    print("*********Dica: Frutas******\n")

def carrega_palavras_secretas():
    with open("palavras.txt", "r") as arquivo:
        palavras = []

        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def inicializa_letras_acertadas(palavra_secreta):
    return ["_" for letra in palavra_secreta]

def finalizacao():
    print("Deseja jogar outra vez? [1]Sim ou [2]Não \n")
    resposta = input("?: ")

    verifica_entradas(resposta)

    if (resposta == 1):
        jogar_forca()
    elif (resposta == 2):
        print("Deseja retornar ao Menu de jogos? [1] Sim ou [2] Não")
        final = input("?: ")

        verifica_entradas(final)

        if (final == 1):
            Menu_jogos.entrar_menu()
        elif (final == 2):
            print("Fim de Execução!")
        else:
            print("Digite apenas 1 ou 2")
    else:
        print("Digite apenas 1 ou 2")

def chutar():
    chute = input("Qual Letra? ")
    chute = chute.strip().upper()
    if chute.isdigit():
        print("Digite somente letras!!")
    return chute

def marca_chute_correto(chute, palavra, letras):
    index = 0
    for letra in palavra:
        if (chute.upper() == letra.upper()):
            letras[index] = letra
        index += 1
    print("Você Acertou a letra", chute)

def messagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def messagem_ganhador():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def jogar_forca():

    carrega_abertura()
    palavra_secreta = carrega_palavras_secretas()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas, "\n")

    enforcou = False
    acertou = False
    tentativas = 0

    while(not enforcou and not acertou):

        chute = chutar()

        if(chute in palavra_secreta):
            marca_chute_correto(chute, palavra_secreta, letras_acertadas)
        else:
            tentativas += 1
            desenha_forca(tentativas)

        enforcou = tentativas == 7
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        messagem_ganhador()
    else:
        messagem_perdedor(palavra_secreta)
    finalizacao()


