num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

resultado = num1 * num2

if resultado <= 100:
    print(f'{num1} * {num2} = {resultado}')
    print('baixo')
else:
    print(f'{num1} * {num2} = {resultado}')
    print('alto')
