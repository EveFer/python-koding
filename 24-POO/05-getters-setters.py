class A():
    def __init__(self):
        self._contador = 0
        self._cuenta= 0

    # getters

    # Para lo getter se recomienda llamarlos como su atributo

    @property # esto es un decorador que permitira que este meotodo pueda ser llamado como propiedad
    def cuenta(self):
        return self._cuenta
    
    @property 
    def contador(self):
        return self._contador

    # setters
    @cuenta.setter # decorador que le dice a python  que será un setter
    def cuenta(self, cuenta):
        self._cuenta = cuenta

    @contador.setter
    def contador(self, contador):
        self._contador = contador

    #  si un atributo no cuenta con setter se dice que es only read


a = A()

print(a.cuenta)
print(a.contador)

# setter
a.cuenta = 20
a.contador = 10

print(a.cuenta)
print(a.contador)