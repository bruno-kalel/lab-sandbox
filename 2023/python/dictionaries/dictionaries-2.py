dicionario = dict()

while True:
  code = input("código: ")
  if code == "nao":
    break
  name = input("nome: ")
  if name == "nao":
    break
  price = input("preço: ")
  if price == "nao":
    break

  dicionario[code] = [name, price]

print(dicionario)
