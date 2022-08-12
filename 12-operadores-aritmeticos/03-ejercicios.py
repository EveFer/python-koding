# coding=utf-8
# Ejercicio 1

# Escribir un programa que realice la siguiente operación aritmética:
print('Ejercicio 1')
operation = ((3+2) / (2*5))**2
print(operation)

calculo = pow(((3+2)/(2*5)),2)
print(calculo)

# Ejercicio 2

# Una juguetería tiene mucho éxito en dos de sus productos: 
# payasos y muñecas. Suele hacer venta por correo y la empresa 
# de logística les cobra por peso de cada paquete, así que 
# deben calcular el peso de los payasos y muñecas que 
# saldrán en cada paquete a demanda. Cada payaso pesa 
# 112 g y cada muñeca 75 g. Un cliente frecuente pide la 
# cantidad de 23 payasos y 54 muñecas, realiza un programa
#  que muestre el peso total de toda la venta.

weight_clown=112
weight_wrist=75

quantity_clown = 23
quantity_wrist= 54

total_weight = (weight_clown * quantity_clown)+(weight_wrist * quantity_wrist)
print('El peso total es: ', total_weight)