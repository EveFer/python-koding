

class Animales():

    def dormir(self):
        print('Estoy durmiendo ...')

    def descripcion(self):
        print('Yo soy un {}'.format(self._animal))


class Perro(Animales):
    pass

class Abeja(Animales):
    def __init__(self, animal):
        self._animal = animal

animal = Animales()

animal.dormir()


perro = Perro()
perro.dormir()

abeja = Abeja('Abeja')
abeja.descripcion()