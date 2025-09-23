
my_tuple = (1, 2, 3, 4, "Hola", True, 2, "Hi", 5, 4, 3, 2)
print(my_tuple) # (1, 2, 3, 4, 'Hola', True, 2, 'Hi', 5, 4, 3, 2)

# Ordenada
# INMUTABLES
# Permite duplicados
# Indexadas

# Métodos
# .count()
print(my_tuple.count(2)) # 3

#
print(my_tuple.index(2)) # 1

#my_tuple[4] = "Mundo" # ESTO NO SE PUEDE
new_tuple = my_tuple[4]

print(new_tuple) # Hola


# Desempaquetado
persona = ("Santiago", 25, "México")
nombre, edad, pais = persona
print(nombre, edad, pais)
# Santiago 25 México

# Metodos
datos = (1, 2, 6, 3)
print(datos.count(2))  # 1
print(datos.index(3))  # 3


my_set = {1, 2, 3, 5, 4, 3, 2, 1, 3, 9, 7, 3, 8}

# Colección desordenada
# No tiene indices
# No permite duplicados
# óptimo para operaciones matemáticas

print(my_set) # {1, 2, 3, 4, 5, 7, 8, 9}

usernames = {"ricardo123", "fernando123", "devi", "devi"}
print(usernames)  # {'ricardo123', 'devi', 'fernando123'}


# Conjuntos

# .add()
my_set = {1, 2, 3}
my_set.add(6)
my_set.add(3)
my_set.add(5)
print(my_set)  # {1, 2, 3, 5, 6}

# .remove() Elimina un elemento, pero da error sino existe
my_set.remove(2)
my_set.remove(6)
print(my_set) # {1, 3, 5}

# .discard() No marca error si no existe
my_set.discard(3)
my_set.discard(3)
my_set.discard(7)

print(my_set)  # {1, 5}    
  

# .pop() Elimina un elemento al azar y lo devuelve

print(my_set.pop()) # 1
print(my_set) # {5} 


# set1.union(set2)
set1 = {1, 2, 3}
set2 = {4, 5, 6}

union_set = set1.union(set2)
print(union_set)  # {1, 2, 3, 4, 5, 6}

# set1.intersection(set2)
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
intersection = set1.intersection(set2)
print(intersection)  # {3, 4}

# set1.difference(set2)
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
difference = set2.difference(set1)
print(difference)  # {5, 6}

diference1 = set1.difference(set2)
print(diference1)  # {1, 2}


# set1.symmetric_difference(set2)
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

symmetric_difference = set1.symmetric_difference(set2)
print(symmetric_difference)  # {1, 2, 5, 6}

# set1.issubset(set2) True o False
set1 = {1, 2}
set2 = {1, 2, 3, 4}
print(set2.issubset(set1))  # False

# set1.issuperset(set2)
set1 = {1, 2, 3, 4}
set2 = {1, 2}
print(set2.issuperset(set1))  # False


python_course = {'Ana', 'Luis', 'Maria', 'Pedro'}
java_course = {'Pepito', 'Pedro', 'Carlos', 'Ricardo'}

two_courses = python_course.intersection(java_course)
print(two_courses)  # {'Pedro'}

only_python = python_course.difference(java_course)
print(only_python)  # {'Maria', 'Ana', 'Luis'}

all_students = python_course.union(java_course)
print(all_students) # {'Maria', 'Carlos', 'Ricardo', 'Pepito', 'Ana', 'Pedro', 'Luis'}

# Converter

list1 = [1, 2, 3, 4, 2, 3, 4, 5, 1, 2, 5, 6, 2, 4, 9, 10]
tuple1 = tuple(list1)
print(list1) # [1, 2, 3, 4, 2, 3, 4, 5, 1, 2, 5, 6, 2, 4, 9, 10]
print(tuple1) # (1, 2, 3, 4, 2, 3, 4, 5, 1, 2, 5, 6, 2, 4, 9, 10)  

set1 = set(tuple1)
print(set1) # {1, 2, 3, 4, 5, 6, 9, 10}


list_tuple = [('a', 1), ('b', 2), ('c', 3)]
dictionary = dict(list_tuple)
print(dictionary)  # {'a': 1, 'b': 2, 'c': 3}

frutas = {"manzana", "pera", "uva"}
frutas.add("naranja")    # agrega
frutas.remove("pera")    # elimina, error si no existe
frutas.discard("mango")  # elimina sin error
frutas.pop()             # elimina un elemento aleatorio
frutas.clear()           # vacía el set


# Unión (| o .union()):
A = {1, 2, 3}
B = {3, 4, 5}
print(A | B)  # {1, 2, 3, 4, 5}

# Intersección (& o .intersection()):
print(A & B)  # {3}

# Diferencia (- o .difference()):
print(A - B)  # {1, 2}

# Diferencia simétrica (^ o .symmetric_difference()):
print(A ^ B)  # {1, 2, 4, 5}

# comprobaciones 
A = {1, 2}
B = {1, 2, 3}
print(A.issubset(B))   # True
print(B.issuperset(A)) # True
print(A.isdisjoint({4, 5})) # True
