salario = float(input('Digite o salário: '))
percentual = float(input('Digite o percentual do aumento: '))

aumento = salario * percentual
novo_salario = salario + aumento

print(f'Salário antigo {salario}')
print(f'Percentual do aumento {percentual}')
print(f'Salário ajustado é {novo_salario}')
