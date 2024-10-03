import os
import sys

if len(sys.argv) != 2:
  print("uso: [arg1] = diretório")
elif not os.path.exists(sys.argv[1]):
  print("diretório não existe, tente outro nome")
else:
  print(os.listdir(sys.argv[1]))
