### List Comprehension ###

frutas = ['manzana','platano', 'naranja']
print(frutas[0]) # manzana

numeros = [1, 2, 3]
print(len(numeros))  # 3
print(numeros * 2)   # [1, 2, 3, 1, 2, 3]

frutas = ["manzana", "plátano", "naranja"]
frutas.append("uva")       # agrega al final
frutas.insert(1, "pera")   # inserta en posición
frutas.remove("plátano")   # elimina por valor
frutas.pop()               # elimina último
frutas.sort()              # ordena
frutas.reverse()           # invierte
print(frutas)



my_original_list = [0, 1, 2, 3, 4, 5, 6, 7]
print(my_original_list) # [0, 1, 2, 3, 4, 5, 6, 7]

my_range = range(8)
print(list(my_range)) # [0, 1, 2, 3, 4, 5, 6, 7]

my_list = [i + 1 for i in range(8)]
print(my_list) # [1, 2, 3, 4, 5, 6, 7, 8]

my_list = [i * 2 for i in range(8)]
print(my_list) # [0, 2, 4, 6, 8, 10, 12, 14]

my_list = [i * i for i in range(8)]
print(my_list)  # [0, 1, 4, 9, 16, 25, 36, 49]

def sum_five(number):
    return number + 5
my_list = [sum_five(i) for i in range(8)]
print(my_list) # [5, 6, 7, 8, 9, 10, 11, 12]


print("-"*28)

# Ejercicios
# 1. Genera una lista utilizando comprensión con los números 
#    del 0 al 10.
lista_compresion = range(11)
print(list(lista_compresion)) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 2. Crea una lista utilizando comprensión con los cuadrados 
#    de los números del 1 al 10.
my_list = [i ** 2 for i in range(11)]
print(my_list) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


# 3. Genera una lista utilizando comprension con los numeros pares del 0 al 20.

pares = [i for i in range(21) if i % 2 == 0]
print(pares) # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# 4. Convierte una lista de temperaturas en Celsius a Fahrenheit utilizando comprension.
celsius = [0,10,20,30,40]
fahrenheit = [temp * 1.8 + 32 for temp in celsius]
print(fahrenheit) # [32.0, 50.0, 68.0, 86.0, 104.0]

# 5. Crea una lista utilizando comprension con los caracteres de una cadena.
texto = "Python"
caracteres = [caracter for caracter in texto]
print(caracteres) # ['P', 'y', 't', 'h', 'o', 'n']

# 6. Filtra una lista de palabras y deja solo las que tienen mas de 4 letras utilizando comprension.
palabras = ["Gerardo", "Vazquez", "dev", "hola", "python"]
palabras_largas = [palabra for palabra in palabras if len(palabra) > 4]
print(palabras_largas) # ['Gerardo', 'Vazquez', 'python']

# 7. Aumenta en 5 cada numero de una lista con comprension usando una funcion externa.
def sumar_cinco(numero):
    return numero + 5
numeros = [1,2,3,4,5]
resultado = [sumar_cinco(numero) for numero in numeros]
print(resultado) # [6, 7, 8, 9, 10]

# 8. Crea una lista de booleanos que indique si cada numero es mayor que 10 utilizando comprension.
lista_numeros = [5,9,12,15,7,49]
resultado_booleano = [numero > 10 for numero in lista_numeros]
print(resultado_booleano) # [False, False, True, True, False, True]

# 9. Multiplica solo los numeros impares por 3 en una lista utilizando comprension.
lista_impar =[x * 3 for x in range(1,20) if x % 2 != 0]
print(lista_impar) # [3, 9, 15, 21, 27, 33, 39, 45, 51, 57]

# 10. Usa comprension de listas anidada para generar una matriz 3x3 con numeros del 1 al 9.
matriz = [[fila * 3 + columna + 1 for columna in range(3)] for fila in range(3)]
print(matriz) # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print("-"*35)

# 11. Genera una lista con los números del 1 al 50, pero solo los múltiplos de 3.
multiplos_tres = [n for n in range(51) if n % 3 == 0]
print(multiplos_tres) # [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48]

# 12. Convierte cada letra de la palabra "Pythonista" en minúscula usando list comprehension.
palabra = "Pythonista"
palabra_minuscula = "".join([letra.lower() for letra in palabra])# join une todas las letras en una cadena
print(palabra_minuscula) # pythonista

