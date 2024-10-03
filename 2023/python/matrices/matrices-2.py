matriz = [[7, 4, 9, 2],
          [1, 3, 5, 7],
          [2, 1, 8, 9],
          [7, 8, 3, 4]]

for linha in matriz:
  print(linha)

for i in range(len(matriz)):
  matriz[i][i] = 0

for linha in matriz:
  print(linha)
