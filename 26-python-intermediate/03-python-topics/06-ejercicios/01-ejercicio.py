from functools import reduce

DATA = [
    {
        'name': 'Fernanda',
        'age': 26,
        'organization': 'Kodemia',
        'position': 'Program Lead',
        'language': 'JavaScript',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'BBVA',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Kodemia',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Toroto',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

def run():
    # list comprehension

    # Obtener todos los workers que sepan python
    all_python_devs = [worker for worker in DATA if worker['language'] == 'python']
    all_python_devs_names = [worker['name'] for worker in DATA if worker['language'] == 'python']

    # print(all_python_devs)
    # print(all_python_devs_names)

    # todos los trabajadores de Kodemia
    all_kodemia_workers = [worker for worker in DATA if worker['organization'] == 'Kodemia']
    all_kodemia_workers_names = [worker['name'] for worker in DATA if worker['organization'] == 'Kodemia']
    # print(all_kodemia_workers)
    # print(all_kodemia_workers_names)

    # obtener los adultos mayores a 18
    adults_list = [worker['name'] for worker in DATA if worker['age'] > 18]
    # print(adults_list)

    # # Nueva lista que agregue un llave 'old a todos los dict si la edad es > 50

    old_people_list = [worker | {'old': worker['age'] > 50} for worker in DATA]
    # print(old_people_list)

    # =================== filter | map =================
    # Obtener todos los workers que sepan python

    all_python_developers = list(filter(lambda worker: worker['language'] == 'python', DATA))
    # print(all_python_developers)


    # todos los trabajadores de Kodemia
    all_workers_kodemia = list(filter(lambda worker: worker['organization'] == 'Kodemia', DATA))
    # print(all_workers_kodemia)


    # Obtener los adultos mayores a 18
    adults = list(filter(lambda worker: worker['age'] > 18, DATA))
    adults = list(map(lambda worker: worker['name'], adults))
    # print(adults)

    # Nueva lista que agregue un llave 'old a todos los dict si la edad es > 50
    # El simbolo '|' es un pipe que dentro de python nos permite es unificar dos diccionarios
    # Es un nuevo feature para la version 3.9 en adelante
    old_people = list(map(lambda worker: worker | {'old': worker['age'] > 50}, DATA))
    # print(old_people)

    # Obtener la edad promedio de los trabajadores
    
    age_average = reduce(lambda accum, workerCurrent: accum + workerCurrent['age'], DATA, 0) / len(DATA)
    print('La edad promedio es: ', age_average)

if __name__ == '__main__':
    run()