def divisao_inteira(num1, num2):
    return num1 // num2


def operacao(num1, num2, func):
    return func(num1, num2)


print(operacao(11, 2, divisao_inteira))
print(divisao_inteira(1, 2))
