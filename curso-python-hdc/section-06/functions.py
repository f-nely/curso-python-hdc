def uppercase():
    name = str(input('Informe o seu nome: ')).upper()
    return name


def subtracao(num1, num2):
    return num1 - num2


def divisao(num1, num2):
    if num2 > 0:
        return num1 / num2

    return 0


def exponenciacao(num1, num2):
    return num1 ** num2
