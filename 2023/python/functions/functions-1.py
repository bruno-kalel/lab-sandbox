import random

lista = []


def gerar_lista(num):
  for _ in range(num):
    lista.append(random.randint(1, 10))


gerar_lista(5)
print(lista)
