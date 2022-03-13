class Veiculo:
    def __init__(self, rodas, marca, ligaado):
        self.rodas = rodas
        self.marca = marca
        self.ligado = ligaado

    def ligar(self):
        self.ligado = True
        return 'Vrummm!'


class Carro(Veiculo):
    def __init__(self, rodas, marca, ligado, teto_solar):
        super().__init__(rodas, marca, ligado)
        self.teto_solar = teto_solar


class Moto(Veiculo):
    def __init__(self, rodas, marca, ligado, protecao_lateral):
        super(Moto, self).__init__(rodas, marca, ligado)
        self.protecao_lateral = protecao_lateral

    def empinar(self):
        self.ligado = True
        return 'Empinou a moto!'


carro1 = Carro(4, 'Ford', False, True)
print(carro1.marca)
print(carro1.ligar())

moto1 = Moto(2, 'Bros', False, True)
print(moto1.marca)
print(moto1.empinar())
