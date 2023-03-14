"""
5.6 Etapas de la vida

Escriba una cadena if-elif-else que determine la etapa de vida de una
persona. Establezca un valor para la variable edad, luego:

•   Si la persona tiene menos de 2 años, imprima un mensaje de que la
    persona es un bebé
•   Si la persona tiene al menos 2 años pero menos de 4, escriba el
    mensaje de que la persona es un niño pequeño
•   Si la persona tiene al menos 4 años pero menos de 13, imprima un
    mensaje de que la persona es un niño
•   Si la persona tiene al menos 13 años pero menos de 20, imprima un
    mensaje de que la persona es un adolescente
•   Si la persona tiene al menos 20 años pero menos de 65, imprima un
    mensaje de que la persona es un adulto
•   Si la persona tiene 65 años o más, imprima un mensaje de que la
    persona es una persona mayor
"""

age = 24

if age < 2:
    age = "baby"
elif age >= 2 and age < 4:
    age = "toodler"
elif age >= 4 and age < 13:
    age = "kid"
elif age >= 13 and age < 20:
    age = "teenager"
elif age >= 20 and age < 65:
    age = "adult"
else:
    age = "elder"
    
print("The person is a/an " + age)