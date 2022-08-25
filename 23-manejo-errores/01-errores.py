
while True:
    try:
        age = int(input('Ingresa tu edad: '))
        print('Tu edad es: ',age)
        break
    except:
        print('Ingresaste un valor erroneo ')
    finally:
        print('La ejecución a finalizado')