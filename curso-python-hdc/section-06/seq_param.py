def sum_all(*numbers):
    s = 0
    for number in numbers:
        s += number
    return s


print(sum_all(10, 2, 13, 5, 1))
