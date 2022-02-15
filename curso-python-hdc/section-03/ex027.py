renda = int(input('Digite sua renda atual: '))
limite = 0

if renda < 2000:
    limite = 1000
elif renda < 4000:
    limite = 2000
elif renda < 10000:
    limite = 3000
elif renda > 10000:
    print('Você precisa falar com o gerente.')
    limite = 3000

print(f'O seu cartão foi aprovado, e o limite é de R$ {limite}')
