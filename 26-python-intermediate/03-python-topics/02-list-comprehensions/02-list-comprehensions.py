# Crear un lista con los 10 primeros numeros al cuadrado y que no sean divisibles entre 3

def run():
    list_numbers = []

    for number in range(101):
        if number % 3 != 0:
            number_square = number ** 2
            list_numbers.append(number_square)
    print(list_numbers)

    print('------')
    # with list comprehensions
    # Un list comprehension es una estructura en python que nos permite crear
    # nuevas listas
    # [element for element in iterable if condition]

    # [] -> lista
    # element -> Representa a cada uno de los elementos a poner en la nueva lista
    # for element in iterable -> Ciclo a partir del cual se extraerán elementos de otra lista o cualquier iterable
    # if condition (opcional)-> Condicion opcional para filtrar los elementos del ciclo

    # como se Lee:
    # Primero enmedio
    # elemento
    # condiconal
    '''
     -> Para cada elemento en el iterable, ese elemento solo si se cumple la condicion
    '''

    squares = [number**2 for number in range(1, 101) if number % 3 != 0 ]
    print('squares', squares)

    

if __name__ == '__main__':
    run()