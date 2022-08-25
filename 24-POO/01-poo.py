

class Telefono():

    # este metodo se ejecuta cuando se instancia un objeto
    # __init__ -> es un metodo constructor
    def __init__(self, marca, color,memoria_ram, almacenamiento):
        self.marca = marca
        self.color = color
        self.memoria_ram = memoria_ram
        self.almacenamiento = almacenamiento

        print('El objeto ha {} sido creado'.format(self.marca))

    # metodos - recibe self
    def llamar(self, num_tel):
        return 'llamando a {}'.format(num_tel)

    def reproducir_music(self):
        return 'Reproduciendo la musica'

    # self -> Hace referencia a si mismo

    def elaborarHuawei(self):
        self.marca = 'Sansumg'

    # metodos especiales 

    # Para describir el formato del objeto
    def __str__(self):  
        return 'El objeto es {}'.format(self.marca)

    # destructor -> se ejecuta al finalizar | destrutir -> es automatico
    def __del__(self):
        print('El objeto {} ha sido destruido'.format(self.marca))



print(type(Telefono))

# crear objetos a partir de classes

celular = Telefono('Samsung', 'plateado', 32, 128)

print(type(celular))
print(celular) # muestra es espacio en memoria
print(celular.marca)
print(celular.llamar('9672939283'))
print(celular.reproducir_music())