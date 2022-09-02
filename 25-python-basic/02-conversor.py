# conversor de modenas

# de pesos mexicanos  dolares

def conversion(type, value):
        value_usd = 19.9448
        if type == 'usd':
            return round(value / value_usd, 4)
        elif type == 'mxn':
            return round(value * value_usd, 4)
        else:
            return 'No se encuentra esta opcion'

try:
    while True:
        choice = int(input('''
Selecciona que tipo de conversion deseas realizar:
[1] - MXN -> USD
[2] - USD -> MXN 
'''))

        if choice == 1:
            mxn = float(input('Ingresa el valode en MXN: '))
            usd = conversion('usd', mxn)
            print('El valor de ${} MXN es igual a ${} USD'.format(mxn, usd))
        else:
            usd = float(input('Ingresa el valode en USD: '))
            mxn = conversion('mxn', usd)
            print('El valor de ${} USD es igual a ${} MXN'.format(usd, mxn))
except KeyboardInterrupt:
    print('Se ah terminado :D')




