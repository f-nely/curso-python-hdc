saldo = 359.56
nova_quantia = float(input('Insira um novo: '))

saldo += nova_quantia
print(round(saldo, 2))

valor_removido = 125.98
saldo -= valor_removido

print(f'O saldo restante na conta é de R$ %.2f' % saldo)
