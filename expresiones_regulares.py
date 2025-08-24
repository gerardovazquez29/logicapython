### Expresiones Regulares ###

import  re
my_string = "Esta es la leccion numero 7: leccion llamada Expresiones Regulares"
my_other_string = "Esta no es la leccion numero 6: Manejo de ficheros"

match = re.match("Esta es la leccion", my_string,re.I)
print(match)
# <re.Match object; span=(0, 18), match='Esta es la leccion'>
start, end = match.span()
print(my_string[start:end]) # Esta es la leccion

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
start, end = search.span()
print(my_string[start:end]) # leccion

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

# 2. Busca la palabra "Python" en una cadena aunque estan en minusculas.

# 3. Encuentra todas las apariciones de la palabra "curso" en una cadena.

# 4. Reemplaza todas las apariciones de "leccion" por "LECCION".

# 5. Divide un texto en partes separadas por comas.

# 6. Busca la primera palabra que comience con "A" o "a".

# 7. Encuentra todas las palabras en una cadena que terminen en "cion".

# 8. Verifica si una cadena contiene solo numeros.

# 9. Reemplaza todos los numeros de una cadena por el texto "[numero]".

# 10. Encuentra todas las palabras de 4 letras exactas en una cadena.

