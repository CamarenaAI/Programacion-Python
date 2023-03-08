"""
3.10 Cada Función

Piensa en algo que podrías almacenar en una lista. 
Por ejemplo, podría hacer una lista de montañas, ríos, países, ciudades, idiomas o cualquier 
otra cosa que desee. Escriba un programa que cree una lista que contenga estos elementos y 
luego use cada función presentada en este capítulo al menos una vez.
"""
idiomas = ['Ingles', 'Portugues', 'Frances', 'Aleman', 'Chino']
idiomas[4] = 'Holandes'
idiomas.append('Español')
idiomas.insert(4, 'Griego')
del idiomas[4]
idiomas.pop(3)
idiomas.remove('Frances')
print("Yo hablo ", idiomas[0])

print(idiomas)
print(sorted(idiomas)) # Orden alfabetico
print(sorted(idiomas, reverse=True)) # Orden alfabetico inverso
idiomas.reverse() # Cambiar el oredn de la lista
print(idiomas)
idiomas.reverse() # Cambiar otra vez el orden de la lista
print(idiomas)
idiomas.sort() # Orden alfabetico
print(idiomas)
idiomas.sort(reverse=True) # Orden alfabetico inverso
print(idiomas)
print("Numero de idiomas, que me gustaria hablar: ", len(idiomas))