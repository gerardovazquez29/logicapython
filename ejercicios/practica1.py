# Ejercicios prácticos (10 en total)

# Crea una lista con tus 5 comidas favoritas e imprime la segunda y la última.
comidas = ['huevo','atun','pizza','comida china','arroz']
print(comidas[1])  # atun
print(comidas[-1]) # arroz

# Añade un nuevo elemento al final de una lista usando append().
comidas.append('surimi')
print(comidas) # ['huevo', 'atun', 'pizza', 'comida china', 'arroz', 'surimi']

# Elimina el tercer elemento de una lista con pop().
comidas.pop(2)
print(comidas) # ['huevo', 'atun', 'comida china', 'arroz', 'surimi']

# Ordena una lista de números y luego inviértela.
numeros = [6,2,8,3,4,1,9,7,2]
numeros.sort()
print(numeros) # [1, 2, 2, 3, 4, 6, 7, 8, 9]
numeros.reverse()
print(numeros) # [9, 8, 7, 6, 4, 3, 2, 2, 1]

# Usa slicing para imprimir los primeros 3 elementos de una lista.
print(numeros[:3]) # [9, 8, 7]

# Crea una lista de los números pares del 0 al 20 con comprensión de listas.
num = [num for num in range(21) if num % 2 == 0 ]
print(num) # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Dada la lista [5, 10, 15, 20, 25], imprime el elemento de la posición -2.
lista = [5,10,15,20,25]
print(lista[-2]) # 20

# Crea una lista anidada que represente una matriz 2x3 e imprime el primer elemento de la segunda fila.
matriz = [[2,3],[5,4],[9,7]]
print(matriz[1][0]) # 5

# Recorre una lista de nombres e imprime cada uno con la frase "Hola <nombre>".
nombres = ['Gerardo','Santiago','Luis','Roberto']
for nombre in nombres:
    print(f"Hola {nombre}")
"""
Hola Gerardo
Hola Santiago
Hola Luis
Hola Roberto
"""

# Usa sum(), max() y min() en una lista de números para obtener su suma, mayor y menor.
num = [8,7,6,5,2,3,4,9,1,0]
print(max(num)) # 9
print(min(num)) # 0
print(sum(num)) # 45
