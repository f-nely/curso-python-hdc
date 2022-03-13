class Pessoa:
    def __init__(self, nome, sexo, cpf, ativo):
        self.__nome = nome
        self.__sexo = sexo
        self.__cpf = cpf
        self.__ativo = ativo

    def desativar(self):
        self.__ativo = False
        print('A pessoa foi desativada com sucesso.')

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome


p1 = Pessoa('Aaron', 'M', '123.456.789-00', True)
p1.desativar()
p1.ativo = True
print(p1.ativo)

p1.set_nome('Guido')
print(p1.get_nome())
