
def jogar():
    print("*****************************************")
    print("*******bem vindo ao jogo da forca!*******")
    print("*****************************************")

    palavra_secreta = 'banana'
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]
    enforcou = False
    acertou = False
    print(letras_acertadas)
    while(not(enforcou) and not(acertou)):

        chute = input("qual letra? ")
        chute = chute.strip()

        index = 0
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                letras_acertadas[index] = letra
            index = index + 1

        print(letras_acertadas)
        print("jogando")

    print("fim de jogo")

if (__name__ == "__main__"):
    jogar()