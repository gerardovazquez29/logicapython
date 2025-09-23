#   10 Ejercicios de Práctica
# Ejercicios de Tuplas (1–5)
# 1-Crea una tupla con 6 números. Imprime el primero y el último.
numeros = (1,2,3,4,5,6)
print(numeros[0]) # 1
print(numeros[-1]) # 6

# 2-Desempaqueta una tupla de 3 valores en variables e imprímelas.
tupla = ('toño',35,'mexico')
nombre, edad,pais = tupla
print(nombre,edad,pais) # toño 35 mexico

# 3-Usa .count() para contar cuántas veces aparece un número en una tupla.
numeros_contados = (1,2,5,4,6,9,8,5,3,4,7,2,6,4,2,6)
print(numeros_contados.count(2)) # 3


# 4-Crea una tupla de tuplas (matriz 2x2) y accede al elemento en la posición (2,1).
matriz = ((2,1),(5,4))
print(matriz[1][1]) # 4

# 5-Dada la tupla ("python", "java", "python", "c"), encuentra la posición de la primera ocurrencia de "python".
ocurrencia = ("python", "java", "python", "c")
print(ocurrencia.index("python")) # 0


# Ejercicios de Sets (6–10)

# 6-Crea un set con los números 1, 2, 2, 3, 4, 4. Imprime el set (¿qué pasó con los duplicados?).
numeros = {1,2,2,3,4,4}
print(numeros) # {1, 2, 3, 4}  los set no aceptan duplicados
# 7-Agrega "uva" a un set de frutas y luego elimínala.
frutas = {'pera','platano','manzana'}
frutas.add('uva')
print(frutas) # {'platano', 'uva', 'pera', 'manzana'}
frutas.discard('uva')
print(frutas) # {'pera', 'platano', 'manzana'}

# 8-Dado A={1,2,3} y B={3,4,5}, encuentra su unión e intersección.
A={1,2,3}
B={3,4,5}
print(A | B) # {1, 2, 3, 4, 5}
print(A & B)  # {3}

# 9-Verifica si {1,2} es subconjunto de {1,2,3,4}.
a = {1,2}
b = {1,2,3,4}
print(a.issubset(b)) # True

# 10-Usa un set para eliminar duplicados de la lista [1,2,2,3,3,4,5].
numeros = [1,2,2,3,3,4,5]
nuevos_numeros = set(numeros)
print(nuevos_numeros) # {1, 2, 3, 4, 5}