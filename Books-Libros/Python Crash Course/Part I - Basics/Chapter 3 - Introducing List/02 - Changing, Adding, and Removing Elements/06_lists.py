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