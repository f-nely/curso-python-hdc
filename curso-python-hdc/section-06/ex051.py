def func_ten(number):
    result = ''
    if number > 10:
        result = 'Maior que 10'
    elif number == 10:
        result = 'Igual a 10'
    else:
        result = 'Menor que 10'
    return result


print(func_ten(10))
