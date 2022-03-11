def multiplicacao_all(*numbers):
    ac = 1
    for i in numbers:
        ac *= i
    return ac


print(multiplicacao_all(2, 3, 5, 4))
