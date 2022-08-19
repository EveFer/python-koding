# Ejercicio 1

# Crear un programa que pida al usuario una letra, y si es vocal, muestre el 
# mensaje "Es vocal". Sino, decirle al usuario que no es vocal

from curses.ascii import islower


letter = input('Ingresa una letra: ')

if letter.lower() == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
    print('{} es vocal'.format(letter))
else:
    print('No es vocal')

# option 2
# in -> esta en
if letter.lower() in 'aeiou':
    print('Es Vocal')
else:
    print('No es Vocal')

# Ejercicio 2

# Escribir un programa que, dado un número entero, muestre su valor absoluto. 
# Nota: para los números positivos su valor absoluto es igual al número 
# (el valor absoluto de 52 es 52), mientras que, para los negativos, 
# su valor absoluto es el número multiplicado por -1 (el valor absoluto de -52 es 52).

number = int(input('Ingresa un numero entero: '))

print('El valor absoluto de {} es {}'.format(number, abs(number)))

if number > 0:
    print('El valor absoluto de {} es: {}'.format(number, number))
else:
    print('El valor absoluto de {} es: {}'.format(number, str(number*-1)))