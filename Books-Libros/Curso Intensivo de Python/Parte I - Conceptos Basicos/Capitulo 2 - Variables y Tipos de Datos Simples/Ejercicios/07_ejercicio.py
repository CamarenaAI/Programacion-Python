"""
2.7 Removiendo caracteres en blanco de nombres

Guarde el nombre de una persona e incluya algunos espacios en blanco
al principio y al final del nombre. Asegúrese de usar cada
combinación de caracteres, "\t" y "\n", al menos una vez.
    Imprima el nombre una vez, de modo que se muestre el espacio en
    blanco alrededor del nombre.
    Luego imprima el nombre usando cada una de las tres funciones de
    strip: lstrip(), rstrip() y strip()
"""

name = "\tEric\n Erika"
print(name.lstrip())

name = "\tEric\n Luis"
print(name.rstrip())

name = "\nEric\n\t May"
print(name.strip())