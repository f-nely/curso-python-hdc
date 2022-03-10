def media_lista(n):
    listas = []
    s = 0
    for i in range(0, n):
        lista = int(input('Digite um valor: '))
        s += lista
        listas.append(lista)
    media = s / n
    return media


lista_numeros = media_lista(3)
print(round(lista_numeros, 2))
