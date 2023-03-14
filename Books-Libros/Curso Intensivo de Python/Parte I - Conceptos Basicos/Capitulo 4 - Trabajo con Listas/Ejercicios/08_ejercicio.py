"""
4.8 Cubos

Un número elevado a la tercera potencia se llama cubo. Por ejemplo, el
cubo de 2 se escribe como 2**3 en Python. Haga una lista de los primeros
10 cubos (es decir, el cubo de cada número entero del 1 al 10) y use un
ciclo for para imprimir el valor de cada cubo
"""

cubes = []
for value in range(1,11):
    cubes.append(value**3)
print(cubes)