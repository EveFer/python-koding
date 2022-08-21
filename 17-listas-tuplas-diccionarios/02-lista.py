
# colors = ['yellow', 'green', 'orange', 'purple']

tuffs = ['circle', 'developer', True, 10.34, 23, 'Python']

print(type(tuffs))

print(tuffs[3])
print(len(tuffs))

# son mutables

tuffs[2] = False

print(tuffs)

# segmentado de listas

lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(len(lista))

print('position 5: ', lista[5])
print('Primeros 5: ', lista[:5])
print('Primeros 5: ', lista[0:5])
print('Del 10 en adelante: ', lista[10:]) 
print('Del 10 en adelante hasta el 20 sin contal el ultimo: ', lista[10:20]) 
print('El ultimo item: ', lista[-1]) 