palabra_minuscula = "".join([letra.lower() for letra in "Pythonista"])# agregando las comillas y el join une todo
print(palabra_minuscula) # ['p', 'y', 't', 'h', 'o', 'n', 'i', 's', 't', 'a'] o pythonista

# 13. Crea una lista con los cubos de los números impares del 1 al 20.
impares = [i**3 for i in range(1,21) if i % 2 != 0]
print(impares) # [1, 27, 125, 343, 729, 1331, 2197, 3375, 4913, 6859]

# 14. Genera una lista con las palabras de una frase, pero solo aquellas que tengan más de 4 letras.
frase = "Eres un buen estudiante seras el mejor"
frase_mas_cuatro = [palabra for palabra in frase.split() if len(palabra) > 4 ] # split divide la frase en palabras
print(frase_mas_cuatro) # ['estudiante', 'seras', 'mejor']

# 15. Dada una lista de temperaturas en Celsius [0, 20, 30, 40], conviértelas a Fahrenheit.
Celsius = [0, 20, 30, 40]
Fahrenheit = [temp * 9/5 + 32 for temp  in Celsius]
print(Fahrenheit) # [32.0, 68.0, 86.0, 104.0]

# 16. Crea una matriz identidad de 3x3 usando list comprehension.
matriz = [[1 if x == j else 0  for x in range(3)]  for j in range(3)] 
print(matriz) # [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

# 17.Crear una matriz 3x3 usando listas por compresión
matriz = [[s for s in range(3)] for m in range(3)]
print(matriz) # [[0, 1, 2], [0, 1, 2], [0, 1, 2]]

# 18. Crea una nueva lista que contenga solo las palabras que 
# tengan más de 6 letras y conviértelas en mayúsculas.
palabras = ["computadora", "python", "dato", "programación", "red", "algoritmo"]
mas_de_seis = [n.upper() for n in palabras if  len(n) > 6 ]
print(mas_de_seis) # ['COMPUTADORA', 'PROGRAMACIÓN', 'ALGORITMO']

# 19. Usa comprensión de listas para obtener la matriz transpuesta (filas ↔ columnas).
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matriz_traspuesta = [[fila[i] for fila in matriz] for i in range(len(matriz[0]))]
print(matriz_traspuesta) # [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

# 20. Crea una lista por comprensión que contenga los números únicos en orden ascendente.
numeros = [3, 6, 2, 6, 7, 3, 8, 2, 1]
unicos_ordenados = [n for n in sorted(set(numeros))]
print(unicos_ordenados) # [1, 2, 3, 6, 7, 8]

# 21. Dada la lista ["python", "es", "poderoso"], 
# crea un diccionario donde la clave sea la palabra y el valor la palabra en mayúsculas.
frase = ["python", "es", "poderoso"]

# 22. Genera un diccionario con los números del 1 al 10 como claves y 
# su paridad como valor ("par" o "impar").
pares_y_nones = {n: ("par" if n % 2 == 0 else "impar") for n in range(1, 11)}
print(pares_y_nones) # {1: 'impar', 2: 'par', ..., 10: 'par'}

# 23. Dado un diccionario con nombres y edades:
personas = {"Ana": 20, "Luis": 17, "María": 25, "Pedro": 15}
# Crea un nuevo diccionario solo con las personas mayores de edad (>=18).
mayores = {nombre: edad for nombre, edad in personas.items() if edad >= 18}
print(mayores) # {'Ana': 20, 'María': 25}

# 24. Dada una cadena: "programacion", crea un diccionario con cada letra y cuántas veces aparece.
cadena = "programacion"
veses_aparese = {letra: cadena.count(letra) for letra in set(cadena)}
print(veses_aparese) # {'c': 1, 'n': 1, 'a': 2, 'i': 1, 'r': 2, 'p': 1, 'o': 2, 'g': 1, 'm': 1}

# 25. Genera un diccionario que represente una tabla de multiplicar del 5, 
# con el número como clave y el resultado como valor.
tabla_del_cinco = {n: n * 5 for n in range(1,6)}
print(tabla_del_cinco) # {1: 5, 2: 10, 3: 15, 4: 20, 5: 25}

matriz = [[1, 2], [3, 4], [5, 6]]
print(matriz[1][0])  # 3

numeros = [3, 7, 2, 9, 5]
print(min(numeros))  # 2
print(max(numeros))  # 9
print(sum(numeros))  # 26
