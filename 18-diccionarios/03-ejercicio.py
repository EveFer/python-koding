'''
En el siguiente diccionario se encuentran capitales de los paises en el mundo, 
debes realizar un programa que pida un pais al usuario, y muestre la capital 
de ese pais, en dado caso el pais no este en el diccionario, se debe mostrar 
un mensaje diciendo que ese pais no se encuentra.

{"Guatemala": "Ciudad de Guatemala", "El Salvador": "San Salvador", "Honduras": "Honduras","Nicaragua": "Managua", "Costa Rica": "San Jose", "Panama": "Panama", "Argentina": "Buenos Aires", "Colombia": "Bogota", "Venezuela": "Caracas", "España": "Madrid"}
'''

countries = {
    "Guatemala": "Ciudad de Guatemala", 
    "El Salvador": "San Salvador", 
    "Honduras": "Honduras",
    "Nicaragua": "Managua", 
    "Costa Rica": "San Jose",
    "Panama": "Panama", 
    "Argentina": "Buenos Aires", 
    "Colombia": "Bogota", 
    "Venezuela": "Caracas", 
    "España": "Madrid"
}

country_input = input('Ingresa el país para obtener su capital: ')

if(country_input in countries.keys()):
    print('La capital de {} es: {}'.format(country_input, countries[country_input]))
else:
    print('No se encontro la capital de este país')
