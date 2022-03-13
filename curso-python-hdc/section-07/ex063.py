class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


class SuperHeroi(Pessoa):
    def __init__(self, nome, idade, asas):
        super().__init__(nome, idade)
        self.asas = asas

    def voar(self):
        self.asas = True
        return 'Super Herói voa...'


p1 = Pessoa('Pietro', 31)
print(p1.nome)
h1 = SuperHeroi('Homem Passáro', 101, False)
print(h1.voar())
