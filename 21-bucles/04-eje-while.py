'''
Escribir un programa que pregunte al usuario su edad y muestre 
por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
'''

name = input('Cual es tu nombre: ')
age = int(input('Cual es tu edad: '))

i = 1
while i <= age:
    print('{}'.format(i))
    i += 1