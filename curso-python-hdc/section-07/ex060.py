class Carro:
    def __init__(self, portas, motor, teto_solar, marca, preco):
        self.portas = portas
        self.motor = motor
        self.teto_solar = teto_solar
        self.marca = marca
        self.preco = preco


carro1 = Carro(4, 2.1, True, 'volkswagen', 137720)
print(carro1.marca)
print(carro1.motor)
print(carro1.preco)
