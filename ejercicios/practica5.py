# 1-Tabla de multiplicar del 7 con for.
for n in range(11):
    total = n * 7 
    print(f"{n} X 7 = {total}")
"""     
1 X 7 = 7 
2 X 7 = 14
3 X 7 = 21
4 X 7 = 28
5 X 7 = 35
6 X 7 = 42
7 X 7 = 49
8 X 7 = 56
9 X 7 = 63
10 X 7 = 70 """

# 2-Contar palabras en una lista usando diccionario.
animales = ["casa", "perro", "casa", "gato", "perro", "casa", "pájaro"]
contador = {}
for animal in animales:
    if animal in contador:
        contador[animal] += 1
    else:
        contador[animal] = 1
print(contador)
  # {'casa': 3, 'perro': 2, 'gato': 1, 'pájaro': 1}

# 3-Dibujar un triángulo con for.
for fila in range(1,5):
    for columna in range(fila):
        print("*", end="")
    print()
""" 
*
**
***
****
"""
print("-"*30)
# - Triangulo Invertido
for fila in range(5,0,-1):
    for columna in range(fila):
        print("*", end="")
    print()
"""     
*****
****
***
**
* 
"""
print("-"*30)
# -Triangulo alineado ala derecha
filas_totales = 5
for fila in range(filas_totales):
    espacios = " " * (filas_totales - fila - 1)
    asteriscos = "*" * (fila + 1)
    print(espacios + asteriscos)
"""    
    *
   **
  ***
 ****
*****
"""

print("-"*30)

# 4-Recorre una lista de números y crea una nueva con sus cuadrados.
numeros = [5,6,7,9,2,15,45]
cuadrados = []
for numero in numeros:
    cuadrados.append(numero * numero)
print(cuadrados)
# [25, 36, 49, 81, 4, 225, 2025]


# 5-Muestra el índice y el valor de cada letra en "Python".
letras = "Python"
for indice,valor in enumerate(letras):
    print(f"Indice: {indice} valor:{valor}")
"""     
Indice: 0 valor:P
Indice: 1 valor:y
Indice: 2 valor:t
Indice: 3 valor:h
Indice: 4 valor:o
Indice: 5 valor:n 
"""
print("-"*30)
# 6-Recorre un diccionario de países y capitales mostrando "La capital de X es Y".
paises = {
    "Mexico":"Ciudad de Mexico",
    "Rusia":"Moscu",
    "China":"Pekin",
    "Corea":"Seul"
}
for clave,valor in paises.items():
    print(f"La Capital de {clave} es: {valor} ")
""" 
La Capital de Mexico es: Ciudad de Mexico
La Capital de Rusia es: Moscu
La Capital de China es: Pekin
La Capital de Corea es: Seul 
"""
print("-"*30)
# 7-Usa bucles anidados para imprimir una tabla de multiplicar del 1 al 5.
for i in range(1,6):
    print(f"----Tabla del {i}----")
    for j in range(1, 11):
        resultado = i * j
        print(f"{i} X {j} = {resultado}")
    print("-"*20)
"""     ----Tabla del 1----
1 X 1 = 1
1 X 2 = 2
1 X 3 = 3
1 X 4 = 4
1 X 5 = 5
1 X 6 = 6
1 X 7 = 7
1 X 8 = 8
1 X 9 = 9
1 X 10 = 10
--------------------
----Tabla del 2----
2 X 1 = 2
2 X 2 = 4
2 X 3 = 6
2 X 4 = 8
2 X 5 = 10
2 X 6 = 12
2 X 7 = 14
2 X 8 = 16
2 X 9 = 18
2 X 10 = 20
--------------------
----Tabla del 3----
3 X 1 = 3
3 X 2 = 6
3 X 3 = 9
3 X 4 = 12
3 X 5 = 15
3 X 6 = 18
3 X 7 = 21
3 X 8 = 24
3 X 9 = 27
3 X 10 = 30
--------------------
----Tabla del 4----
4 X 1 = 4
4 X 2 = 8
4 X 3 = 12
4 X 4 = 16
4 X 5 = 20
4 X 6 = 24
4 X 7 = 28
4 X 8 = 32
4 X 9 = 36
4 X 10 = 40
--------------------
----Tabla del 5----
5 X 1 = 5
5 X 2 = 10
5 X 3 = 15
5 X 4 = 20
5 X 5 = 25
5 X 6 = 30
5 X 7 = 35
5 X 8 = 40
5 X 9 = 45
5 X 10 = 50
-------------------- """

# 8-Escribe un programa que pida al usuario un número y genere su tabla de multiplicar (1 al 10).
print("bienvenido ala multiplicadora ")
numero_multiplicar = int(input("Ingresa un numero para que aparersca la tabla de multiplicar: "))
for numero in range(1,11):
    resultado = numero_multiplicar * numero
    print(f"{numero_multiplicar} X {numero} = {resultado}")
""" 
6 X 1 = 6
6 X 2 = 12
6 X 3 = 18
6 X 4 = 24
6 X 5 = 30
6 X 6 = 36
6 X 7 = 42
6 X 8 = 48
6 X 9 = 54
6 X 10 = 60 
"""
# 9-Recorre una lista de palabras y cuenta cuántas tienen más de 5 letras.
palabras = ["dibujo","dardo","telefono","pala", "celular"]

for letra in palabras:
    if len(letra) > 5:
        print(letra)
""" 
dibujo
telefono
celular 
"""


# 10-Dibuja este patrón:
""" 
*
**
***
****
*****
 """
print("*"*30)

for x in range(1,6):
    for j in range(x):
        print("*", end="")
    print()
""" 
*
**
***
****
***** 
"""
