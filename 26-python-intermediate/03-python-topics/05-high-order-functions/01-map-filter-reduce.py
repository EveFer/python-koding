# Una funcion de orden superior
# Es aquella que recibe como parametro a otra funcion

# 

def saludo(func):
    func()

def hola():
    print('Hola!')

def adios():
    print('Adios!!')

saludo(hola)
saludo(adios)

# Filter

# Filtrar de una lista los numeros impares

my_list = [1,4,5,6,9,19,21]

# cons list comprehension
odd = [num for num in my_list if num % 2 != 0]
print(odd)


# Filter
odd_filter = list(filter(lambda num: num % 2 !=0, my_list))
print(odd_filter)


# Map
# Elevar todos los numeros al cuadrado

squares = [num**2 for num in my_list]
print(squares)

squares_map = list(map(lambda num: num**2, my_list))
print(squares_map)


# Reduce

# [2,2,2,2,2] -> 32

numbers = [2,2,2,2,2]

all_multiplied = 1

for num in numbers:
    all_multiplied *= num

print(all_multiplied)

# with reduce

from functools import reduce

numbers_multiplied = reduce(lambda num1, num2: num1 * num2, numbers)
print(numbers_multiplied)


