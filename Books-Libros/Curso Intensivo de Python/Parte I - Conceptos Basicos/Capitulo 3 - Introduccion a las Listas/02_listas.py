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

# Removiendo un elemento usando el metodo pop()
motocicletas = ['honda', 'yamaha', 'suzuki']
print(motocicletas)

motocicletas_pop = motocicletas.pop() # El metodo pop() remueve el ultimo elemento en una lista, pero te permite trabajar con ese elemento despues de eliminarlo
print(motocicletas)
print(motocicletas_pop)

motocicletas = ['honda', 'yamaha', 'suzuki'] 
ultima_motocicleta = motocicletas.pop() 
print("La ultima motocicleta que tuve fue una " + ultima_motocicleta.title() + ".")

# Removiendo elementos en cualquier posicion en una lista 
primer_motocicleta = motocicletas.pop(0) # De hecho, puede usar pop() para eliminar un elemento de una lista en cualquier posición al incluir el índice del elemento que desea eliminar entre paréntesis
print('La primer motocicleta que tuve fue una ' + primer_motocicleta.title() + '.')

# Removiendo un elemento de acuerdo con un valor
motocicletas = ['honda', 'yamaha', 'suzuki', 'ducati'] 
print(motocicletas)

motocicletas.remove('ducati') # Si solo conoce el valor del elemento que desea eliminar, puede usar el método remove()
print(motocicletas)

motocicletas = ['honda', 'yamaha', 'suzuki', 'ducati'] 
print(motocicletas)

motocicleta_cara = 'ducati'
motocicletas.remove(motocicleta_cara) # También puede usar el método remove() para trabajar con un valor que se está eliminando de una lista
print(motocicletas)
print("\nUna " + motocicleta_cara.title() + " es muy cara para mi.")