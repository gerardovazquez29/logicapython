# Ejercicios para Practicar Diccionarios

# 1- Crea un diccionario con tu nombre, edad y ciudad.
#    Muestra solo tu ciudad usando la clave.
persona = {
    'nombre': 'Gerardo',
    'edad': 44,
    'ciudad': 'Tlaquepaque'
}
print(persona['ciudad']) # Tlaquepaque

# 2 - Añade una nueva clave “lenguaje favorito” a ese diccionario.
persona.update({'lenguaje faborito':'python'})
print(persona)
# {'nombre': 'Gerardo', 'edad': 44, 'ciudad': 'Tlaquepaque', 'lenguaje faborito': 'python'}

# 3 - Elimina la clave “edad” del diccionario y muestra el resultado.
persona.pop('edad')
print(persona)
# {'nombre': 'Gerardo', 'ciudad': 'Tlaquepaque', 'lenguaje faborito': 'python'}


# 4 - Recorre un diccionario de frutas con sus precios y muestra cada uno en formato:
#       "Fruta: Precio".
frutas = {
    'manzana':29,
    'pera':35,
    'platano':25,
    'fresa': 42 
        }
for clave,valor  in frutas.items():
    print(f"{clave}: {valor}")
"""
manzana: 29
pera: 35
platano: 25
fresa: 42
"""


# 5 - Crea un diccionario con 5 países y sus capitales.
        #ingresa un país y muestra su capital.
paises = {
    'Mexico':'df',
    'Canada':'toronto',
    'Rusia':'moscu',
    'China':'pekin',
    'Brasil':'sao paulo'
}
print(paises['Rusia']) # moscu

# 6 - Usa dict comprehension para crear un diccionario con los números del 1 al 5 y sus cubos.
cubos = {numeros: numeros**3 for numeros in range(1,6)}
print(cubos)
 # {1: 1, 2: 8, 3: 27, 4: 64, 5: 125}

# 7 - Crea un inventario con al menos 3 productos.
      #Resta 1 a la cantidad de un producto al “venderlo”.
productos = {
    'rollo':39,
    'servilletas':25,
    'tortillas':13
    }
productos['tortillas'] -= 1
print(productos) # {'rollo': 39, 'servilletas': 25, 'tortillas': 12}

# 8 - Crea un diccionario anidado que guarde datos de 2 estudiantes (nombre, edad, calificación).
        #Muestra la calificación del segundo estudiante.
estudiantes = {
    'est1': {'nombre':'Gerardo',
            'edad':25,
            'calificacion': 8.9
            },
    'est2': {
        'nombre':'Santiago',
        'edad':22,
        'calificacion':8.5
    }
}
print(estudiantes['est2']['calificacion']) # 8.5


# 9 - Escribe una función que reciba un diccionario y muestre todas sus claves y valores.
def mostrar(dic):
    for clave,valor in dic.items():
        print(f"{clave}:{valor}")
mostrar({"nombre":"Santiago","edad":44})
"""
nombre:Santiago
edad:44
"""

# 10 - Simula un carrito de compras con un diccionario.
        # Agrega productos con sus precios.
        # Calcula el total de la compra.
carrito = {
    'desodorante':48,
    'perfume':350,
    'playera':120,
    'pantalon':500
}
total = sum(carrito.values())
print(f"Total a pagar es: ${total}") # Total a pagar es: $1018

