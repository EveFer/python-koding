'''
Escribir una función que reciba un número entero positivo y devuelva su factorial.
'''

import math


def factorial(number):
    if number > 0:
        total = 1
        for i in range(1, number + 1):
            total *= i
        return total
    else:
        print('El numero no es positivo')

print('El Faltorial de 7 es: ',factorial(7))

def factorial_two(number):
    if number > 0:
        return math.factorial(number)
    else:
        print('El numero no es positivo')

print('El Faltorial de 5 es: ',factorial_two(5))