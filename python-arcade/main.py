import adivinhacao
import forca


def escolher_jogo():
    escolha = 0
    while escolha not in (1, 2):
        escolha = int(input('escolha seu jogo: 1 - adivinhação / 2 - forca\n'))
        if escolha == 1:
            adivinhacao.jogar()
        elif escolha == 2:
            forca.jogar()


if __name__ == '__main__':
    escolher_jogo()
