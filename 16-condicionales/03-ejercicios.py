# Ejercicio

# Escribe un programa que pida dos palabras y diga si riman o no. 
# Si coinciden las tres últimas letras tiene que decir que riman. 
# Si coinciden sólo las dos últimas tiene que decir que riman un poco y si no, 
# que no riman.

word_1 = input('Ingresa la primera palabra: ')
word_2 = input('Ingresa la segunda palabra: ')

if len(word_1) >= 3 and len(word_2) >= 3:
    if word_1[-3:] == word_2[-3:]:
        print('Las palabras {} {} SI riman'.format(word_1, word_2))
    elif word_1[-2:] == word_2[-2:]:
        print('Las palabras {} {} riman un POCO'.format(word_1, word_2))
    else:
        print('Las palabras {} {} NO riman'.format(word_1, word_2))
else:
    print('Alguna de las palabras tiene menor de 3 caracteres')

# 

if len(word_1) < 3 or len(word_2) < 3:
    print('No riman, alguna de las palabras tiene menor de 3 caracteres')
elif word_1[-3:] == word_2[-3:]:
    print('Las palabras {} {} SI riman'.format(word_1, word_2))
elif word_1[-2:] == word_2[-2:]:
    print('Las palabras {} {} riman un POCO'.format(word_1, word_2))
else:
    print('Las palabras {} {} NO riman'.format(word_1, word_2))



# Ejercicio

# Crear un programa que permita al usuario elegir un candidato por el cual votar. 
# Las posibilidades son: candidato A por el partido rojo, candidato B por el partido verde, 
# candidato C por el partido azul. Según el candidato elegido (A, B ó C) se 
# le debe imprimir el mensaje “Usted ha votado por el partido 
# [color que corresponda al candidato elegido]”. 
# Si el usuario ingresa una opción que no corresponde a ninguno de los candidatos disponibles, 
# indicar “Opción errónea”.

choice = input('''
Por vota por un candidato:
A) partido rojo
B) partido verde
C) partido azul 
''')

if choice.lower() == 'a':
    print('Usted a votado por el partido Rojo')
elif choice.lower() == 'b':
    print('Usted a votado por el partido Verde')
elif choice.lower() == 'c':
    print('Usted a votado por el partido Azul')
else:
    print('Opción no correcta')


