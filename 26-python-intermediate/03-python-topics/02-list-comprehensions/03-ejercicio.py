# Crear, con un list comprehension, una lista de todos
# los multiplos de 4 que a la vez tambien sean multiplos de 6 y 9
# 1 - 99,999

def run ():
    number_list = [number for number in range(1, 1000) if number % 4 == 0 and number % 6 == 0 and number % 9 == 0]
    print(number_list)

if __name__ == '__main__':
    run()