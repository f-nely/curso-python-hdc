# def soma_ate_100(n):
#     if n < 100:
#         n += 1
#         print(n)
#         return soma_ate_100(n)
#     else:
#         return n
#
#
# print(soma_ate_100(94))

def fatorial(n):
    if n == 1 or n == 0:
        return 1
    return n * fatorial(n - 1)


print(fatorial(2))
