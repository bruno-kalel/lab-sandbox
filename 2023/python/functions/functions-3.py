import sys


def trocar_letras(argumento):
  print(argumento.replace("r", "!"))


if len(sys.argv) != 2:
  print("quantidade de argumentos deve ser 2")
else:
  trocar_letras(sys.argv[1])
