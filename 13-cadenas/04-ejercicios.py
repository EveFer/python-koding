# Ejercicio 1

# Crear un programa que tenga una variable con la cadena "Hola todos, bienvenidos", 
# y muestre la siguiente informacion

string = 'Hola a todos, bienvenidos'

# 1.1 imprimir los dos primeros caracteres
print(string[:2])

# 1.2 imprimir los tres ultimos caracteres
print(string[-3:])

# 1.3 imprimir dicha cadena cada dos caracteres. Ej. Si la cadena fuese: 'recta' imprime 'rca'
# [index_initial : index_final: steps]
# sacar un copia de la cadena 
print('recta'[::2])
print(string[::2])

# 1.4 Imprimir la cadena en sentido inverso: 'hola mundo!' -> '!odnum aloh'
print(string[::-1])

# 1.5 imprimir la cadena en un sentido y un sentido inverso: Ej. 'reflejo' -> 'reflejoojelfer' 
print(string + string[::-1])

# Ejercicio 2

# 'separado' -> 's,e,p,a,r,a,d,o
string_2 = 'Separado'
print(string_2.replace('',',')[1:-1])