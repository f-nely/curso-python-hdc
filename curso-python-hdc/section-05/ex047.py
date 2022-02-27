# p1 = ['Mesa', 'Rack', 'Armário']
# p2 = ['Azul', 'Branco', 'Cinza']
# p3 = [400, 200, 700]
#
# produtos = [p1, p2, p3]
#
# print(produtos)
# for produto in produtos:
#     print(f'O nome do produto: {produto[0]}')

p1 = ['Camisa', 'Azul', 25.62]
p2 = ['Bermuda', 'Marrom', 112.90]
p3 = ['Casaco', 'Bege', 200.00]

produtos = [p1, p2, p3]
print(produtos)

for produto in produtos:
    print(f'O produto é: {produto[0]} e tem cor {produto[1]} e o preço é R${produto[2]}')
