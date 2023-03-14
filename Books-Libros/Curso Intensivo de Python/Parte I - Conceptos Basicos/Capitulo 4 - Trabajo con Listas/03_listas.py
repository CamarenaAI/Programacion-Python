# Hacer Listas Numéricas

# Uso de la Función range()
for value in range(1,5): # La función range() de Python facilita la generación de una serie de números
    print(value)
print("\n")

for value in range(1,6):
    print(value)
print("\n")

# Usando range() Para Hacer una Lista de Números
numbers = list(range(1,6))
print(numbers)

even_numbers = list(range(2,11,2)) 
print(even_numbers)

squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
print(squares)

squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares, "\n")

# Estadísticas Simples con una Lista de Números
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits), "\n")

# Lista de Comprensiones
squares = [value**2 for value in range(1,11)]
print(squares)