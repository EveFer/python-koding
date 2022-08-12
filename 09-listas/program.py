# Presentación de listas

# Python tiene muchos tipos integrados, como cadenas y enteros. 
# También tiene un tipo para almacenar una colección de valores: la lista.

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

# Acceso a elementos de lista por índice

print("The first planet is", planets[0])
print("The second planet is", planets[1])
print("The third planet is", planets[2])

# Output
# The first planet is Mercury
# The second planet is Venus
# The third planet is Earth

# Determinación de la longitud de una lista

# Para obtener la longitud de una lista, use la función integrada len(). 
# El código siguiente crea una variable, number_of_planets. 
# El código asigna esa variable con el número de elementos de la lista planets (8).

number_of_planets = len(planets)
print("There are", number_of_planets, "planets in the solar system.")

# Output:
# There are 8 planets in the solar system



# Incorporación de valores a listas
# Las listas de Python son dinámicas: puede agregar y quitar elementos después de crearlas. 
# Para agregar un elemento a una lista, use el método .append(value).
planets.append("Pluto")
number_of_planets = len(planets)
print("There are actually", number_of_planets, "planets in the solar system.")

# Output:
# There are actually 9 planets in the solar system.

# Eliminación de valores de listas
# Puede quitar el último elemento de una lista llamando al método .pop() en la variable de lista:
planets.pop()  # Goodbye, Pluto
number_of_planets = len(planets)
print("No, there are definitely", number_of_planets, "planets in the solar system.")


# Uso de índices negativos
# Ha visto cómo usar índices para capturar un elemento individual en una lista:
print("The first planet is", planets[0])

# Output:
# The first planet is Mercury

# Los índices comienzan en cero y van en aumento. Los índices negativos comienzan al 
# final de la lista y van hacia atrás.

# En el ejemplo siguiente, un índice de -1 devuelve el último elemento de una lista. 
# Un índice de -2 devuelve el penúltimo
print("The last planet is", planets[-1])
print("The penultimate planet is", planets[-2])

# Output
# The last planet is Neptune
# The penultimate planet is Uranus

# Si quisiera devolver el antepenúltimo, usaría un índice de -3 (y así sucesivamente).


# Búsqueda de un valor en una lista
# Para determinar dónde se almacena un valor en una lista, use el método index 
# de la lista. Este método busca el valor y devuelve el índice de ese 
# elemento en la lista. Si no encuentra ninguna coincidencia, devuelve -1.

# En el ejemplo siguiente se muestra el uso de "Jupiter" como el valor del índice:
jupiter_index = planets.index("Jupiter")
print("Jupiter is the", jupiter_index + 1, "planet from the sun")

# Output
# Jupiter is the 5 planet from the sun


# Almacenamiento de números en listas

gravity_on_earth = 1.0
gravity_on_the_moon = 0.166

# El código siguiente crea una lista en la que se muestran las fuerzas de los ocho planetas del sistema solar, en G:
gravity_on_planets = [0.378, 0.907, 1, 0.377, 2.36, 0.916, 0.889, 1.12]

# En esta lista, gravity_on_planets[0] es la gravedad en Mercurio (0,378 G), 
# gravity_on_planets[1] es la gravedad en Venus (0,907 G), y así sucesivamente.

# En la Tierra, un autobús de dos pisos pesa 12 650 kilogramos (kg), es decir, 
# 12,65 toneladas. En Mercurio, donde la gravedad es de 0,378 G, el mismo autobús 
# pesa 12,65 toneladas multiplicado por 0,378. En Python, para multiplicar dos valores, 
# se usa el símbolo *.

# En el ejemplo siguiente, puede averiguar el peso de un autobús de dos pisos en 
# diferentes planetas obteniendo el valor de la lista:

bus_weight = 12650 # in kilograms, on Earth

print("On Earth, a double-decker bus weighs", bus_weight, "kg")
print("On Mercury, a double-decker bus weighs", bus_weight * gravity_on_planets[0], "kg")

# Output
# On Earth, a double-decker bus weighs 12650 kg
# On Mercury, a double-decker bus weighs 4781.7 kg

