'''
Escribir una función que reciba un número entero positivo y devuelva su factorial.
'''

def factorial(number):
    total = 1
    for i in range(1, number + 1):
        total *= i
    return total

print('El Faltorial de 7 es: ',factorial(7))