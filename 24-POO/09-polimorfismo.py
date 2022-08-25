
class Animal():
    def __init__(self, mensaje):
        self.mensaje = mensaje

    def dormir(self):
        print(self.mensaje)


class Perro(Animal):

    def dormir(self):
        print('El perro esta durmiendo')


class Pez(Animal):

    def dormir(self):
        print('El pez durmiendo')


perro = Perro('Guau')
perro.dormir()