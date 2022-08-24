'''
Escribir una tupla que tenga las letras del alfabeto. Luego, debes pedir al 
usuario un numero, el que haya ingresado, es la letra que debe imprimir el programa
'''

alphabet = 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'

input_letter = int(input('Ingresa el numero de la letra que deseas ver: '))

print('La letra es: {}'.format(alphabet[input_letter - 1]))