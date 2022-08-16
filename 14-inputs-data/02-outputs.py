# formats

name = input('Ingresa tu nombre: ')
age = int(input('Ingresa tu Edad: '))

output = 'Hola {} tienes {} años'.format(name, age) 

greeting = 'Hola {name} tienes {age} años'.format(name=name, age=age)

print(output)
print(greeting)