# Prueba Condicional

# Comprobación de Igualdad
car = 'audi' # Inserta el modelo del auto
if car == 'bmw':
	print(True)
else:
	print(False)

# Ignorar el caso al verificar la igualdad
car = 'Audi' # Inserta el modelo del auto
if car.lower() == 'audi':
	print(True)
else:
	print(False)
print(car)

# Comprobación de Desigualdad
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")

# Comparaciones Numéricas
age = 18
if age == 18:
    print(True)
else:
    print(False)

answer = 17
if answer != 42:
    print("That is not the correct answer. Please try again!")

age = 19
if age < 21:
    print(True)
else:
    print(False)
if age <= 21:
    print(True)
else:
    print(False)
if age > 21:
    print(True)
else:
    print(False)
if age >= 21:
    print(True)
else:
    print(False)

# Comprobación de múltiples condiciones
# Uso de "and" para comprobar varias condiciones
age_0 = 22 
age_1 = 22
if age_0 >= 21 and age_1 >= 21: # Es necesario cumplir las 2 condiciones
    print(True)
else:
    print(False)

# Usar "or" para comprobar varias condiciones
age_0 = 10 
age_1 = 22
if age_0 >= 21 or age_1 >= 21: # Es necesario cumplir 1 condicion
    print(True)
else:
    print(False)

# Comprobar si un valor está en una lista
requested_toppings = ['mushrooms', 'onions', 'pineapple']
'mushrooms' in requested_toppings
print(True)
'pepperoni' in requested_toppings
print(False)

# Comprobar si un valor no está en una lista
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")

# Expresiones booleanas
"""
A Boolean expression is just another name for a 
conditional test. A Boolean value is either True or False, just like the value 
of a conditional expression after it has been evaluated
"""
game_active = True
can_edit = False