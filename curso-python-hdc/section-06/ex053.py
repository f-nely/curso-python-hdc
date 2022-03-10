def list_numbers(n):
    listas = []
    for i in range(0, n):
        lista = int(input('Digite um valor: '))
        if lista % 2 == 0:
            listas.append(lista)
    return listas


listas_pares = list_numbers(6)
print(listas_pares)
