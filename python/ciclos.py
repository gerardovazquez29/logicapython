

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