# Uso de min() y max() con listas

# Python tiene funciones integradas para calcular los números más grandes y más 
# pequeños de una lista. La función max() devuelve el número más grande y min() 
# devuelve el más pequeño. Por lo tanto, min(gravity_on_planets) devuelve el 
# número más pequeño de la lista gravity_on_planets, que es 0,377 (Marte).

# El código siguiente calcula los pesos mínimo y máximo en el sistema solar 
# mediante esas funciones:
bus_weight = 12650 # in kilograms, on Earth

print("On Earth, a double-decker bus weighs", bus_weight, "kg")
print("The lightest a bus would be in the solar system is", bus_weight * min(gravity_on_planets), "kg")
print("The heaviest a bus would be in the solar system is", bus_weight * max(gravity_on_planets), "kg")

# Output
# On Earth, a double-decker bus weighs 12650 kg
# The lightest a bus would be in the solar system is 4769.05 kg
# The heaviest a bus would be in the solar system is 29854 kg


# Manipulación de datos de la lista
# Es posible que tenga que trabajar con distintas partes de una lista. Por ejemplo, 
# suponga que tiene una lista con cantidades de precipitaciones durante varios meses. 
# Para analizar correctamente este tipo de datos, es posible que tenga que buscar las 
# precipitaciones en otoño o en un periodo de tres meses. También puede que quiera 
# ordenar la lista de mayor a menor cantidad de precipitaciones.

# Python proporciona una compatibilidad sólida para trabajar con los datos de las listas. 
# Esta compatibilidad incluye la segmentación de datos (examinando solo una parte) y 
# la ordenación.

# Segmentación de listas
# Puede recuperar una parte de una lista mediante una segmentación. Una segmentación 
# usa corchetes, pero en lugar de un solo elemento, tiene los índices inicial y final. 
# Cuando se usa una segmentación, se crea una lista que comienza en el índice inicial 
# y termina antes del índice final (y no lo incluye).

# La lista de planetas tiene ocho elementos. La Tierra es el tercero de la lista. 
# Para mostrar los planetas que hay antes de la Tierra, use una segmentación a fin 
# de obtener los elementos que empiezan en 0 y terminan en 2:
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
planets_before_earth = planets[0:2]
print(planets_before_earth)

# Output: ['Mercury', 'Venus']

# Observe cómo la Tierra no está incluida en la lista. El motivo es que el índice 
# finaliza antes del índice final.
# Para obtener todos los planetas después de la Tierra, comience en el tercero 
# y vaya hasta el octavo:
planets_after_earth = planets[3:8]
print(planets_after_earth) 

# Output
# ['Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

# En este ejemplo, se muestra Neptuno. La razón es que el índice de Neptuno es 7, 
# porque la indexación comienza en 0. Dado que el índice final era 8, incluye el 
# último valor. Si no coloca el índice de detención en la segmentación, 
# Python asume que quiere ir al final de la lista:

planets_after_earth = planets[3:]
print(planets_after_earth)

# Output
# ['Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

# Una segmentación crea una lista nueva. No modifica la lista actual.


# Ordenación de listas
# Para ordenar una lista, use el método .sort() de la lista. Python ordenará 
# una lista de cadenas en orden alfabético y una lista de números en orden numérico:
regular_satellite_moons = []
regular_satellite_moons.sort()
print("The regular satellite moons of Jupiter are", regular_satellite_moons)

# Output
# The regular satellite moons of Jupiter are ['Adrastea', 'Amalthea', 'Callisto', 'Europa', 'Ganymede', 'Io', 'Metis', 'Thebe']

# Para ordenar una lista en orden inverso, llame a .sort(reverse=True) en la lista:

regular_satellite_moons.sort(reverse=True)
print("The regular satellite moons of Jupiter are", regular_satellite_moons)

# Output
# The regular satellite moons of Jupiter are ['Thebe', 'Metis', 'Io', 'Ganymede', 'Europa', 'Callisto', 'Amalthea', 'Adrastea']

# El uso de sort modifica la lista actual.

