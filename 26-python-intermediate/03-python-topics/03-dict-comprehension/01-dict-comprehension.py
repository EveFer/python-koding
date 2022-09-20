'''
Crear un diccionario cuya llaves sean
los primero 100 numeros y cuyos valores sean esos
numero elevados al cubo
'''

def run():
    dict_nums = {}

    for number in range(1, 101):
        if number % 3 != 0:
            dict_nums[number] = number**3
    
    print(dict_nums)

    # With comprehension
    print('------- dict comprehension -------')
    # {key: value for value in iterable if condition}

    my_dict = {num: num**3 for num in range(1,101) if num % 3 != 0}

    # key: value -> Representa a cada una de las llaves y valores a poner en el nuevo diccionario
    # for value in iterable -> Ciclo apartir del cual se extraerán elementos de cualquier iterable
    # if condition -> condicion opcional para filtrar los elementos del ciclo

    # Como se lee:
    # Para cada elemento en cada iterable voy a colocar una clave:valor al diccionario siempre y cumpla la condicion

    


    print(my_dict)

if __name__ == '__main__':
    run()