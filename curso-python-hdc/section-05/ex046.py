lista = [30, 11, 9, 6, 20, 3, 12]

menor_valor = lista[0]

for i in lista:
    if i < menor_valor:
        menor_valor = i

print(f'O menor valor é {menor_valor}!')
