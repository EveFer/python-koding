from math import sqrt

# Formula General: () / ()

# 3x^2 - 5 x + 2 = 9  x = 1 x = 2/3

value_a = int(input('Ingrese el valor de "a": '))
value_b = int(input('Ingrese el valor de "b": '))
value_c = int(input('Ingrese el valor de "c": '))

# Si el resultado de la operación (b^2 - 4ac) es negativo no es posible obtener la raiz cuadrada de un valor netativo

value_x1 = 0
value_x2 = 0

operation = (value_b ** 2) - (4*value_a*value_c)

if operation > 0:
    value_x1 = (-value_b + (sqrt(operation))) / (2*value_a)
    value_x2 = (-value_b - (sqrt(operation))) / (2*value_a)
    print('x1: ', value_x1) 
    print('x2: ', value_x2) 
else: 
    print('No es posible obtener los valores de x')

