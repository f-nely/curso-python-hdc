carros = {
    'pneus': 4,
    'portas': 2,
    'motor': 1,
    'janelas': 4
}

print(carros)

carros['teto solar'] = True
print(carros)

del carros['motor']
del carros['janelas']
print(carros)
