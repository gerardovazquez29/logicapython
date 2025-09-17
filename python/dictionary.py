user = {
    'name': 'Ricardo',
    'age': 29,
    'greet': 'Hola Mundo',
    'numbers': [1, 2, 3]
}

# .get()
# print(user.get('name'))

# in
print(user.values())
# dict_items([('name', 'Ricardo'), ('age', 29), ('greet', 'Hola Mundo'), ('numbers', [1, 2, 3])])
# print('Ricardo' in user)
# print('Ricardo' in user.keys())
# print('Hola Ricardo' in user.values())

print(user.items())
# {'name': 'Ricardo', 'age': 29, 'greet': 'Hola Mundo', 'numbers': [1, 2, 3]}


user = {
    'name': 'Ricardo',
    'age': 29,
    'greet': 'Hola Mundo',
    'numbers': [1, 2, 3]
}

# .copy()

user_copy = user.copy()
user_copy['age'] = 20
print(user)
# {'name': 'Ricardo', 'greet': 'Hola Mundo', 'numbers': [1, 2, 3]}
# print(user_copy)

# .pop()
user.pop('age')
print(user) # {'name': 'Ricardo', 'greet': 'Hola Mundo'}

# .popitem()
user.popitem()
print(user)
# {'name': 'Fernando', 'greet': 'Hola Mundo', 'cats': 2}

# .update()
user.update({'name': 'Fernando'})
user.update({'cats': 2})
print(user) 
# {'name': 'Fernando', 'greet': 'Hola Mundo', 'cats': 2, 'skills': ['Python', 'Django']}

# .append()
user['skills'] = user.get('skills', [])
user['skills'].append('Python')
user['skills'].append('Django')
print(user)

# Diccionario vacío
dic_vacio = {}

# Con datos iniciales
persona = {"nombre": "Ana", "edad": 30}

# Con dict()
persona2 = dict(nombre="Luis", edad=22)
persona2.update({'ciudad':'Guadalajara'}) # modifica un  diccionario
print(persona2) # {'nombre': 'Luis', 'edad': 22, 'ciudad': 'Guadalajara'}

mi_dic = {"nombre": "Santiago", "edad": 25, "lenguaje": "Python"}
print(mi_dic.get('nombre')) # Santiago

for clave in mi_dic:
    print(clave, mi_dic[clave])
    """
    nombre Santiago
    edad 25
    lenguaje Python
    """

for clave, valor in mi_dic.items():
    print(f"{clave}: {valor}")
    """
    nombre Santiago
    edad 25
    lenguaje Python
    """
dic = {"a": 1, "b": 2}

print(dic.keys())    # dict_keys(['a', 'b'])
print(dic.values())  # dict_values([1, 2])
print(dic.items())   # dict_items([('a', 1), ('b', 2)])

dic.update({"c": 3}) # Agregar múltiples
print(dic)           # {'a':1,'b':2,'c':3}

dic.clear()          # Vacía el diccionario

# Diccionarios anidados
usuarios = {
    "u1": {"nombre": "Ana", "edad": 25},
    "u2": {"nombre": "Luis", "edad": 30}
}
print(usuarios["u2"]["nombre"])  # Luis

# Comprensión de diccionarios (dict comprehension)
# Elevar al cuadrado cada número
numeros = [1, 2, 3, 4]
cuadrados = {n: n**2 for n in numeros}
print(cuadrados)  # {1:1, 2:4, 3:9, 4:16}


# Usar diccionarios como "mini bases de datos"

inventario = {"manzanas": 10, "peras": 5}

# Vender 2 manzanas
inventario["manzanas"] -= 2
print(inventario)  # {'manzanas': 8, 'peras': 5}


# Uso con funciones

def info_persona(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

info_persona(nombre="Ana", edad=28, ciudad="CDMX")
"""
nombre: Ana
edad: 28
ciudad: CDMX
"""

