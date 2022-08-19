# Operadores relacionales y Logicos
# Hacen referencias a condiciones enetre datos, tambien pueden ser visto como
# comparaciones

# Para hacer comparaciones

# == | Igual que | 5 == 7 -> False
# != | Diferente de | 5 != 7 -> True
# < | Menor que  | 5 < 7 -> True
# > | Mayor que  | 5 > 7 -> False
# <= | Menor o igual que  | 5 <= 7 -> True
# >= | Mayor o igual que  | 5 >= 7 -> False

# Operadores Logicos
# Hacen referencia a condiciones entre datos, tambien pueden
# ser vistos como comparaciones

# and | y |  10 > 1 and 70 <= 70 -> True
# or | o |  50 >= 80 or 6 == 6 -> True
# not | negacion |  3.14 > 3 -> True -> con not -> False

# and tabla de verdad
# True  | True -> True
# True  | False -> False
# False | True -> False
# False | False -> False

# or tabla de verdad
# True  | True -> True
# True  | False -> True
# False | True -> True
# False | False -> False

# not tabla de verdad
# True  -> False
# False -> True


num_1 = 234
num_2 = 500

print(num_1 < num_2)
print(num_1 > num_2)
print(num_1 >= num_2)
print(num_1 <= num_2)
print(num_1 == num_2)
print(num_1 != num_2)

string_1 = 'Fer'
string_2 = 'fer'

print(string_1 == string_2)

# Operadores logicos

print(10 > 2 and 20 > 50)

print(88 <= 100 or 100 >= 500)

print(not 90 != 90)

