def greet():
    return 'Hola Fernanda!'

greet_fer = greet()
print(greet_fer)

say = greet

print(say())

# 🤓
def return_many_elements():
    return 'hola', 10, True, '🤓'

many_elements = return_many_elements()
print(type(many_elements)) # return a tuple


# woow 😍
def return_many_elements_two():
    return 1,2,3,4,5

num1, num2, num3, num4, num5 = return_many_elements_two()

print(num1, num2, num3, num4, num5)

