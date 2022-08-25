class Animal():
    def __init__(self, nombre):
        self._nombre = nombre

class Perro(Animal):
    def __init__(self,nombre, sonido):
        super().__init__(nombre) # heredar el método init y el atributo nombre
        self._sonido = sonido

perro = Perro('Firulais', 'Guau!!')


print(perro._nombre)