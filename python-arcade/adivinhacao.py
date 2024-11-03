import random


def jogar():
    numero_secreto = random.randint(1, 50)
    numero_tentativas = 0
    pontos = 1000

    print('escolha um nível válido')
    escolha = 0

    while escolha not in (1, 2, 3):
        escolha = int(input('1 - fácil (5t) / 2 - médio (4t) / 3 - difícil (3t)\n'))
    if escolha == 1:
        numero_tentativas = 5
    elif escolha == 2:
        numero_tentativas = 4
    elif escolha == 3:
        numero_tentativas = 3
    for rodada in range(numero_tentativas):
        print('rodada', rodada + 1)

        chute = int(input('chute um número secreto\n'))
        print('você digitou', chute)

        if not 0 < chute < 51:
            print('chute entre 1 e 50')
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if acertou:
            print('acertou')
            break
        else:
            if maior:
                print('seu chute foi MAIOR que o número secreto')
                pontos -= chute - numero_secreto
            elif menor:
                print('seu chute foi MENOR que o número secreto')
                pontos += chute - numero_secreto

    print('pontuação', pontos)
    print('resposta', numero_secreto)
    print('fim do jogo')


if __name__ == '__main__':
    jogar()
