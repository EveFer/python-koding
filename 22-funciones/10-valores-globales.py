# valores globales

def valores():
    global num1, num2 # declararla como globales
    num1 = 10
    num2 = 50
    return num1 + num2

print(valores())
print(valores())
print(valores())

# scope

resta = num1 - num2

print(resta)