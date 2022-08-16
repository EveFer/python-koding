
# Hacer un programa que pida al usuario su nombre, su edad y su genero y 
# los muestre de la siguiente forma:

# Te llamas: <nombre>

# Tu edad es: <edad>

# Eres: <Genero>

name = input('Ingresa tu nombre: ')
age = input('Ingresa tu edad: ')
gender = input('Ingresa tu genero: ')

output = '''
Te llamas: {}
Tu edad es: {}
Eres: {}
'''.format(name, age, gender)

print(output)