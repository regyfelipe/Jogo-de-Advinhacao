import random


def jogar():

    print("********************************")
    print('Bem vindo no jogo de adivinhação')
    print("********************************")

    numero_secreto = round(random.randrange(1,21))
    total_de_tentativas = 3
    pontos = 1000

    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Define o nivel: "))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel ==2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5


    for rodada in range(1, total_de_tentativas + 1):
        print("tentativas {} de {}".format(rodada, total_de_tentativas))
        chute_str = input("Digite o seu numero: ")
        print("você digitou ", chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 20):
            print("você deve digitar um número entre 1 e 20!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            print("voce acertou e fez {} pontos".format(pontos))
            break
        else:
            if(maior):
                print("voce errou! O seu chute foi maior do que o número secreto")
            elif(menor):
                print("voce errou! O seu chute foi menor do que o número secreto")
            pontos_perdidos = abs(numero_secreto - chute) #40-60
            pontos = pontos - pontos_perdidos


print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()
