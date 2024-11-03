lista = [2, 4, 9, 6]
cont = 0

for i in range(-1, len(lista), 2):
  if lista[i] % 3 == 0:
    cont += 1

print(cont)
