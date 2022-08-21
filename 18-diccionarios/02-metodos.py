dicci = {
    1:2,
    2:3,
    3:4
}

print(dicci)

# eliminar una clave pop(''claveName)
dicci.pop(1)

print(dicci)

# limpiar un diccionario
dicci.clear()

print(dicci)

# obtener datos por metodo
# dicci.get(2)
data = dicci.get(2)
print(data)
print(dicci.get(3))

person = {
    'name': 'Fernanda'
}

print(person.get('name'))

# agregar valores

# setdefault(key, value)

person.setdefault('lastName', 'Palacios')

print(person)

# Actualizar un valor

# update(key, value)

person.update({'name': 'Evelyn Fernanda'})

print(person)

# .copy()