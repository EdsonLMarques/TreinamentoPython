import random
def jogar():
    print("**********************")
    print("jogo 1")
    print("**********************")
    numero_secreto = random.randrange(1,101)
    tentativas = 0
    rodada = 1
    pontos = 1000
    print("qual o nivel de dificuldade")
    print("(1) Fácil (2) Médio (3) Difícil")
    nivel = int(input("defina o nivel: "))
    if (nivel == 1):
        tentativas = 20
    elif (nivel == 2):
        tentativas = 10
    else:
        tentativas = 5
    for rodada in range(1, tentativas + 1):
        print("rodada: {} de {}".format(rodada, tentativas))
        chute = int(input("digite seu numero: "))
        print("voce digitou: ", chute)
        if chute < 1 or chute > 100:
            print("Voce deve digitar um valor de 0 a 100")
            continue
        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto
        if acertou:
            print("voce acertou e fez {}".format(pontos))
            break
        else:
            if maior:
                print(" valor que voce digitou é maior")
            elif menor:
                print("o valor que voce digitou é menor")
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos
if (__name__ == "__main__"):
    jogar()