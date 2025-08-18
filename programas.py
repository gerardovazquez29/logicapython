
### Challenges ###

"""
EL FAMOSO "FIZZ BUZZ:
Escribe un programa que muestre por consola (con un print) los
numeros de 1 a 100 (ambos incluidos y con un salto de li­nea entre
cada impresion), sustituyendo los siguientes:
- Multiplos de 3 por la palabra "fizz".
- Multiplos de 5 por la palabra "buzz".
- Multiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
"""


def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)


fizzbuzz()

"""
¿ES UN ANAGRAMA?
Escribe una funcion que reciba dos palabras (String) y retorne
verdadero o falso (Bool) segun sean o no anagramas.
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
LA SUCESION DE FIBONACCI
Escribe un programa que imprima los 50 primeros numeros de la sucesion
de Fibonacci empezando en 0.
- La serie Fibonacci se compone por una sucesion de numeros en
  la que el siguiente siempre es la suma de los dos anteriores.
  0, 1, 1, 2, 3, 5, 8, 13...
"""


def fibonacci():

    inicio = 0
    siguente = 1

    for i in range(0, 50):
        print(inicio)
        fib = inicio + siguente
        inicio = siguente
        siguente = fib
fibonacci()

"""
¿ES UN NUMERO PRIMO?
Escribe un programa que se encargue de comprobar si un numero es o no primo.
Hecho esto, imprime los numeros primos entre 1 y 100.
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
sin usar funciones propias del lenguaje que lo hagan de forma automatica.
- Si le pasamos "Hola mundo" nos retornarla "odnum aloH"
"""


def reverse(text):
    text_len = len(text)
    reversed_text = ""
    for index in range(0, text_len):
        reversed_text += text[text_len - index - 1]
    return reversed_text


print(reverse("Hola mundo"))
