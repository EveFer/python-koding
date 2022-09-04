dictionario = {
    'llave1': 1,
    "llave2": 2,
    "llave3": 3
}

print(dictionario["llave1"])
print(dictionario["llave2"])
print(dictionario["llave3"])

poblacion_paises = {
    'argentina': 44938712,
    'brasil': 210147125,
    'colombia': 50372424
}

for pais in poblacion_paises.keys():
    print(pais)

for poblacion in poblacion_paises.values():
    print(poblacion)

for pais, poblacion in poblacion_paises.items():
    print('{} tiene {} habitantes'.format(pais, poblacion))