from random import randint

aleatorio = randint(0, 10)

num = int(input('Digite um número entre [0, 10] '))

if num == aleatorio:
    print(f'Parabéns. Você acertou, o número é: {aleatorio}')
else:
    print(f'Você errou! o número era: {aleatorio}')
