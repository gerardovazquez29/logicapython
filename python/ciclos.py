

# Es una estructura que se puede reoetir varias veces
for item in "python":
    print(item)
#p
#y
#t
#h
#o
#n 
fruits = ["manzana", "platano", "sandia"]
for fruit in fruits:
    print(fruit)    
"""
manzana
platano
sandia
"""   
my_list = [1,2,3,4,5]
sum = 0
for number in my_list:
    print(number)
    sum += number
print(sum)
"""
1
2
3
4
5
15
"""
user = {
    'name': 'Gerardo',
    'age': 44,
    'can_swin': False
}
for item in user:
    print(item)
"""
name
age
can_swin
"""
for item in user.items():
    print(item)
"""
('name', 'Gerardo')
('age', 44)
('can_swin', False)
"""
for key, value in user.items():
    print(key, value)
"""
name Gerardo
age 44
can_swin False
"""

persona = {"nombre": "Ana", "edad": 25}
for clave, valor in persona.items():
    print(clave, ":", valor)
""" nombre : Ana
edad : 25 """

# Bucles anidados
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)


# Iterando con range
for number in range(0,10):
    print(number) # 0 => 9

for _ in range(0,10):
    print("enviar notificacion")  # enviar notificacion * 10

# Enumerate
for index, char in enumerate('Devtalles'):
    print(index, char)  # funciona tambien con numeros
"""
0 D
1 e
2 v
3 t
4 a
5 l
6 l
7 e
8 s
"""
for index, number in enumerate(list(range(100))):
    print(index, number) # del 0 al 99 

colores = ["rojo", "verde", "azul"]
for indice, color in enumerate(colores):
    print(indice, color)
""" 
0 rojo
1 verde
2 azul  """


# While

#while True:
#    print("nunca se detendra") # ciclo infinito
counter = 1
while counter <= 5:
    print(f"Number: {counter}")
    counter += 1
else:
    print("Terminamos")
"""
Number: 1
Number: 2
Number: 3
Number: 4
Number: 5
Terminamos
"""
response = ''
while response.lower() != 'python':
    response = input("Escribe python para salir: ")

print("Terminamos")

# pass break continue
# pass 
for item in [1,2,3,4,5]:
    pass

# break
for item in [1,2,3,4,5]:
    print(item) # 1
    break

# continue
number = 0
while number < len([1,2,3,4,5]):
    number += 1
    print(number) # 12345

# For es para iterables, y cuando sabemos cuando terminara.

my_list = [1,2,3,4,5,6,7,8,9]

for item in my_list:
    print(item) # 123456789

print("-"*30)

# while es para cuando no sabemos cuando terminara y necesitamos una condicion.
item = 1
while item < len(my_list):
    print(item) # 123456789
    item += 1

print("-"*30)

# listas anidadas
nested_list = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
for sublist in nested_list:
    print(sublist)
"""     
[1, 2, 3]
[4, 5, 6]
[7, 8, 9] 
"""

# aqui te da todos los numeros
for sublist in nested_list:
    for item in sublist:
        print(item, end=" ") # 123456789


# diccionarios anidados

nested_dict = {
    "persona1": {"nombre": "Gerardo", "edad": "44", "ciudad": "Guadalajara"},
    "persona2": {"nombre": "Santiago", "edad": "40", "ciudad": "Tlaquepaque"},
    "persona3": {"nombre": "Fani", "edad": "28", "ciudad": "Tlajomulco"}
}
for key, value in nested_dict.items():
    print(f"{key}")
    for sub_key, sub_value in value.items():
        print(f"{sub_key}: {sub_value}")
"""
persona1     
nombre: Gerardo
edad: 44
ciudad: Guadalajara
persona2
nombre: Santiago
edad: 40
ciudad: Tlaquepaque
persona3
nombre: Fani
edad: 28
ciudad: Tlajomulco 
"""    
