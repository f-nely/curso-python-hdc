class Carro:
    def __init__(self, marca, preco):
        self.ligado = False
        self.marca = marca
        self.preco = preco

    def ligar(self):
        self.ligado = True
        return 'Vrumm'


carro1 = Carro('Volkswagen', 60000)
print(carro1.marca)
print(carro1.preco)
print(carro1.ligar())
