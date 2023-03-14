"""
3.11 Error Intencional

Si aún no ha recibido un error de índice en uno de sus programas, intente
que suceda. Cambie un índice en uno de sus programas para producir un
error de índice. Asegúrese de corregir el error antes de cerrar el 
programa
"""

languages = ['English', 'Portuguese', 'French', 'German', 'Chinese']
languages[4] = 'Dutch'
languages.append('Spanish')
languages.insert(4, 'Greek')
del languages[4]
languages.pop(3)
languages.remove('French')
print("I speak ", languages[0])
# print("I would like learn ", languages[6]) Error

print(languages)
print(sorted(languages)) # Alphabetic order
print(sorted(languages, reverse=True)) # Reverse alphabetic order
languages.reverse() # Change order of your list
print(languages)
languages.reverse() # Change order of your list again
print(languages)
languages.sort() # Alphabetic order
print(languages)
languages.sort(reverse=True) # Reverse alphabetic order
print(languages)
print("Number of languages, I would like learn: ", len(languages))