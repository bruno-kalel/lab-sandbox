with open('arq_musica.txt', 'r') as original:
  texto = original.read()
  for letra in texto:
    texto_novo = ''.join(['!' if letra.isalpha() and letra.lower(
    ) not in 'aeiou' else letra for letra in texto])

with open('novo_arq_musica.txt', 'w') as novo:
  novo.write(texto_novo)
