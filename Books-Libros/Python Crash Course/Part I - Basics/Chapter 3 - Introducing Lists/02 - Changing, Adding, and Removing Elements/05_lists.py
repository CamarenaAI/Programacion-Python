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