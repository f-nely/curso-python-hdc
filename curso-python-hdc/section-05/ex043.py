lst = ['Amarok', 'Jeep Compass', 'Cronos', 'Sandero']

it1 = str(input('Digite o primeiro item procurado: ')).strip().title()
it2 = str(input('Digite o segundo item procurado: ')).strip().title()

# r1 = lst.index(it1)
# print(r1)
# r2 = lst.index(it2)
# print(r2)
#
# if r1 and r1 < r2:
#     print(f'O item {it1} foi encontrado primeiro')
# if r2 and r2 < r1:
#     print(f'O item {it2} foi encontrado primeiro')

j = 0
while j < len(lst):
    if lst[j] == it1:
        print(f'O item {it1} foi encontrado primeiro')
        break
    elif lst[j] == it2:
        print(f'O item {it2} foi encontrado primeiro')
        break
    j += 1
