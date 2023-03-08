"""
4.10 Slices

Using one of the programs you wrote in this chapter, add several 
lines to the end of the program that do the following:
•	Print the message, The first three items in the list are:. Then use a slice to 
    print the first three items from that program’s list
•	Print the message, Three items from the middle of the list are:. Use a slice 
    to print three items from the middle of the list
•	Print the message, The last three items in the list are:. Use a slice to print 
    the last three items in the list
"""
pizzas = ['Hawaiian', 'Buffalo', 'Pepperoni', 'Cheese', 'Veggie', 'Meat', 'BBQ Chicken', 'Supreme', 'Margherita']
for pizza in pizzas:
    print("This is a " + pizza + " pizza\n" )
print(pizzas[0:3])
print(pizzas[3:6])
print(pizzas[6:9])
