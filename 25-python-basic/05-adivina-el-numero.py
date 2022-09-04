import random

def run():
    num_random = random.randint(1, 100)
    num_choice = int(input('Elige un numero del 1 -100: '))

    while num_choice != num_random:
        if num_choice < num_random:
            print('Busca numero mas grande')
        else:
            print('Busca un numero mas pequeno')
        
        num_choice = int(input('Elige otro numero: '))
    print('Ganaste!!')

if __name__ == '__main__': # entry point
    run()