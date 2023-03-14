# Uso de sentencias if con listas

# Comprobación de artículos especiales
requested_toppings = ['mushrooms', 'green peppers', 'extra chesse']
for requested_topping in requested_toppings:
    print("Adding " + requested_topping+ ".")

print("\nFinished making your pizza!") 

requested_toppings = ['mushrooms', 'green peppers', 'extra chesse']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print("Adding " + requested_topping + ".")

print("\nFinished making your pizza!") 

# Comprobar que una lista no está vacía
requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding: " + requested_topping + ".")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")
    
# Uso de lista multiples
available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pinapple', 'extra chesse']

requested_toppings = ['mushrooms', 'french fries', 'extra chesse']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")