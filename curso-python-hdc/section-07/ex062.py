class Banco:
    def __init__(self, nome, saldo):
        self.nome = nome
        self.saldo = saldo

    def deposito(self, valor):
        self.saldo += valor

    def saque(self, valor):
        self.saldo -= valor

    def transferencia(self, outra_conta, valor):
        self.saldo -= valor
        outra_conta.saldo += valor


conta1 = Banco('Pietro', 1500)
print(f'{conta1.nome} tem de saldo R${conta1.saldo}')
conta1.deposito(500)
print(f'{conta1.nome} tem de saldo R${conta1.saldo}')
conta1.saque(100)
print(f'O saldo é R${conta1.saldo}')
conta2 = Banco('Diana', 3000)
print(f'{conta2.nome} tem de saldo R${conta2.saldo}')
conta1.transferencia(conta2, 350)
print(conta2.saldo)
print(conta1.saldo)
