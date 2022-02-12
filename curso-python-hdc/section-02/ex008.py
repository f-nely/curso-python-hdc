salario = float(input('Informe o salário: '))
percentual = float(input('Informe o percentual: '))

aumento = salario * percentual
novo_salario = salario + aumento
print(f'Salário antigo: {salario}')
print(f'Aumento: {aumento}')
print(f'Novo salário {novo_salario}')
