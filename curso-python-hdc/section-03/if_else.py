poupanca = 200
saque = 300

if saque <= poupanca:
    print(f'Você sacou R$ {saque}')
    poupanca -= saque
    print(f'Saldo restante R$ {poupanca}')
else:
    print(f'Você não tem saldo para sacar R$ {saque}')
    print(f'Sua poupança tem no momento R$ {poupanca}')
