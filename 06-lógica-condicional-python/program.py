
# Operadores Lógicos
# Es igual que: a == b
# No es igual a: a != b
# Menor que: a < b
# Menor o igual que: a <= b
# Mayor que: a > b
# Mayor o igual que: a >= b

# En Python, None y 0 también se interpretan como False.

a = 97
b = 55
# test expression
if a > b:
    print("a is greater than b")
elif a < b:
    print("a is less than b")
else: 
    print ("a is equal to b")  

# if test_expression:
#     # statement(s) to be run
# elif test_expression:
#     # statement(s) to be run
# elif test_expression:
#     # statement(s) to be run
# else:
#     # statement(s) to be run 

# Uso de lógica condicional anidada

a = 16
b = 25
c = 27
if a > b:
    if b > c:
        print ("a is greater than b and b is greater than c")
    else: 
        print ("a is greater than b and less than c")
elif a == b:
    print ("a is equal to b")
else:
    print ("a is less than b")

# 
object_size = 10
if object_size > 5:
    print('We need to keep an eye on this object')
else:
    print('Object poses no threat.')


# Operadores and or

a = 23
b = 34
if a == 34 or b == 34:
    print(a + b)

a = 23
b = 34
if a == 34 and b == 34:
    print (a + b)

object_size = 10
proximity = 9000

if object_size > 5 and proximity < 1000:
    print('Evasive maneuvers required')
else:
    print('Object poses no threat')