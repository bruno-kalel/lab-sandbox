import sys
import cadastro
import consulta

while True:
  if len(sys.argv) != 1:
    cadastro.cadastrar(True)
    break
  else:
    escolha = int(input('1. cadastrar\n'
                        '2. consultar\n'
                        '3. sair\n'))
    if escolha == 1:
      cadastro.cadastrar(False)
    if escolha == 2:
      consulta.consultar()
    if escolha == 3:
      break
