import random


def gerar_num():
  num = random.randint(1, 100)
  with open('par_ou_impar.txt', 'w') as arquivo:
    if num % 2 == 0:
      arquivo.write(f"o número gerado {num} é par")
    else:
      arquivo.write(f"o número gerado {num} é ímpar")


gerar_num()
