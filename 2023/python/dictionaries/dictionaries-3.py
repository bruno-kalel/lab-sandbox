dicionario = dict()

while True:
  escolha = int(input("1 - cadastrar aluno\n"
                      "2 - remover aluno\n"
                      "3 - consultar aluno\n"
                      "4 - encerrar\n"))

  if not 1 <= escolha <= 4:
    print("dígito fora dos limites do menu")

  if escolha == 1:
    cpf = input("cpf: ")
    nome = input("nome: ")
    dicionario[cpf] = nome
  if escolha == 2:
    cpf = input("cpf: ")
    del dicionario[cpf]
  if escolha == 3:
    cpf = input("cpf: ")
    print(dicionario.get(cpf))
  if escolha == 4:
    break
