dicionario = dict()

while True:
  cpf = input("cpf: ")
  if cpf == "nao":
    break
  nome = input("nome: ")
  if nome == "nao":
    break

  dicionario[cpf] = nome

print(dicionario)
