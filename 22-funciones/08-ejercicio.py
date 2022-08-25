'''
Escribir una función que calcule el total de una factura tras aplicarle el IVA. 
La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, 
y devolver el total de la factura. Si se invoca la función sin pasarle el 
porcentaje de IVA, deberá aplicar un 16%.
'''

def calculateTax(subtotal, tax = 0.16):
    if tax:
        tax_value = subtotal * tax
        return subtotal + tax_value
    else:
        print('No hay tax')

print(calculateTax(234, None))