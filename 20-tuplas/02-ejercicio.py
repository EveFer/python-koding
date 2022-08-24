'''
Escribir una tupla con los meses del año, luego, pide al usuario un numero, 
el que haya ingresado, es el mes que debe mostrar en la tupla
'''
months = ('Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre')

input_month_number = int(input('Ingresa el número del més que deseas ver: '))

print('El més que elegiste fue: {}'.format(months[input_month_number - 1]))