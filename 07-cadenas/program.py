# Inmutabilidad de las cadenas

# En Python, las cadenas son inmutables. Es decir, no pueden cambiar. 
# Esta propiedad del tipo de cadena puede ser sorprendente, ya que
#  Python no proporciona errores al modificar cadenas.

# Métodos de cadena en Python

# .title()
heading = "temperatures and facts about the moon"

print(heading.title()) # Temperatures And Facts About The Moon

# División de una cadena
# Un método de cadena común es .split(). Sin argumentos, el método separará la cadena en 
# cada espacio. Esto crearía una lista de todas las palabras o números separados por un
# espacio:

temperatures = """Daylight: 260 F
... Nighttime: -280 F"""
print(temperatures.split()) #['Daylight:', '260', 'F', 'Nighttime:', '-280', 'F']

# Búsqueda de una cadena

# in
"Moon" in "This text will describe facts and challenges with space travel" # False
"Moon" in "This text will describe facts about the Moon" # True

# .find()
temperatures = """Saturn has a daytime temperature of -170 degrees Celsius,
... while Mars has -28 Celsius."""

temperatures.find("Moon") # -1

# El método .find() devuelve -1 cuando no se encuentra la palabra, o 
# bien devuelve el índice (el número que representa la posición en 
# la cadena). Así es como se comportaría si busca la palabra Mars:

temperatures.find("Mars") #65

# .count()

# Otra manera de buscar contenido consiste en usar el método .count(), 
# que devuelve el número total de repeticiones de una palabra determinada en una cadena:

temperatures.count("Mars") # 1
temperatures.count("Moon") # 0


# .lower()
# Las cadenas en Python distinguen mayúsculas de minúsculas, lo que significa 
# que Luna y luna se consideran palabras diferentes. Para realizar una comparación 
# sin distinguir mayúsculas de minúsculas, puede convertir una cadena en letras 
# minúsculas mediante el método .lower():

"The Moon And The Earth".lower() # 'the moon and the earth'

# .upper()

"The Moon And The Earth".upper() # 'THE MOON AND THE EARTH'


# Comprobación del contenido

mars_temperature = "The highest temperature on Mars is about 30 C"
for item in mars_temperature.split():
     if item.isnumeric():
        print(item)

# .isnumeric(), .isdecimal()

# Le sorprenderá saber que "-70".isnumeric() devolverá False. 
# Esto se debe a que todos los caracteres de la cadena tendrían que ser 
# numéricos y el guión (-) no lo es. Si tiene que comprobar números negativos
#  en una cadena, el método .isnumeric() no funcionará.

"-60".startswith('-') # True

if "30 C".endswith("C"):
    print("This temperature is in Celsius")

# .join()

moon_facts = ["The Moon is drifting away from the Earth.", "On average, the Moon is moving about 4cm every year"]
'\n'.join(moon_facts)


# Formato de cadenas en Python

# Formato de signo de porcentaje (%)

# El marcador de posición es %s, y la variable se pasa al 
# texto después del carácter % fuera de la cadena. Aquí 
# se muestra cómo dar formato mediante el carácter %:
mass_percentage = "1/6"
print("On the Moon, you would weigh about %s of your weight on Earth" % mass_percentage) #On the Moon, you would weigh about 1/6 of your weight on Earth

# El uso de varios valores cambia la sintaxis, ya que se necesitan 
# paréntesis para rodear las variables que se pasan:

print("""Both sides of the %s get the same amount of sunlight,
... but only one side is seen from %s because
... the %s rotates around its own axis when it orbits %s.""" % ("Moon", "Earth", "Moon", "Earth"))
# Both sides of the Moon get the same amount of sunlight,
# but only one side is seen from Earth because
# the Moon rotates around its own axis when it orbits Earth.

# El método format()

# El método .format() usa llaves ({}) como marcadores de posición 
# dentro de una cadena y utiliza la asignación de variables para reemplazar texto.

mass_percentage = "1/6"
print("On the Moon, you would weigh about {} of your weight on Earth".format(mass_percentage))
# On the Moon, you would weigh about 1/6 of your weight on Earth

print("""You are lighter on the {0}, because on the {0} 
... you would weigh about {1} of your weight on Earth""".format("Moon", mass_percentage))
# You are lighter on the Moon, because on the Moon you would weigh about 1/6 of your weight on Earth

print("""You are lighter on the {moon}, because on the {moon} 
... you would weigh about {mass} of your weight on Earth""".format(moon="Moon", mass=mass_percentage))
# You are lighter on the Moon, because on the Moon you would weigh about 1/6 of your weight on Earth

# Acerca de las cadenas f-strings

# A partir de la versión 3.6 de Python, es posible usar f-strings. 
# Estas cadenas son como plantillas con las mismas variables con 
# nombre que las del código. El uso de f-strings en el ejemplo anterior 
# tendría el siguiente aspecto:

print(f"On the Moon, you would weigh about {mass_percentage} of your weight on Earth")
# On the Moon, you would weigh about 1/6 of your weight on Earth

print(f"On the Moon, you would weigh about {round(100/6, 1)}% of your weight on Earth")
# On the Moon, you would weigh about 16.7% of your weight on Earth

subject = "interesting facts about the moon"
f"{subject.title()}"
# 'Interesting Facts About The Moon'