
# Esta función imprime un saludo
def saludar_mundo():
    print("¡Hola, mundo!")  # Muestra el mensaje en pantalla

# Llamamos a la función para que se ejecute
saludar_mundo()

# Esta función recibe un nombre y saluda a esa persona
def saludar_persona(nombre):
    print("Hola", nombre)

saludar_persona("Gerardo")  # Llamamos a la función con un argumento

# Esta función suma dos números y devuelve el resultado
def sumar(a, b):
    resultado = a + b
    return resultado  # Devuelve el valor al llamador

total = sumar(3, 4)  # Guardamos el valor retornado en una variable
print("La suma es:", total)

# Si no se pasa un valor, se usa el valor por defecto "Invitado"
def saludar(nombre="Invitado"):
    print(f"Hola, {nombre}!")

saludar()           # Usa el valor por defecto
saludar("Gerardo")  # Usa el valor dado

# Esta función devuelve la suma y la resta de dos números
def operaciones(a, b):
    suma = a + b
    resta = a - b
    return suma, resta  # Devuelve dos valores

x, y = operaciones(10, 5)  # Desempaquetamos los resultados
print("Suma:", x)
print("Resta:", y)

def cuadrado_simple(x):
    return x * x

def suma_de_cuadrados(a, b):
    return cuadrado_simple(a) + cuadrado_simple(b)

resultado = suma_de_cuadrados(2, 3)
print("Suma de cuadrados:", resultado)

# Función lambda para multiplicar dos números
multiplicar = lambda x, y: x * y
print(multiplicar(4, 5))  # Resultado: 20


def aplicar_funcion(func, valor):
    return func(valor)
def doble(n):
    return n * 2
print(aplicar_funcion(doble, 5))  # Pasa la función 'doble' como argumento


# Calcula el factorial de un número usando recursión
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)
print(factorial(5))  # Resultado: 120


# *args permite pasar cualquier número de argumentos posicionales
def suma_total(*args):
    return sum(args)
print(suma_total(1, 2, 3, 4))  # Resultado: 10


