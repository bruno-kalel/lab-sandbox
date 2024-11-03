linhas = 3
colunas = 3
matriz = [[0 for _ in range(colunas)] for _ in range(linhas)]

for i in range(linhas):
  for j in range(colunas):
    valor = int(input(f"valor ({i + 1},{j + 1}): "))
    matriz[i][j] = valor

for linha in matriz:
  print(linha[2])
