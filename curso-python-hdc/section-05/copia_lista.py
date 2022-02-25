lista = [1, 2, 3]
nova_lista = lista

print(lista)
print(nova_lista)

nova_lista[0] = 1000
print(nova_lista, lista)

lista[0] = 5000
print(lista, nova_lista)
