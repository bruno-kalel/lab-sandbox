import sys


def escrever_arquivo(dado1, dado2):
  with open('base_alunos.txt', 'a') as arquivo:
    arquivo.write(dado1 + " || " + dado2 + "\n")


def cadastrar(boolean):
  if boolean:
    print('sys.arg')
    if len(sys.argv) != 3:
      print('para uso os argumentos são: nome do script, matrícula e nome, respectivamente')
    else:
      matricula = sys.argv[1]
      nome = sys.argv[2]
      escrever_arquivo(matricula, nome)
  else:
    matricula = input('matricula: ')
    nome = input('nome: ')
    escrever_arquivo(matricula, nome)
