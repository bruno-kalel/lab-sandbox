def executa_funcao1(num):
  if num % 2 == 0 and num > 2:
    executa_funcao2(num)
  else:
    num += 1
    executa_funcao1(num)


def executa_funcao2(cont):
  print(cont)


executa_funcao1(1)
