lista = ["tomate", "cebola", "arroz", "biscoito", "suco"]
na_lista = False
user_input = input("verificar item na lista: ").lower()

for produto in lista:
  if produto == user_input:
    na_lista = True

if na_lista:
  print(f"{user_input} está presente na lista")
else:
  print(f"{user_input} não está presente na lista")
