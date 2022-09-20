# Crear, con un dictionary comprehension, un diccionario cuyas lleves sean los 1000
# primeros numeros naturales con sus raices cuadradas como valores


from math import sqrt


def run():
    nums_dict = {num: sqrt(num) for num in range(1,1001)}

    print(nums_dict)

if __name__ == '__main__':
    run()