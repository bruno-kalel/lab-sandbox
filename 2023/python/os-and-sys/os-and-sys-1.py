import os
import sys

if len(sys.argv) != 4:
  print("uso: [arg1] = diretório, [arg2] = arquivo, [arg3] = conteúdo")
elif os.path.exists(sys.argv[1]):
  print("diretório já existe, tente outro nome")
else:
  os.mkdir(sys.argv[1])
  with open(f'{sys.argv[2]}.txt', 'w') as arquivo:
    arquivo.write(sys.argv[3])
