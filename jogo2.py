
def jogar():
    print("*****************************************")
    print("*******bem vindo ao jogo da forca!*******")
    print("*****************************************")

    palavra_secreta = 'maça'.upper()
    letras_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)
    while(not(enforcou) and not(acertou)):
        chute = input("qual letra? ")
        chute = chute.strip().upper()
        if(chute.upper()  in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                index = index + 1
        else:
            erros = erros + 1
        if (erros == 6):
            enforcou = True
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)
        print("jogando")

    if(acertou):
        print("Você ganhou")
    else:
        print("Você perdeu")
    print("FIM DE JOGO")

if (__name__ == "__main__"):
    jogar()