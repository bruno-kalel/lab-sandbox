salario_bruto = float(input("salario_bruto: "))
inss = salario_bruto * 8 / 100
irpf = 0


def calcular_irpf(num):
  return salario_bruto * num / 100


if salario_bruto <= 1903.98:
  irpf = calcular_irpf(0)

elif 1903.99 <= salario_bruto <= 2826.65:
  irpf = calcular_irpf(7.5)

elif 2826.66 <= salario_bruto <= 3751.05:
  irpf = calcular_irpf(15)

elif 3751.06 <= salario_bruto <= 4664.68:
  irpf = calcular_irpf(22.5)

elif salario_bruto > 4664.68:
  irpf = calcular_irpf(27.5)

salario_liquido = salario_bruto - inss - irpf

print("salario_bruto:", salario_bruto)
print("inss:", inss)
print("irpf:", irpf)
print("salario_liquido:", salario_liquido)
