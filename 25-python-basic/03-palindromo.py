# Palabra que se lee igual al inverso

# luz azul

def isPalindromo(word):
    new_word = word.lower().replace(' ', '')
    inverted_word = new_word[::-1]
    if new_word == inverted_word:
        return True
    else:
        return False


def run():
    try:
        while True: 
            word = input('Ingresa una palabra: ')
            es_palindromo = isPalindromo(word)
            if es_palindromo:
                print('Es palindromo')
            else:
                print('No es palindromo')

    except KeyboardInterrupt:
        print('goodbay')

# punto de entrada
if __name__ == '__main__':
    run()