# tipos de datos básicos en python

# tipo númerico | Número, con o sn decimales  | int, float, complex, no = 3
# tipo de texto | cadena de caracteres        | str = "a literal string"
# tipo Booleano | booleano                    | continue = True

# examples
planets_in_solar_system = 8 # int, pluto used to be the 9th planet, but is too small
distance_to_alpha_centauri = 4.367 # float, lightyears
can_liftoff = True
shuttle_landed_on_the_moon = "Apollo 11" #string 

# Para saber el tipo de dato de una variable utilizar la función type()

type(distance_to_alpha_centauri) ## <class 'float'>


# operadores
# <left side> <operator> <right side>

left_side = 10
right_side = 5
left_side / right_side # 2

# Operadores Aritmeticos
# + |   Operador de suma que suma dos valores juntos    |   1 + 1
# - |   Operador de resta que elimina el valor del lado derecho del lado izquierdo  |   1 - 2
# / |   Operador de división que divide el lado izquierdo tantas veces como especifica el lado derecho  |   10 / 2
# * |   Operador de multiplicación  |   2 * 2

# Operadores de Asignación

# = |   x = 2   |   x ahora contiene 2.
# +=    |   x += 2 |   x incrementado en 2. Si antes contenía 2, ahora tiene un valor de 4.
# -=    |   x -= 2  |   x decrementada en 2. Si antes contenía 2, ahora tiene valor 0.
# /=    |   x /= 2  |   x dividido por 2. Si antes contenía 2, ahora vale 1.
# *=    |   x *= 2  |   x multiplicado por 2. Si antes contenía 2, ahora vale 4.

# Fechas

# Cuando está creando programas, es probable que interactúe con las fechas. Una fecha en un programa generalmente significa tanto la fecha del calendario como la hora.

# Puede usar una fecha en varias aplicaciones, como estos ejemplos:

# Archivo de copia de seguridad: . Usar una fecha como parte del nombre de un archivo de copia de seguridad es una buena manera de indicar cuándo se realizó una copia de seguridad y cuándo se debe volver a realizar.
# Condición: . Es posible que desee llevar una lógica específica cuando hay una fecha determinada.
# Métrica: . Las fechas se utilizan para comprobar el rendimiento del código para (por ejemplo) medir el tiempo que lleva ejecutar una función.
# Para trabajar con una fecha, debe importar el datemódulo:

from datetime import date

print(date.today())
print("Today's date is: " + str(date.today()))