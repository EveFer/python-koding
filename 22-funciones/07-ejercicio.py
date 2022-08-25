'''
Crear una funcion que pida dos numeros. Si el primero es mayor al segundo, 
el programa debe retornar el valor 1; si el segundo es mayor al primero, 
debe retornar -1; si ambos son iguales, debe retornar 0
'''

def compareNumbers() :
    number_1 = float(input('Ingresa el 1º numero: '))
    number_2 = float(input('Ingresa el 2º numero: '))
    if number_1 > number_2 :
        return 1
    elif number_2 > number_1 :
        return -1
    else:
        return 0

print(compareNumbers())