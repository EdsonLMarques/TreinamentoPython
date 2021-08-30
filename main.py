import jogo1
import jogo2

print("**********************")
print("***Escolha seu jogo***")
print("**********************")

print("(1) ADIVINHAÇÂO (2) FORCA")

jogo = int(input("Qual jogo? "))

if jogo == 1:
    print("abrindo jogo da adivinhação")
    jogo1.jogar()
elif jogo == 2:
    print("abrindo jogo da forca")
    jogo2.jogar()