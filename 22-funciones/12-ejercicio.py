'''
Crear un programa que tenga dos funciones, una que contenga el area de un 
cuadrado con argumento el lado; y la otra el area de un circulo 
con argumento de radio
'''

def areaSquare(base):
    return base * base

def areaCircle(radio):
    return 3.1415 * (radio**2)


print(areaSquare(10))
print(areaCircle(8))