### Expresiones Regulares ###

import  re
my_string = "Esta es la leccion numero 7: leccion llamada Expresiones Regulares"
my_other_string = "Esta no es la leccion numero 6: Manejo de ficheros"

match = re.match("Esta es la leccion", my_string,re.I)
print(match)
# <re.Match object; span=(0, 18), match='Esta es la leccion'>
if match is not None:
    start, end = match.span()
    print(my_string[start:end]) # Esta es la leccion
else:
    print("No se encontró coincidencia")

match = re.match("Esta no es la leccion", my_other_string)
if match is not None:
    print(match)
    # <re.Match object; span=(0, 21), match='Esta no es la leccion'>
    start, end = match.span()
    print(my_other_string[start:end]) # Esta no es la leccion

#print(re.match("Expresiones Regulares", my_string))

# Search
search = re.search("leccion", my_string,re.I)
print(search)
# <re.Match object; span=(11, 18), match='leccion'>
if search is not None:
    start, end = search.span()
    print(my_string[start:end]) # leccion
else:
    print("No se encontró coincidencia")

# findall
findall = re.findall("leccion", my_string,re.I)
print(findall) # ['leccion', 'leccion']

# split
print(re.split("\n", my_string))
# ['Esta es la leccion numero 7: leccion llamada Expresiones Regulares']
print(re.split(":", my_string))
# ['Esta es la leccion numero 7', ' leccion llamada Expresiones Regulares']

# sub
print(re.sub("Expresiones", "expresiones", my_string))
# Esta es la leccion numero 7: leccion llamada expresiones Regulares


#### Ejercicios ####
# 1. Busca si una cadena empieza por "Hola".
texto = "Hola mundo"
patron = "Hola"

if re.match(patron, texto):
    print("si, empieza con Hola") # si, empieza con Hola
else:
    print("No empieza con Hola")

# 2. Busca la palabra "Python" en una cadena aunque estan en minusculas.
texto = "Hola Gerardo, bienvenido al mundo de python"
patron = "Python"
resultado = re.findall(patron,texto,re.IGNORECASE)
if resultado:
    print(f"Patron encontrado {resultado}") # Patron encontrado ['python']
else:
    print("No se encontro el pátron")

# 3. Encuentra todas las apariciones de la palabra "curso" en una cadena.
texto = "Bienvenido al curso de Python, en este curso encontraras el mejor curso"
patron = "curso"
resultado = re.findall(patron,texto)
if resultado:
    print(resultado) # ['curso', 'curso', 'curso']
else:
    print("No se encontro coincidencia")

# 4. Reemplaza todas las apariciones de "leccion" por "LECCION".
texto = "En esta leccion de python te superaras, Encontraras una buena leccion"
nuevo_texto = re.sub(r"leccion", "LECCION", texto)
print(nuevo_texto) # En esta LECCION de python te superaras, Encontraras una buena LECCION

# 5. Divide un texto en partes separadas por comas.
texto = "Hola Gerardo: bienvenido al mundo de Python"
resultado = re.split(":", texto)
print(resultado) # ['Hola Gerardo', ' bienvenido al mundo de Python']

# 6. Busca la primera palabra que comience con "A" o "a".
texto = "Hoy aprendí algo sobre Algoritmos y análisis."
coincidencia = re.search(r"\b[aA]\w*", texto)
if coincidencia:
    print("Primera palabra que comienza con A o a:", coincidencia.group())
    # Primera palabra que comienza con A o a: aprendí
else:
    print("No se encontró ninguna palabra que comience con A o a.")

# 7. Encuentra todas las palabras en una cadena que terminen en "cion".
texto = "trabaja mas con esta coleccion y pasa a la accion "
palabras = re.findall(r"\b\w*cion\b", texto)
if palabras:
    print(palabras) # ['coleccion', 'accion']
else:
    print("No se encontro la palabra")

# 8. Verifica si una cadena contiene solo numeros.
texto = "123456789"
if re.fullmatch(r"\d+", texto):
    print("La cadena contiene solo numeros")
    # La cadena contiene solo numeros
else:
    print("La cadena no contiene solo numeros")

# 9. Reemplaza todos los numeros de una cadena por el texto "[numero]".
texto = "Estoy aprendiendo 1 lenguaje de programacion y 1 de base de datos"
nuevo_texto = re.sub(r"\d","[numero]", texto)
print(nuevo_texto)
# Estoy aprendiendo [numero] lenguaje de programacion y [numero] de base de datos


# 10. Encuentra todas las palabras de 4 letras exactas en una cadena.
texto = "Esta frase tiene solo unas pocas palabras"
palabra_cuatro = re.findall(r"\b\w{4}\b", texto)
print(palabra_cuatro) # ['Esta', 'solo', 'unas']

texto = "Mi número es 123-456-789"
nuevo_texto = re.sub(r"\d", "*", texto)  # Reemplaza todos los dígitos con "*"
print(nuevo_texto) # Mi número es ***-***-***

texto = "Mi fecha de nacimiento es 29/03/1981"
patron = r"(\d{2})/(\d{2})/(\d{4})"

resultado = re.search(patron, texto)
if resultado:
    print("Día:", resultado.group(1)) # Día: 29
    print("Mes:", resultado.group(2)) # Mes: 03
    print("Año:", resultado.group(3)) # Año: 1981
else:
    print("No se encontró una fecha válida en el texto.")


correo = "gerardo123@example.com"
patron = r"^[\w\.-]+@[\w\.-]+\.\w+$"

if re.match(patron, correo):
    print("Correo válido ") # Correo válido
else:
    print("Correo inválido")


# Escribe un patrón para validar números de teléfono en el formato:
telefono = "(33) 10-53-39-21"
patron = r"^\(\d{2}\) \d{2}-\d{2}-\d{2}-\d{2}$"
if re.match(patron, telefono):
    print("Telefono valido") # Telefono valido
else:
    print("Telefono invalido")

# Extrae todos los precios usando expresiones regulares.
texto = "El auto cuesta 12000 pesos y la moto 8000 pesos"
numeros = re.findall(r"\d+", texto)
print(numeros) # ['12000', '8000']

# Crea un patrón que detecte todas las palabras que comienzan con mayúscula en un texto.
texto = "La Cadena contiene solo numeros"
Mayusculas = re.findall(r"\b[A-Z][a-zA-Z]*\b", texto)
print(Mayusculas) # ['La', 'Cadena']

# Reemplaza todas las vocales de un texto por *.
texto = "Bienvenido a python"
remplasar = re.sub(r"[aeiou]", "*", texto)
print(remplasar)  # B**nv*n*d* * pyth*n

"""
Valida si una contraseña es segura:
- Mínimo 8 caracteres
- Al menos una mayúscula
- Al menos un número
- Al menos un carácter especial
"""
def es_contrasena_segura(contrasena):
    patron = r'^(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()_+\-=\[\]{};\'":\\|,.<>\/?]).{8,}$'
    return bool(re.match(patron, contrasena))
print(es_contrasena_segura("Abcdef1!"))  # True
print(es_contrasena_segura("abcdefg1!")) # False (no mayúscula)
