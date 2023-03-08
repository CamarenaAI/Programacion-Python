"""
3.11 Error Intencional

Si aún no ha recibido un error de índice en uno de sus programas, 
intente que suceda. Cambie un índice en uno de sus programas para 
producir un error de índice. Asegúrese de corregir el error antes 
de cerrar el programa
"""
idiomas = ['Ingles', 'Portugues', 'Frances', 'Aleman', 'Chino']
idiomas[4] = 'Holandes'
idiomas.append('Español')
idiomas.insert(4, 'Griego')
del idiomas[4]
idiomas.pop(3)
idiomas.remove('Frances')
print("Yo hablo ", idiomas[0])
# print("Me gustaria aprender a hablar ", idiomas[6]) Error

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