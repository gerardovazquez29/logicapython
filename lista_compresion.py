### List Comprehension ###

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

### Challenges ###

"""
EL FAMOSO "FIZZ BUZZâ€:
Escribe un programa que muestre por consola (con un print) los
nÃºmeros de 1 a 100 (ambos incluidos y con un salto de lÃ­nea entre
cada impresiÃ³n), sustituyendo los siguientes:
- MÃºltiplos de 3 por la palabra "fizz".
- MÃºltiplos de 5 por la palabra "buzz".
- MÃºltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
"""


def fizzbuzz():
    for index in range(1, 101):
        if index % 3 == 0 and index % 5 == 0:
            print("fizzbuzz")
        elif index % 3 == 0:
            print("fizz")
        elif index % 5 == 0:
            print("buzz")
        else:
            print(index)


fizzbuzz()

"""
Â¿ES UN ANAGRAMA?
Escribe una funciÃ³n que reciba dos palabras (String) y retorne
verdadero o falso (Bool) segÃºn sean o no anagramas.
- Un Anagrama consiste en formar una palabra reordenando TODAS
  las letras de otra palabra inicial.
- NO hace falta comprobar que ambas palabras existan.
- Dos palabras exactamente iguales no son anagrama.
"""


def is_anagram(word_one, word_two):
    if word_one.lower() == word_two.lower():
        return False
    return sorted(word_one.lower()) == sorted(word_two.lower())


print(is_anagram("Amor", "Roma"))

"""
LA SUCESIÃ“N DE FIBONACCI
Escribe un programa que imprima los 50 primeros nÃºmeros de la sucesiÃ³n
de Fibonacci empezando en 0.
- La serie Fibonacci se compone por una sucesiÃ³n de nÃºmeros en
  la que el siguiente siempre es la suma de los dos anteriores.
  0, 1, 1, 2, 3, 5, 8, 13...
"""


def fibonacci():

    prev = 0
    next = 1

    for index in range(0, 50):
        print(prev)
        fib = prev + next
        prev = next
        next = fib


fibonacci()

"""
Â¿ES UN NÃšMERO PRIMO?
Escribe un programa que se encargue de comprobar si un nÃºmero es o no primo.
Hecho esto, imprime los nÃºmeros primos entre 1 y 100.
"""


def is_prime():

    for number in range(1, 101):

        if number >= 2:

            is_divisible = False

            for index in range(2, number):
                if number % index == 0:
                    is_divisible = True
                    break

            if not is_divisible:
                print(number)


is_prime()

"""
INVIRTIENDO CADENAS
Crea un programa que invierta el orden de una cadena de texto
sin usar funciones propias del lenguaje que lo hagan de forma automÃ¡tica.
- Si le pasamos "Hola mundo" nos retornarÃ­a "odnum aloH"
"""


def reverse(text):
    text_len = len(text)
    reversed_text = ""
    for index in range(0, text_len):
        reversed_text += text[text_len - index - 1]
    return reversed_text


print(reverse("Hola mundo"))