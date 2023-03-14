# Strings

# Cambio de mayúsculas y minúsculas en un string usando métodos
name = "ada lovelace"
print(name.title()) # El método title() convierte las primeras letras de las palabras en mayúsculas

name = "ada lovelace"
print(name.upper()) # El método upper() convierte todas las letras en mayúsculas

name = "ada lovelace"
print(name.lower()) # El método lower() convierte todas las letras en minúsculas

# Combinando o concatenando Strings
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name)

first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
message = "Hello, " + full_name.title() + "!"
print(message)

# Agregar espacios en blanco a strings con tabulador o saltos de línea
print("Python")
print("\tPython") # para agregar un string a su texto, use la combinación de caracteres \t
print("Languages:\nPython\nC\nJavaScript")  # para agregar una nueva línea en una cadena, use la combinación de caracteres \n
print("Languages:\n\tPython\n\tC\n\tJavaScript")

# Removiendo espacios en blanco
favorite_language = 'python '
print(favorite_language)
favorite_language = ' python '
favorite_language = favorite_language.rstrip()
print(favorite_language)
favorite_language = favorite_language.lstrip()
print(favorite_language)
favorite_language = favorite_language.strip()
print(favorite_language)

# Evitar errores de sintaxis con Strings
"""
message = 'One of Python's strengths is its diverse comunity'
print(message)
Output: SyntaxError: invalid syntax
"""
message = "One of Python's strengths is its diverse comunity"
print(message)