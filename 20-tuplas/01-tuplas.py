# Es una lista que no de puede modificar
# Es inmutable

# No tiene métodos

# sintaxis
# () -> no es obligatoio
# 

tupla = (1,2,3,4,5)
tupla_1 = 6,7,8,9,10

print(tupla)
print(type(tupla))

print(tupla_1)
print(type(tupla_1))

# acceder a un elemento

print(tupla[2])

# segmatado de tuplas
print(tupla[0:3])

# suma
print(tupla + tupla_1)

# no modificar
# Marca Error
tupla[2] = 'hola'
print(tupla)