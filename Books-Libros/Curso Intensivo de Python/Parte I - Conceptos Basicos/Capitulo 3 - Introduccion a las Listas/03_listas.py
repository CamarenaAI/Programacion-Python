# Organizando una lista

# Organizando una lista de forma permanente con el metodo sort()
carros = ['bmw', 'audi', 'toyota', 'subaru']
carros.sort() # El método sort() de Python hace que sea relativamente fácil ordenar una lista
print(carros)

carros = ['bmw', 'audi', 'toyota', 'subaru']
carros.sort(reverse=True) # También puede ordenar esta lista en orden alfabético inverso pasando el argumento reverse=True al método sort()
print(carros)

# Ordenar una lista temporalmente con la función sorted()
carros = ['bmw', 'audi', 'toyota', 'subaru']

print("Aqui esta es la lista original:")
print(carros)

print("\nAqui esta la lista ordenada:")
print(sorted(carros)) # La función sorted() le permite mostrar su lista en un orden particular pero no afecta el orden real de la lista

print("\nAqui esta la lista original otra vez:")
print(carros)

# Imprimir una lista en orden inverso
carros = ['bmw', 'audi', 'toyota', 'subaru']
print(carros)

carros.reverse() # Para invertir el orden original de una lista, puede usar el método reverse()
print(carros)

# Encontrar la longitud de una lista
carros = ['bmw', 'audi', 'toyota', 'subaru']
print(len(carros)) # Puede encontrar rápidamente la longitud de una lista usando la función len()
