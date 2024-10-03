with open('arq_coxinha.txt', 'r') as arquivo:
  texto = arquivo.read()
  quantidade_vogais = sum(
    1 for caractere in texto if caractere.lower() in 'aeiou')

print(texto)
print(quantidade_vogais)
