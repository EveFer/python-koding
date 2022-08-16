# coding=utf-8
#  una cadena es una secuencia de caracteres
# La cadena de caracteres tienen posiciones cada caracter
# iniciando en 0
# hola mundo
# 0123456789

# Debandado de Cadena - segmentación de cadenas

# hola mundo
# 0123456789

# [0:5] = "hola " [index_initial:index_final (no lo incluye)]
# [:3] = ""  [:index_final] desde el indice 0 al indice final (no lo incluye)
# [3:] = ""  Obtiene a partir del indice incial al resto de la cadena

string = 'hola mundo'

print(string[0:3])
print(string[:8])
print(string[1:]) 

# string literal | escapar carcateres
cadena = 'Esto es una "cadena" \'de\' texto \n en otra linea'
# \n salto de linea
# \t tabulador
# \f
# \b elimina un espacio
# \v
print(cadena)

# operadores aritmeticos con strings

string_1 = 'Fernanda'
string_2 = ' Bienvenida'
number = 1

print(string_1 + string_2) # concatenacion 
print(string_1 * 3)
# print(string_1 - 3)

message = "Hola usuario: " + string_1
print(number, ' Hola usuario: ', string_1)

print(str(number) + string_1)




