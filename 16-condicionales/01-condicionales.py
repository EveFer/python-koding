# Un condicional
# Son situaciones en las que pueden darse varios
# resultados dentro de un programa

# if -> Es la forma de colocar un condicional en python
# significa 'Si..', de condicion

# else -> 'Sino', en dado caso que no compla la condicion en 'if'

# elif -> Se utiliza cuando se combina varias opciones que el programa debe elegir

age_fer = 26

if age_fer >= 18:
    print('Es mayor de edad')
else:
    print('Es menor de Edad')

if age_fer <= 18:
    print('Es menor de Edad D:')
else:
    print('Es mayor de Edad 😎')

hour = 4
# 5 - 11 -> buenos dias
# 12 - 18 -> buenos tardes
# 19 - 23 -> buenas noches
# 00 - 4 -> dejenme dormir

if hour >= 5 and hour <= 11:
    print('Buenos dias')
elif hour >= 12 and hour <= 18:
    print('Buenas tardes')
elif hour >= 19 and hour <= 23:
    print('Buenas noches')
else:
    print('Dejenme dormir')


# condicionales anidados

name = 'Fer'
age = 26

if name == 'Fer':
    if age >= 18:
        print('Eres Fer y Eres mayor de Edad')
    else:
        print('Eres fer pero NO eres Mayor de Edad')
else:
    print('Tu No eres Fer')
