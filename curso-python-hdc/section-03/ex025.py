num = int(input('Digite um número: '))

if num > 10:

    if num > 20:
        print('Número maior que 20')
        print(num * 2)
    else:
        print('Número menor que 20')
        print(num * 5)

else:
    print('O número precisa ser maior que 10.')
