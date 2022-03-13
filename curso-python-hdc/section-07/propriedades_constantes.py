class Carro:
    rodas = 4

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo


carro1 = Carro('Fiat', 'Cronos')
print(carro1.modelo)
