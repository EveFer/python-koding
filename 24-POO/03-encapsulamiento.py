# Pilar - Encapsulamiento

# aplicar cierto alcance a los atributos, para que dichos atrubutos sean utilizados
# dentro de la clase
# - Evitar desvordamiento de memoria
# - Evitar ejecuciones innecesarias

class A():
    def __init__(self):
        self.contador = 0
    
    def incrementar(self):
        self.contador += 1
    
    def cuenta(self):
        return self.contador

class B():
    # _ -> encapsular un atributo
    def __init__(self):
        self._contador = 0
    
    def incrementar(self):
        self._contador += 1
    
    def cuenta(self):
        return self._contador

a = A()
print(a.cuenta())
a.incrementar()

print(a.cuenta())

print('atributo contador: ',a.contador) # esto no es una buena práctica -  acceder a los atributos

print('Objeto -> 2')
b = B()

print(b.cuenta())
b.incrementar()
print(b.cuenta())
print(b.__contador) # cuando agregamos un guion bajo lo estamos encapsulando, es decir es, hacerlo privado desde fuera de la clase