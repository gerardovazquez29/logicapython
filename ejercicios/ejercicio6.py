inventario = {
    "chocolate": 10,
    "gomitas": 5,
    "paleta": 8,
    "chicle": 2,
    "mexicano": 8,
    "galleta": 12
}
cart = []

print("Bienvenido a la tienda de dulces, DevCandy!")
print("Inventario: ")

for dulces,precio in inventario.items():
    print(f"{dulces.capitalize()} - ${precio}")

while True:
    pedido = input("¿Que dulce te gustaria comprar?  (Escribe 'salir' para terminar)").lower()

    if pedido == 'salir':
        break

    if pedido in inventario:
        cart.append(pedido)
        print(f"su dulce: {pedido} a sido agregado a su carrito")
    else:
        print("dulce no encontrado en nuestro inventario")

Total = 0
print("Tu carrito")
for pedido in cart:
    print(f"{pedido.capitalize()} - ${inventario[pedido]}")
    Total += inventario[pedido]

print(f"Total a pagar: ${Total} ")

""" 
su dulce: galleta a sido agregado a su carrito
¿Que dulce te gustaria comprar?  (Escribe 'salir' para terminar)chicle
su dulce: chicle a sido agregado a su carrito
¿Que dulce te gustaria comprar?  (Escribe 'salir' para terminar)salir
Tu carrito
Chocolate - $10
Paleta - $8
Galleta - $12
Chicle - $2
Total a pagar: $32 
"""
