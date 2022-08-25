'''
Realizar un programa en el cual se declaren dos valores enteros 
por teclado utilizando el método __init__. Calcular después la suma, 
resta, multiplicación y división. Utilizar un método para cada una e 
imprimir los resultados obtenidos. Llamar a la clase Calculadora.
'''

class Calculator():
    def __init__(self):
        self._num1 = float(input('Ingresa el 1º numero: '))
        self._num2 = float(input('Ingresa el 2º numero: '))

    def sum(self):
        return self._num1 + self._num2
    
    def subtract(self):
        return self._num1 - self._num2
    
    def product(self):
        return self._num1 * self._num2
    
    def divide(self):
        return self._num1 / self._num2


calculator = Calculator()

print(calculator.sum())
print(calculator.subtract())
print(calculator.product())
print(calculator.divide())