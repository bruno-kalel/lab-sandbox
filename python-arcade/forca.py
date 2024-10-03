import random


def imprimir_abertura():
    print('bem-vindo à forca')


def carregar_palavra():
    palavras = []

    with open('palavras.txt', 'r') as arquivo:
        for linha in arquivo:
            palavras.append(linha.strip().lower())

    return palavras[random.randrange(0, len(palavras))]


def inicializar_tracinhos(palavra):
    return ['_' for letra in palavra]


def pedir_chute():
    return input('qual letra?\n').strip().lower()


def marcar_correto(chute, tracinhos, palavra):
    index = 0
    for letra in palavra:
        if chute == letra:
            tracinhos[index] = letra
        index += 1


def desenhar_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if erros == 1:
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if erros == 2:
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if erros == 3:
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if erros == 4:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if erros == 5:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if erros == 6:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if erros == 7:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def jogar():
    imprimir_abertura()

    palavra = carregar_palavra()

    tracinhos = inicializar_tracinhos(palavra)

    enforcou = False
    acertou = False
    erros = 0

    while not enforcou and not acertou:
        print(tracinhos)
        chute = pedir_chute()

        if chute in palavra:
            marcar_correto(chute, tracinhos, palavra)
        else:
            erros += 1
            print(f'ops, você errou! faltam {7 - erros} tentativas')
            desenhar_forca(erros)

        enforcou = erros == 7
        acertou = '_' not in tracinhos

    if acertou:
        print('você ganhou')
        print(tracinhos)
    else:
        print('você perdeu')
        print(f'a palavra era {palavra}')


if __name__ == '__main__':
    jogar()
