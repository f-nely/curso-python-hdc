lista = ['Sofá', 'Televisão', 'Rádio', 'AC', 'Poltrona']

item_procurado = str(input('O que deseja buscar na casa? ')).strip().capitalize()
j = 0
while j < len(lista):
    if lista[j] == item_procurado:
        print(f'Encontramos um {item_procurado} na posição {j}!')
    j += 1
