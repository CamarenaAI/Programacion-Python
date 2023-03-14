"""
3.10 Cada Función

Piensa en algo que podrías almacenar en una lista. Por ejemplo, podría
hacer una lista de montañas, ríos, países, ciudades, idiomas o cualquier
otra cosa que desee. Escriba un programa que cree una lista que contenga
estos elementos y luego use cada función presentada en este capítulo al
menos una vez.
"""

languages = ['English', 'Portuguese', 'French', 'German', 'Chinese']
languages[4] = 'Dutch'
languages.append('Spanish')
languages.insert(4, 'Greek')
del languages[4]
languages.pop(3)
languages.remove('French')
print("I speak ", languages[0])

print(languages)
print(sorted(languages)) # Orden alfabetico
print(sorted(languages, reverse=True)) # Orden alfabetico inverso
languages.reverse() # Cambiar el orden de la lista
print(languages)
languages.reverse() # Cambiar otra vez el orden de la lista
print(languages)
languages.sort() # Orden alfabetico
print(languages)
languages.sort(reverse=True) # Orden alfabetico inverso
print(languages)
print("Number of languages, I would like learn: ", len(languages))