# **kwargs permite pasar argumentos con clave-valor
def mostrar_info(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")
mostrar_info(nombre="Gerardo", edad=30)

# Crea una función que reciba tu edad y diga si eres mayor de edad.
def saludo_edad():
    edad = int(input("Dime cuantos años tienes: "))
    if edad >= 18:
        print(f"Tu Edad es: {edad} Eres mayor de edad")
    else:
        print(f"Tu Edad es: {edad} Eres menor de edad")
    return edad
saludo_edad()

print("-" * 20)

# Escribe una función que reciba una cadena y devuelva cuántas letras tiene.
def contar_cadena_input():
    texto = input("Escribe una cadena de texto: ")
    cantidad = len(texto.replace(" ", ""))
    print(f"La cadena de texto: {texto} tiene: {cantidad} letras")
    return cantidad
contar_cadena_input() 


print("-" * 20)

# Escribe una función que multiplique dos números.
def multiplicar_dos_numeros(a, b):
    numeros = a * b
    return numeros
print(multiplicar_dos_numeros(6,7))

print("-" * 20)

# Crea una función que reciba un número y devuelva si es par o impar.
print("Hola Te gustaria saber si un numero es par o impar")
def par_o_impar_v2():
    numero = int(input("Ingresa un numero: "))
    if numero % 2 == 0:
        print(f"El numero; {numero} es par")
    else:
        print(f"El numero: {numero} es impar")
    return numero
par_o_impar_v2()

print("-" * 20)

# Escribe una función que reciba tu nombre y devuelva "Hola, [nombre]".
def nombre_saludo_input():
    nombre = input("Ingresa tu Nombre: ")
    print(f"Hola {nombre}")
nombre_saludo_input()

# Crea una función que reciba una lista de números y devuelva la suma total.

def suma_lista(lista_numeros):
    total = 0
    for numeros in lista_numeros:
        total += numeros
    return total
resultado = suma_lista([2,6,4,8,7])
print(resultado)

print("-" * 20)

# Escribe una función que reciba una palabra y devuelva si es palíndromo.

def es_palindromo(palabra):
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False
resultado = es_palindromo("Reconocer")
print(resultado)

print("-" * 20)

# Crea una función que reciba 3 números y devuelva el mayor.
def num_mayor(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
print(num_mayor(5,3,7))

print("-" *20) 

# Crea una función que reciba un texto y lo devuelva en mayúsculas.
def texto_mayusculas(texto):
    texto = texto.upper()
    return texto
texto = input("Escribe un texto y lo convierto en mayusculas: ")
print(texto_mayusculas(texto))

print("-" *20)

# Usa *args para crear una función que reciba cualquier cantidad 
# de números y devuelva su promedio.

def calcular_promedio(*numeros):
    suma = sum(numeros)
    cantidad = len(numeros)
    promedio = suma / cantidad
    return promedio
print(calcular_promedio(5,0,9,5))

print("-" *20)

# Crea una función que reciba tu edad y diga si eres mayor de edad.
def saludo():
    edad = int(input("Dime cuantos años tienes: "))
    if edad >= 18:
        print(f"Tu Edad es: {edad} Eres mayor de edad")
    else:
        print(f"Tu Edad es: {edad} Eres menor de edad")
    return edad
saludo()

print("-" * 20)

# Escribe una función que reciba una cadena y devuelva cuántas letras tiene.
def contar_cadena():
    texto = input("Escribe una cadena de texto: ")
    cantidad = len(texto.replace(" ", ""))
    print(f"La cadena de texto: {texto} tiene: {cantidad} letras")
    return cantidad
contar_cadena() 


print("-" * 20)

# Escribe una función que multiplique dos números.
def multiplicar_num(a, b):
    numeros = a * b
    return numeros
print(multiplicar_num(6,7))

print("-" * 20)

# Crea una función que reciba un número y devuelva si es par o impar.
print("Hola Te gustaria saber si un numero es par o impar")
def par_o_impar():
    numero = int(input("Ingresa un numero: "))
    if numero % 2 == 0:
        print(f"El numero; {numero} es par")
    else:
        print(f"El numero: {numero} es impar")
    return numero
par_o_impar()

print("-" * 20)

# Escribe una función que reciba tu nombre y devuelva "Hola, [nombre]".
def nombre_saludo():
    nombre = input("Ingresa tu Nombre: ")
    print(f"Hola {nombre}")
nombre_saludo()

# Escribe una función recursiva que calcule la suma de los 
# primeros n números naturales.

def suma_naturales(n):
    if n <= 1:
        return n
    else:
        return n + suma_naturales(n - 1)
    
print(suma_naturales(7))# 28
print(suma_naturales(3))# 6

print("-" *20)

# Usa una función lambda para ordenar una 
# lista de tuplas por el segundo valor.

lista = [(1,3),(2,4),(4,8),(6,7),(3,5)]
lista_ordenada = sorted(lista,key=lambda x:x[1])
print(lista_ordenada)
# = [(1, 3), (2, 4), (3, 5), (6, 7), (4, 8)]

print("-" * 20)

# Crea una función que reciba una función y un número, y 
# aplique esa función al número tres veces
def aplicar_trs_veces(funcion, numero):
    return funcion(funcion(funcion(numero)))
print(aplicar_trs_veces(lambda x: x + 1,4))
# = 7

print("-"* 20)

# Escribe una función que reciba una lista de números y 
# devuelva otra lista con los números al cuadrado (usa map).

def cuadrado(lista):
    return list(map(lambda x: x** 2, lista))
numeros = [2,3,5,6]
print(cuadrado(numeros))
# = [4,9,25,36]

print("-"*20)

# Usa **kwargs para mostrar 
# los datos de una persona (nombre, edad, ciudad, etc.).

def mostrar_datos_persona(**kwargs):
    print('Datos de la persona')
    for clave,valor in kwargs.items():
        print(f"-{clave.capitalize()}: {valor}")
mostrar_datos_persona(nombre="Gerardo",edad=44,ciudad='Tlaquepaque',ocupacion='Ingeniero')
"""
Datos de la persona
-Nombre: Gerardo
-Edad: 44
-Ciudad: Tlaquepaque
-Ocupacion: Ingeniero
"""

lista = [(3, 2), (1, 5), (4, 1)]
ordenada = sorted(lista, key=lambda x: x[0])
print(ordenada)  # [(1, 5), (3, 2), (4, 1)]

print('-' *20)

numeros = [1, 2, 3, 4, 5, 6, 25,28,36]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # [2, 4, 6, 28, 36]

print('-'*20)

#  Crea una función que reciba cualquier 
# cantidad de números con *args y devuelva el promedio. 
# Consejo: Usa sum() y len() sobre args.
def promedio(*numeros):
    if len(numeros) == 0:
        return 0
    suma = sum(numeros)
    cantidad = len(numeros)
    return suma / cantidad
print(promedio(4,9,7)) # = 6.666666666666667

print('-' *20)

# obtener los cuadrados de los números pares
numeros = [1,2,3,4,5,6]
cuadrado_pares = [n**2 for n in numeros if n % 2 == 0]
print(cuadrado_pares) # = [4, 16, 36]

print('-' *20)

# convertir palabras a mayúsculas
palabras = ['perro','loro','cantar']
mayusculas = [p.upper() for p in palabras]
print(mayusculas) # = ['PERRO', 'LORO', 'CANTAR']

print('-' *20)

# : crear un diccionario con número:cuadrado
numeros = [2,6,7,9]
dic_cuadrados = {n: n ** 2 for n in numeros}
print(dic_cuadrados) # = {2: 4, 6: 36, 7: 49, 9: 81}

print('-' *20)

