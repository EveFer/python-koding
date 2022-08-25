
class Telefono():

    # cuando se manda un parametro con un * lo recibe como tupla
    # cuando se manda un parametro con un ** lo recibe como diccionarios
    def __init__(self, marca, *colores, **modelos):
        self.marca = marca
        self.colores = colores
        self.modelos = modelos
    

tel = Telefono('Alcatel', 'Negro', 'Rosa', 'Verde', m1= 500, m2= 1000)

print(tel.marca)
print(tel.colores)
print(tel.modelos)

# atributos temporales
tel.memoria = 512
print(tel.memoria)