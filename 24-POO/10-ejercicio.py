'''
Realizar un programa que conste de una clase llamada Estudiante, 
que tenga como atributos el nombre y la nota del alumno. 
Definir los métodos para inicializar sus atributos, imprimirlos y 
mostrar un mensaje con el resultado de la nota y si ha aprobado o no.
'''

class Student():
    def __init__(self, name, note):
        self._name = name
        self._note = note

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name

    @property
    def note(self):
        return self._note

    @note.setter
    def note(self, note):
        self._note = note

    def printNote(self):
        if self._note > 6:
            print('Hola {}, Tu nota es {} y has aprobado'.format(self._name, self._note))
        else:
            print('Hola {}, Tu nota es {} y NO has aprobado'.format(self._name, self._note))


student = Student('Fernanda', 9)

student.printNote()