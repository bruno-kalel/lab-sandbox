def checa_lista(lista):
  total = 0.0
  media = sum(lista) / len(lista)
  for elemento in lista:
    if elemento > media:
      total += elemento
    else:
      total -= 1.0
  return total


print(checa_lista([2.0, 4.0, 2.0, 4.0]))
