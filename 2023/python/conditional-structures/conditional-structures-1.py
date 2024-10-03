peso = float(input("peso: "))
altura = float(input("altura: "))

imc = peso / (altura**2)

if imc < 17:
  print("muito abaixo do peso")
elif 17 < imc < 18.49:
  print("abaixo do peso")
elif 18.5 < imc < 24.99:
  print("peso normal")
elif 25 < imc < 29.99:
  print("acima do peso")
elif 30 < imc < 34.99:
  print("obesidade 1")
elif 35 < imc < 39.99:
  print("obesidade 2")
else:
  print("fora dos limites estabelecidos")
