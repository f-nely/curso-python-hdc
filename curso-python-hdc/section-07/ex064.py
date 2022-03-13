class Mamifero:

    def emitir_som(self):
        pass


class Cachorro(Mamifero):

    def emitir_som(self):
        return 'Som cachorro...'


class Gato(Mamifero):

    def emitir_som(self):
        return 'Som gato..'


cachorro = Cachorro()
gato = Gato()

print(cachorro.emitir_som())
print(gato.emitir_som())
