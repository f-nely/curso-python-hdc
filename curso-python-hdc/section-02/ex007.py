notas = 0
media = 0
soma = 0

for i in range(0, 3):
    notas = float(input('Digite a nota: '))
    soma += notas

media = soma / 3
round(media, 2)

if media >= 7:
    print(f'A média é {media}:')
else:
    print(f'Aluno com a média {media} reprovado: ')
