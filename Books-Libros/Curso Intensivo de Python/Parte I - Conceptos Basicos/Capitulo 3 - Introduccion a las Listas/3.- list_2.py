# Cambiando, agregando y removiendo elementos

# Modificando elementos de una lista
motocicletas = ['honda', 'yamaha', 'suzuki']
print(motocicletas)
motocicletas[0] = 'ducati'
print(motocicletas)

# Agregando elementos de una lista
motocicletas = ['honda', 'yamaha', 'suzuki']
print(motocicletas)

motocicletas.append('ducati') # Concatenando elementos al final de una lista
print(motocicletas)

motocicletas = [] 
motocicletas.append('honda') 
motocicletas.append('yamaha') 
motocicletas.append('suzuki') 
print(motocicletas)

# Insertando elementos en una lista
motocicletas = ['honda', 'yamaha', 'suzuki'] 
motocicletas.insert(0, 'ducati') # Tu pudes agregar un nuevo elemento en una posicion en la lista usando el metodo insert()
print(motocicletas)

# Removiendo elementos de una lista
motocicletas = ['honda', 'yamaha', 'suzuki'] 
print(motocicletas)

del motocicletas[0] # Removiendo un elemento usando el metodo del
print(motocicletas)

motocicletas = ['honda', 'yamaha', 'suzuki']
print(motocicletas)
del motocicletas[1] 
print(motocicletas)

# Removing an Item Using the pop() Method
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop() # The pop() method removes the last item in a list, but it lets you work with that item after removing it
print(motorcycles)
print(popped_motorcycle)

motorcycles = ['honda', 'yamaha', 'suzuki'] 
last_owned = motorcycles.pop() 
print("The last motorcycle I owned was a " + last_owned.title() + ".")

# Popping Items from any Position in a List
first_owned = motorcycles.pop(0) # You can actually use pop() to remove an item in a list at any position by including the index of the item you want to remove in parentheses
print('The first motorcycle I owned was a ' + first_owned.title() + '.')

# Removing an Item by Value
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati'] 
print(motorcycles)

motorcycles.remove('ducati') # If you only know the value of the item you want to remove, you can use the remove() method
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati'] 
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive) # You can also use the remove() method to work with a value that’s being removed from a list
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")