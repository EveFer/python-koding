
while True:
    try:
        num1 = int(input('Ingresa un numero: '))
        result = 100/num1
        break
    except ZeroDivisionError:
        print('No se puede dividir entre cero')


while True:
    try:
        age = input('Ingresa tu edad: ')
        print('Tu edad es: ', age)
        break
    except ValueError:
        print('Has colocado un valor Erroneo')
    except KeyboardInterrupt:
        print('Has cancelado la ejecucion')
        break