'''
Con el siguiente diccionario, debes crear un programa que pregunte
al usuario por un número; el programa debe imprimir el jugador al que hace 
referencia ese número

{
    1 : "Casillas", 
    15 : "Ramos",
    3 : "Pique", 
    5 : "Puyol",
    11 : "Capdevila", 
    14 : "Xabi Alonso",
    16 : "Busquets", 
    8 : "Xavi Hernandez",
    18 : "Pedrito", 
    6 : "Iniesta",
    7 : "Villa"
}
'''

players = {
    1 : "Casillas", 
    15 : "Ramos",
    3 : "Pique", 
    5 : "Puyol",
    11 : "Capdevila", 
    14 : "Xabi Alonso",
    16 : "Busquets", 
    8 : "Xavi Hernandez",
    18 : "Pedrito", 
    6 : "Iniesta",
    7 : "Villa"
}

number_player = int(input('Ingresa el numero de un jugador: '))

if(number_player in players):
    print('El jugador con el numero {} es: {}'.format(number_player, players.get(number_player)))
else:
    print('No se encontro ningun jugador con este numero D:')