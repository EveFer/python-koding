
# diferencias entre una lista y un conjunto
# lista   |  conjunto

conjunto = {1,2,3,4,5}
lista = [1,2,2,3,4,5,4,5]

# print(lista)
print(conjunto)
print(type(conjunto))

# Conjunto, no permite datos repetidos
# lista, si permite datos repetidos

conjunto.add(20)

print(conjunto)

conjunto.remove(1)
conjunto.discard(3)
print(conjunto)

# elimina el primero
conjunto.pop()
print(conjunto)

# añadir elementos iterables
conjunto.update([1,2,3])
print(conjunto)

# clear()

conjunto.clear()
print(conjunto)