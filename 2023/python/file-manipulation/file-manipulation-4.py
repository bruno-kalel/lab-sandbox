while True:
  escolha = int(input("1 - cadastrar matrícula e nome do aluno\n"
                      "2 - consultar matrícula\n"
                      "3 - remover aluno usando matrícula\n"
                      "4 - encerrar\n"))

  if not 1 <= escolha <= 4:
    print("dígito fora dos limites do menu")
  else:
    if escolha == 1:
      matricula = input("matricula: ")
      nome = input("nome: ")
      with open('base_alunos.txt', 'a') as arquivo:
        arquivo.write(matricula + " - " + nome + "\n")
    if escolha == 2:
      matricula = input("matricula: ")
      encontrado = False
      with open('base_alunos.txt', 'r') as arquivo:
        linhas = arquivo.readlines()
        for linha in linhas:
          if matricula in linha:
            encontrado = True
            _, nome = linha.strip().split(' - ')
            print(nome)
      if not encontrado:
        print('aluno não encontrado')
    if escolha == 3:
      matricula = input("matricula: ")
      with open('base_alunos.txt', 'r') as arquivo:
        linhas = arquivo.readlines()
        novas_linhas = [linha for linha in linhas if matricula not in linha]
      with open('base_alunos.txt', 'w') as arquivo:
        arquivo.writelines(novas_linhas)
    if escolha == 4:
      break
