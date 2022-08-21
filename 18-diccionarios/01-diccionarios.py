diccionario = {
    'usuario': 'Fernanda',
    'password': '12345',
    'usuario': 'Fernanda'
}

print(diccionario)
print(type(diccionario))

dicti = {
    'name': 'Fernanda',
    'lastName': 'Palacios',
    'age': 26,
    'hobbies': ['Ver anime', 'Programar']
}

# devolver solo las claves
print(dicti.keys())

# devolver solo los valores
print(dicti.values())

# acceder a los valores
print(dicti['name'])

# agregar un nuevo key/value
dicti['work'] = 'Full Stack Developer'

print(dicti)

# modificar un valor

dicti['name'] = 'Evelyn Fernanda'

print(dicti)