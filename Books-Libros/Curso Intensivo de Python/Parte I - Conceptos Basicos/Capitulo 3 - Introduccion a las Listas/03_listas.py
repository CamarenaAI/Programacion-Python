# Organizando una lista

# Organizando una lista de forma permanente con el metodo sort()
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort() # El método sort() de Python hace que sea relativamente fácil ordenar una lista
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True) # También puede ordenar esta lista en orden alfabético inverso pasando el argumento reverse=True al método sort()
print(cars)

# Ordenar una lista temporalmente con la función sorted()
cars = ['bmw', 'audi', 'toyota', 'subaru']

print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars)) # La función sorted() le permite mostrar su lista en un orden particular pero no afecta el orden real de la lista

print("\nHere is the original list again:")
print(cars)

# Imprimir una lista en orden inverso
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.reverse() # Para invertir el orden original de una lista, puede usar el método reverse()
print(cars)

# Encontrar la longitud de una lista
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars)) # Puede encontrar rápidamente la longitud de una lista usando la función len()