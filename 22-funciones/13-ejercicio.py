'''
Escribir una función que reciba una muestra de números en una lista y devuelva su media.
'''

def avgNumbers (*numbers):
    total = 0
    for number in numbers:
        total += number
    return total/len(numbers)

print(avgNumbers(10,10,9))