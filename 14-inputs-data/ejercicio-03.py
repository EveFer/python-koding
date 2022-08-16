# Ejercicio 1
# Escribir un programa que solicite al usuario un avocal en 
# minuscula, y luego una letra en mayúsculas. El programa 
# debe convertir la letra en minúscula y la vocal en mayúscula, 
# y al final, deben ser concatenadas ambas

vowel = input('Ingresa una Vocal: ')
letter = input('Ingresa cualquier letra: ')

print('{}{}'.format(letter.lower(), vowel.upper()))