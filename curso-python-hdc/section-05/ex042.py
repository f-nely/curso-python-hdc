lista = []

for i in range(1, 11):
    lista.append(i)

    if i == 4:
        del lista[3]

print(lista)
