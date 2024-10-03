linhas = 4
colunas = 4
matriz = [[0 for _ in range(colunas)] for _ in range(linhas)]

for linha in matriz:
  print(linha)

for i in range(linhas):
  for j in range(colunas):
    if i < j:
      matriz[i][j] = 2 * i + 2 * j
    elif i > j:
      matriz[i][j] = 3 * i + 3 * j
    else:
      matriz[i][j] = 4 * i + 4 * j

for linha in matriz:
  print(linha)
