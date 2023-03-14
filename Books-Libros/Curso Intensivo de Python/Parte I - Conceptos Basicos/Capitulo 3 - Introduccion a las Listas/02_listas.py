# Cambiando, agregando y removiendo elementos

# Modificando elementos de una lista
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

# Agregando elementos de una lista
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles.append('ducati') # Concatenando elementos al final de una lista
print(motorcycles)

motorcycles = [] 
motorcycles.append('honda') 
motorcycles.append('yamaha') 
motorcycles.append('suzuki') 
print(motorcycles)

# Insertando elementos en una lista
motorcycles = ['honda', 'yamaha', 'suzuki'] 
motorcycles.insert(0, 'ducati') # Tu pudes agregar un nuevo elemento en una posicion en la lista usando el metodo insert()
print(motorcycles)

# Removiendo elementos de una lista
motorcycles = ['honda', 'yamaha', 'suzuki'] 
print(motorcycles)

del motorcycles[0] # Removiendo un elemento usando el metodo del
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[1] 
print(motorcycles)

# Removiendo un elemento usando el metodo pop()
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop() # El metodo pop() remueve el ultimo elemento en una lista, pero te permite trabajar con ese elemento despues de eliminarlo
print(motorcycles)
print(popped_motorcycle)

motorcycles = ['honda', 'yamaha', 'suzuki'] 
last_owned = motorcycles.pop() 
print("The last motorcycle I owned was a " + last_owned.title() + ".")

# Removiendo elementos en cualquier posicion en una lista 
first_owned = motorcycles.pop(0) # De hecho, puede usar pop() para eliminar un elemento de una lista en cualquier posición al incluir el índice del elemento que desea eliminar entre paréntesis
print('The first motorcycle I owned was a ' + first_owned.title() + '.')

# Removiendo un elemento de acuerdo con un valor
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati'] 
print(motorcycles)

motorcycles.remove('ducati') # Si solo conoce el valor del elemento que desea eliminar, puede usar el método remove()
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati'] 
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive) # También puede usar el método remove() para trabajar con un valor que se está eliminando de una lista
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")