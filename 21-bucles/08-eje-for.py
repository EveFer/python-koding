'''
Imprimir por pantalla los numeros del 1 al 10, luego, pedir al usuario 
dos numeros y mostrar el rango de numeros entre ambas cifras
'''

for i in range(1,11):
    print(i)

number_1 = int(input('Ingresa un numero: '))
number_2 = int(input('Ingresa otro numero: '))

print('El rango de numeros es:')
if number_1 < number_2:
    for j in range(number_1, number_2):
        print(j)
else:
    print('ohhh algo salio mal D:')