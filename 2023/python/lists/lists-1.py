len_lista = 5
lista = [0] * len_lista

for i in range(5):
  num = int(input(f"num para posição {i + 1}: "))
  lista[i] = num

print(lista)
