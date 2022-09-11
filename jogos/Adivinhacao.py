import random
import Menu_jogos

def jogar_adivinhacao():
    print("**********************************")
    print("Bem vindo ao jogo de adivinhação!")
    print("**********************************")
    print("Tente adivinhar o número escolhido \npelo computador.\nNúmeros de (1 a 50)")
    print("**********************************")
    print("\n")


    pontos = 1000
    rodada = 1
    tentativas = 0
    numero_secreto = random.randrange(1, 51)

    print("Selecione seu nível de dificuldade.\nDigite o número correspondente: \n")
    print("[1]-Fácil (10 Tentativas)\n[2]-Normal (5 tentativas)\n[3]-Dificil (3 Tentativas) \n")
    nivel = int(input("Nível: "))

    if(nivel == 1):
        tentativas = 10
    elif(nivel == 2):
        tentativas = 5
    else:
        tentativas = 3

    while(rodada <= tentativas):
        print("Tentativa {} de {} ".format(rodada, tentativas),"\n")
        chute = int(input("Digite o seu número: "))

        acerto = numero_secreto == chute
        chute_maior = numero_secreto < chute
        chute_menor = numero_secreto > chute

        if(chute < 1 or chute > 50):
            print("Você deve digitar um número entre [1 e 50]")
            continue

        if (acerto):
            print("***********************")
            print("Você Acertou! Parabéns")
            print("Pontuação final {}".format(pontos))
            print("***********************\n")
            break
        else:
            if(chute_maior):
                print("Você Errou! Seu Chute foi maior que o número escolhido. Tente outra vez.\n")
            elif(chute_menor):
                print("Você Errou! Seu Chute foi menor que o número escolhido. Tente outra vez.\n")

            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

        rodada = rodada + 1


    print("Fim de Jogo! \n")
    print("Deseja jogar outra vez? [1]Sim ou [2]Não \n")
    resposta = int(input("?: "))

    if(resposta == 1):
        jogar_adivinhacao()
    elif(resposta == 2):
        print("Deseja retornar ao Menu de jogos? [1] Sim ou [2] Não")
        final = int(input("?: "))
        if(final == 1):
            Menu_jogos.entrar_menu()
        elif(final == 2):
            print("Fim de Execução!")
        else:
            print("Digite apenas 1 ou 2")
    else:
        print("Digite apenas 1 ou 2")



if(__name__ == "__main__"):
    entrar_menu()