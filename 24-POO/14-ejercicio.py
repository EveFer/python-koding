'''
Crear un programa con tres clases Universidad, con atributos nombre 
(Donde se almacena el nombre de la Universidad). Otra llamada Carerra, 
con los atributos especialidad (En donde me guarda la especialidad de un estudiante). 
Una ultima llamada Estudiante, que tenga como atributos su nombre y edad. 
El programa debe imprimir la especialidad, edad, nombre y universidad de 
dicho estudiante con un objeto llamado persona.
'''

class University():
    def __init__(self, name):
        self._university = name

class Carer():
    def __init__(self, specialization):
        self._specialization = specialization

class Student(University):
    def __init__(self,university, name, age):
        super().__init__(university)
        self._name = name
        self._age = age
    
    def __str__(self):
        return '{} estudia en {} y tiene {} años'.format(self._name, self._university, self._age)



person = Student('ITTG',  'Fernanda Palacios', 26)

print(person)