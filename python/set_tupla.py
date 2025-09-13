
my_tuple = (1, 2, 3, 4, "Hola", True, 2, "Hi", 5, 4, 3, 2)
print(my_tuple)

# Ordenada
# INMUTABLES
# Permite duplicados
# Indexadas

# Métodos
# .count()
# print(my_tuple.count(2))

#
# print(my_tuple.index(2))

# my_tuple[4] = "Mundo" # ESTO NO SE PUEDE
new_tuple = my_tuple[4]

print(new_tuple)

week = ('Lunes', 'Martes', 'Miercoles', 'Jueves',
        'Viernes', ' Sabado', 'Domingo')



my_set = {1, 2, 3, 5, 4, 3, 2, 1, 3, 9, 7, 3, 8}

# Colección desordenada
# No tiene indices
# No permite duplicados
# óptimo para operaciones matemáticas

print(my_set)

usernames = {"ricardo123", "fernando123", "devi", "devi"}
print(usernames)


# Conjuntos

# .add()
my_set = {1, 2, 3}
my_set.add(6)
my_set.add(3)
my_set.add(5)
print(my_set)

# .remove() Elimina un elemento, pero da error sino existe
my_set.remove(2)
my_set.remove(6)
print(my_set)

# .discard() No marca error si no existe
my_set.discard(3)
my_set.discard(3)
my_set.discard(7)

print(my_set)

# .pop() Elimina un elemento al azar y lo devuelve

print(my_set.pop())
print(my_set)


# set1.union(set2)
set1 = {1, 2, 3}
set2 = {4, 5, 6}

union_set = set1.union(set2)
# print(union_set)

# set1.intersection(set2)
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
intersection = set1.intersection(set2)
# print(intersection)

# set1.difference(set2)
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
difference = set2.difference(set1)
print(difference)


# set1.symmetric_difference(set2)
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

symmetric_difference = set1.symmetric_difference(set2)
# print(symmetric_difference)

# set1.issubset(set2) True o False
set1 = {1, 2}
set2 = {1, 2, 3, 4}
# print(set2.issubset(set1))

# set1.issuperset(set2)
set1 = {1, 2, 3, 4}
set2 = {1, 2}
print(set2.issuperset(set1))


python_course = {'Ana', 'Luis', 'Maria', 'Pedro'}
java_course = {'Pepito', 'Pedro', 'Carlos', 'Ricardo'}

two_courses = python_course.intersection(java_course)
# print(two_courses)

only_python = python_course.difference(java_course)
# print(only_python)

all_students = python_course.union(java_course)
print(all_students)


list1 = [1, 2, 3, 4, 2, 3, 4, 5, 1, 2, 5, 6, 2, 4, 9, 10]
tuple1 = tuple(list1)
# print(list1)
# print(tuple1)

set1 = set(tuple1)
# print(set1)


list_tuple = [('a', 1), ('b', 2), ('c', 3)]
dictionary = dict(list_tuple)
print(dictionary)

