'''
Escribir un programa que pida un numero al usuario y 
muestre la tabla de multiplicar de ese numero
'''

number = int(input('Que tabla de multiplcar desea: '))

i = 0

while i <= 10:
    print('{} x {} = {}'.format(i, number, number * i))
    i += 1