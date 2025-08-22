
def sum_one(value):
    return value + 1
def sum_two_value_and_add_one(first_value, second_value):
    return sum_one(first_value + second_value)
print(sum_two_value_and_add_one(5,2))


# 1. Crea una funcion que reciba 
# una funcion y un numero, y devuelva el resultado de aplicar 
# la funcion al numero.
def aplicar_funcion(f, n):
    return f(n)
def cuadrado(x):
    return x*x
resultado = aplicar_funcion(cuadrado, 5)
print(resultado) # 25

# 2. Crea una funcion que reciba dos numeros y una funcion, 
# y devuelva el resultado de sumar los dos numeros y aplicar la funcion.
def aplica_num_funcion(f,n,m):
    suma = n + m
    return f(suma)
def multiplicacion(valor):
    return valor * 2
resultado = aplica_num_funcion(multiplicacion, 2, 3)
print(resultado) # 10

# 3. Crea una funcion que devuelva otra funcion que sume un numero fijo.
def creando_sumador(num_fijo):
    def sumador(x):
        return x + num_fijo
    return sumador
sumar_seis = creando_sumador(6)
print(sumar_seis(7)) # 13

# 4. Usa map() con lambda para multiplicar cada numero de una lista por 10.
lista = [2,3,4,5]
multiplicar_numero = list(map(lambda x: x * 10, lista))
print(multiplicar_numero) # [20, 30, 40, 50]

# 5. Usa filter() con lambda para quedarte solo con los numeros pares.
numeos_pares = list(filter(lambda x: x % 2 == 0, range(10)))
print(numeos_pares) # [0, 2, 4, 6, 8]

# 6. Usa reduce() con lambda para obtener la suma total de una lista.
from functools import reduce
lista_precios = [100, 150, 250]
suma_total = reduce(lambda x,y: x + y, lista_precios)
print(suma_total) # 500

# 7. Escribe una funcion que devuelva una funcion que reciba un nombre y 
# devuelva un Hola, y el nombre.
def crear_saludo():
    def saludar(nombre):
        return f"Hola, {nombre}"
    return saludar
saludo_funcion = crear_saludo()
print(saludo_funcion("Gerardo")) # Hola, Gerardo

# 8. Crea una funcion que reciba una lista y una funcion, y 
# cuente cuantos elementos cumplen con la funcion.
def contar_cumplen(lista, funcion):
    contador = 0
    for elemento in lista:
        if funcion(elemento):
            contador += 1
    return contador
numeros = [1,2,3,4,5,6]
es_par = lambda x: x % 2 == 0
print(contar_cumplen(numeros, es_par)) # 3

# 9. Crea una funcion que reciba dos funciones y un numero, y las aplique en orden.

# 10. Crea una funcion que reciba una lista y una funcion, y 
# aplique esa funcion a cada elemento usando un bucle (sin map).

# 11. Crea una función que devuelva una función que reciba un 
# número y devuelva el doble de ese número.
def crear_doblador():
    def doblar(numero):
        return numero * 2
    return doblar
doblador_funcion = crear_doblador()
print(doblador_funcion(7)) # 14

# 12. Crea una función que reciba una lista y una función, y devuelva una 
# nueva lista solo con los elementos que cumplen la condición.
def filttrar_lista(lista, funcion):
    return [elemento for elemento in lista if funcion(elemento)]

print(filttrar_lista(numeros, es_par)) # [2, 4, 6]
