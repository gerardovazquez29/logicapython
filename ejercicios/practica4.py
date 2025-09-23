# imprime los números pares del 1 al 20.
for numeros in range(1,21):
    if numeros % 2 == 0:
        print(numeros) # 2 4 6 8 10 12 14 16 18 20 

# Recorre una lista con nombres y saluda a cada uno.
nombres = ['Gerardo','Santiago','Guadalupe','Rocio','Elizabet']
for nombre in nombres:
    print(f"Hola {nombre} Que tengas un excelente dia")
    """
    Hola Gerardo Que tengas un excelente dia
    Hola Santiago Que tengas un excelente dia
    Hola Guadalupe Que tengas un excelente dia
    Hola Rocio Que tengas un excelente dia
    Hola Elizabet Que tengas un excelente dia
    """

# Cuenta cuántas letras "a" hay en "programacion".
texto = "programacion"
contador = 0
for letra in texto:
    if letra == 'a':
        contador += 1
        print( contador) # 2

# otra opcion

cantidad_a = texto.count('a')
print(cantidad_a) # 2


# pide una palabra y muestra cada letra en una línea.
palabra = input("Ingresa una palabra: ")
for letra in palabra:
    print(letra)
    """
    o
    r
    t
    a
    """
# imprime la tabla del 7 del 1 al 10.
for num in range(1,11):
    total = num * 7
    print(f"7 X {num} = {total}")
"""
7 X 1 = 7
7 X 2 = 14
7 X 3 = 21
7 X 4 = 28
7 X 5 = 35
7 X 6 = 42
7 X 7 = 49
7 X 8 = 56
7 X 9 = 63
7 X 10 = 70
"""
# imprime números del 1 al 10 pero salta el 5.
for num in range(1,11):
    if num == 5:
        continue
    print(num)
    """
    1
    2
    3
    4
    6
    7
    8
    9
    10
    """
# crea una lista de 5 números y muestra su cuadrado.
numeros = [2,3,4,5,6]
for numero in numeros:
    cuadrados = numero * numero
    print(f"el cuadrado de {numero} es:{cuadrados}")
    """
    el cuadrado de 2 es:4
    el cuadrado de 3 es:9
    el cuadrado de 4 es:16
    el cuadrado de 5 es:25
    el cuadrado de 6 es:36
    """
# crea un bucle que pida al usuario 5 palabras y las guarde en una lista.
lista_palabras = []

print("Bienvenido Escribe 5 palabras que te gusten que aparescan ")
for _ in range(5):
    palabra = input(f"Ingresa la palabra que te guste {_+1}: ")
    lista_palabras.append(palabra)
    print(f"Las Palabras Ingresadas son: {lista_palabras}")
print("Muchas Gracias")
""" Las Palabras Ingresadas son: ['python', 'Dyango', 'Pandas']
Ingresa la palabra que te guste 4: postgress
Las Palabras Ingresadas son: ['python', 'Dyango', 'Pandas', 'postgress']
Ingresa la palabra que te guste 5: flask
Las Palabras Ingresadas son: ['python', 'Dyango', 'Pandas', 'postgress', 'flask']
Muchas Gracias """

# while
lista_palabras = []
contador = 0

while contador < 5:
    palabra = input(f"Ingresa la palabra que te guste {contador+1}: ")
    lista_palabras.append(palabra)
    contador += 1
print(f"Las Palabras Ingresadas son: {lista_palabras}")
""" Ingresa la palabra que te guste 1: papa
Ingresa la palabra que te guste 2: pepe
Ingresa la palabra que te guste 3: pepa
Ingresa la palabra que te guste 4: pipa
Ingresa la palabra que te guste 5: popo
Las Palabras Ingresadas son: ['papa', 'pepe', 'pepa', 'pipa', 'popo'] """


# haz un programa que calcule la suma de los primeros 100 números enteros con un bucle.
total = 0
for numeros in range(101):
    total += numeros
print(f"la suma total de los numeros es: {total} ")
 # la suma total de los numeros es: 5050


# Recorre la palabra "autodidacta" e imprime solo las vocales.
vocales = 'aeiou'
palabra = "autodidacta"
vocales_encontrar = []
print(f"La palabra a analizar es: {palabra}")
for letra in palabra:
    if letra in vocales:
        vocales_encontrar.append(letra)
        print(f"Las vocales de la palabra 'autodidacta' son: {vocales_encontrar}") 

""" Las vocales de la palabra 'autodidacta' son: ['a']
Las vocales de la palabra 'autodidacta' son: ['a', 'u']
Las vocales de la palabra 'autodidacta' son: ['a', 'u', 'o']
Las vocales de la palabra 'autodidacta' son: ['a', 'u', 'o', 'i']
Las vocales de la palabra 'autodidacta' son: ['a', 'u', 'o', 'i', 'a']
Las vocales de la palabra 'autodidacta' son: ['a', 'u', 'o', 'i', 'a', 'a'] """


# intenta resolver un reto sencillo de lógica: imprime los números del 1 al 50, 
# pero sustituye múltiplos de 3 por “Fizz” y de 5 por “Buzz”.
for _ in range(1,51):
    if _ % 3 == 0:
        print("Fizz")
    elif _ % 5 == 0:
        print("Buzz")
    else:
        print(_)
"""  1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
"""
