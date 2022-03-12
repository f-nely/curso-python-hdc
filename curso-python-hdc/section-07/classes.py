class Pessoa:
    def __init__(self, nome, idade, profissao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao


p1 = Pessoa('Matheus', 29, 'Programador')
print(p1.nome)
print(p1.idade)
print(p1.profissao)
print(f'{p1.nome} tem {p1.idade} anos e é {p1.profissao}.')
