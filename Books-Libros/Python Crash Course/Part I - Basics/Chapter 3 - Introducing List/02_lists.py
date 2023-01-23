# Changing, Adding, and Removing Elements

# Modifying Elements in a List
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

# Adding Elements to a List
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles.append('ducati') # Appending Elements to the End of a List
print(motorcycles)

motorcycles = [] 
motorcycles.append('honda') 
motorcycles.append('yamaha') 
motorcycles.append('suzuki') 
print(motorcycles)

# Inserting Elements into a List
motorcycles = ['honda', 'yamaha', 'suzuki'] 
motorcycles.insert(0, 'ducati') # You can add a new element at any position in your list by using the insert() method 
print(motorcycles)

# Removing Elements from a List
motorcycles = ['honda', 'yamaha', 'suzuki'] 
print(motorcycles)

del motorcycles[0] # Removing an Item Using the del Statement
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[1] 
print(motorcycles)

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
