'''
Crear una clase Fabrica que tenga los atributos de Llantas, Color y Precio; 
luego crear dos clases mas que hereden de Fabrica, las cuales son Moto y Carro. 
Crear metodos que muestren la cantidad de llantas, color y precio de ambos transportes. 
Por ultimo, crear objetos para cada clase y mostrar por pantalla los atributos de 
cada uno
'''

class Factory():
    def __init__(self, llantas, color, precio):
        self._llantas = llantas
        self._color = color
        self._precio = precio

    @property
    def llantas(self):
        return self._llantas
    
    @llantas.setter
    def llantas(self, llantas):
        self._llantas = llantas
    
    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color
    
    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, precio):
        self._precio = precio


class Car(Factory):
    pass

class Moto(Factory):
    pass


car = Car(4, 'Gris', 120000)

print(car.llantas)
print(car.color)
print(car.precio)

moto = Moto(2, 'Verde', 60000)

print(moto.llantas)
print(moto.color)
print(moto.precio)