cars = ['Jetta', 'Honda Civic', 'Pajero', 'Cronos']

item_procurado = str(input('Digite o item procurado: ')).strip().title()

for i in cars:
    if item_procurado == i:
        print(f'Item {item_procurado} encontrado!')

