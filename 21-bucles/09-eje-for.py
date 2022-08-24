'''
Pedir al usuario que ingrese 2 numeros, después, se debe mostrar el 
rango de esos 2 números, pero, solo imprimiendo los números que sean impares
'''

number_1 = int(input('Ingresa un numero: '))
number_2 = int(input('Ingresa otro numero: '))

for i in range(number_1, number_2 + 1):
    if(i % 2 != 0):
        print(i)

print('----------------------')

for i in range(number_1, number_2 + 1):
    if(i % 2 == 0):
        continue
    print(i)