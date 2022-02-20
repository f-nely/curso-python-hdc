# j = soma = media = 0
#
# while j < 5:
#     notas = int(input('Digite a nota: '))
#     soma += notas
#     j += 1
#
# media = soma / 5
#
# print(f'A média é: {media}')

soma = notas = media = 0

for i in range(0, 5):
    notas = int(input('Digite a nota: '))
    soma += notas

media = soma / 5

print(f'A média é {media}')
