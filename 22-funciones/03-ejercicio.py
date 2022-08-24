'''
Crear un programa que tenga una lista, luego crear una funcion 
con la cual se van a pedir numeros al usuario para agregar a la lista. 
Debes crear una segunda funcion en donde se ordenen los numeros pares e 
impares dentro de dos listas nuevas
'''

list_numbers = []
list_numbers_pares = []
list_numbers_impares = []

def add_numbers():
    quantity = int(input('cuantos numeros deseas agregar: '))
    for i in range(1, quantity + 1):
        number_to_add = float(input('Ingresa el {}º numero: '.format(i)))
        list_numbers.append(number_to_add)

def sort_list_numbers():
    list_numbers.sort()
    for number in list_numbers:
        if number % 2 == 0:
            list_numbers_pares.append(number)
        else:
            list_numbers_impares.append(number)

add_numbers()

print('Lista de numeros: ',list_numbers)

sort_list_numbers()
print('Lista de numeros impares: ',list_numbers_impares)
print('Lista de numeros pares: ',list_numbers_pares)