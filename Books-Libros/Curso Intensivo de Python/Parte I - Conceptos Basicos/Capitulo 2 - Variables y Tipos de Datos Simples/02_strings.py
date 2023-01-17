# Strings

# Cambio de mayúsculas y minúsculas en un string usando métodos
nombre = "ada lovelace"
print(nombre.title()) # el método title() convierte las primeras letras de las palabras en mayúsculas
nombre = "ada lovelace"
print(nombre.upper()) # El método upper() convierte todas las letras en mayúsculas
nombre = "ada lovelace"
print(nombre.lower()) # El método lower() convierte todas las letras en minúsculas

# Combinando o concatenando Strings
nombre = "ada"
apellido = "lovelace"
nombre_completo = nombre + " " + apellido
print(nombre_completo)

nombre = "ada"
apellido = "lovelace"
nombre_completo = nombre + " " + apellido
mensage = "¡Hola, " + nombre_completo.title() + "!"
print(mensage)

# Agregar espacios en blanco a strings con tabulador o saltos de línea
print("Python")
print("\tPython") # para agregar un string a su texto, use la combinación de caracteres \t
print("Lenguajes:\nPython\nC\nJavaScript")  # para agregar una nueva línea en una cadena, use la combinación de caracteres \n
print("Lenguajes:\n\tPython\n\tC\n\tJavaScript")

# Removiendo espacios en blanco
lenguaje_favorito = 'python '
print(lenguaje_favorito)
lenguaje_favorito = ' python '
lenguaje_favorito = lenguaje_favorito.rstrip()
print(lenguaje_favorito)
lenguaje_favorito = lenguaje_favorito.lstrip()
print(lenguaje_favorito)
lenguaje_favorito = lenguaje_favorito.strip()
print(lenguaje_favorito)

# Evitar errores de sintaxis con Strings
"""
mensaje = 'Una de las fortalezas de Python' es su comunidad diversa'
print(mensaje)
Output: SyntaxError: invalid syntax
"""
mensaje = "Una de las fortalezas de Python es su comunidad diversa"
print(mensaje)