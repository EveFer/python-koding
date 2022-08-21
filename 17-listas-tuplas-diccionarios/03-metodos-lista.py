lista = [10, 20, 30, 40, 50]

print(lista)

# append -> agregal al final de la lista

lista.append(60)

print(lista)

lista.append('Python')

print(lista)

# insert(positionToInsert, item)

lista.insert(2, 'newData')

print(lista)


# count(elemenToCount) -> buscar cuantos items hay del argumento
print(lista.count('Python'))


# index(elementToSearch) -> regresa el valor de la posicion del primer valor encontrado

print(lista.index('Python'))

# sort
lista_2 = [2,4,7,1,23,79]
lista_2.sort(reverse=True) # orden ascendente
print(lista_2)

# reverse -> invierte los items de una lista


# pop() -> eliminar el ultimo item de la lista

lista_2.pop()

# remove(item_to_remove) -> elimina el valor que se pase como argumento