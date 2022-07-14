# Organizing a List

# Sorting a List Permanently with the sort() Method
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort() # Python’s sort() method makes it relatively easy to sort a list
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True) # You can also sort this list in reverse alphabetical order by passing the argument reverse=True to the sort() method
print(cars)

# Sorting a List Temporarily with the sorted() Function
cars = ['bmw', 'audi', 'toyota', 'subaru']

print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars)) # The sorted() function lets you display your list in a particular order but doesn’t affect the actual order of the list

print("\nHere is the original list again:")
print(cars)

# Printing a List in Reverse Order
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.reverse() # To reverse the original order of a list, you can use the reverse() method
print(cars)

# Finding the Length of a List
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars)) # You can quickly find the length of a list by using the len() function
