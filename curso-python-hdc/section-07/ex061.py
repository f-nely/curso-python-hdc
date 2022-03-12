class Carro:
    def __init__(self, marca, valor, portas, tanque):
        self.marca = marca
        self.valor = valor
        self.portas = portas
        self.tanque = tanque

    def abastecer(self, litros):
        if self.tanque >= 100:
            print('Tanque está cheio')
        else:
            self.tanque += litros
            if self.tanque > 100:
                self.tanque = 100


carro = Carro('volkswagen', 15000, 4, 32)
print(carro.marca)
print(carro.abastecer(100))
