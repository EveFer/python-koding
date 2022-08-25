#  Cuando no sabemos cuantos argumentos va a recibir una función

# con el * recibira los argumentos en un tupla
def argumentos(*nums):
    print(nums)
    for num in nums:
        print(num)
    return type(nums)

print(argumentos(10,30,10))