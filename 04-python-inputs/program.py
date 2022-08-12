# Recopilar entrada

# 1º Entrada de línea de comandos

# Cuando inicia un programa usando python3, le da el nombre del archivo
#  para iniciar. También puede darle un conjunto de argumentos: 
# datos a los que tendrá acceso el programa cuando se ejecute. 
# Así es como puede verse:

# python3 backup.py 2022-01-01

# Argumentos de la línea de comandos

# ¿Cómo se capturan estos comandos en el lado de la codificación de las cosas? 
# Al usar el sys módulo, puede recuperar los argumentos de la línea de comandos y usarlos en su programa. Mira el siguiente código:

# En el código anterior, la cadena "2021-01-01" se puede usar como instrucción para que el programa inicie una copia de seguridad a partir 
# de esa fecha. Lo que gana al usar argumentos de línea de comandos es flexibilidad; el programa puede comportarse de manera diferente dependiendo de su entrada externa.

import sys

print(sys.argv)
print(sys.argv[0]) # program name
print(sys.argv[1]) # first arg


# 2º Entrada del usuario

# Otra forma de pasar datos al programa es hacer que el usuario ingrese los datos. Puede codificarlo para que el programa le diga al usuario que ingrese información. Guarda los datos ingresados en el programa y luego actúa en consecuencia.

# Para capturar información del usuario, utilizará la input()función. Aquí hay un ejemplo:

print("Welcome to the greeter program")
name = input("Enter your name ")
print("Greetings: " + name)