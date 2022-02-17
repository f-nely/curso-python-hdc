n = int(input('Digite um número: '))

divisoes = 0

contador = n

while contador > 0:

    if n % contador == 0:
        divisoes += 1

    contador -= 1

if divisoes == 2:
    print(f'O número é primo {n}')
else:
    print(f'O número não é primo {n}')
