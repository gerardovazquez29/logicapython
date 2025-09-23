inventary = {
    "chocolate": 10,
    "gomitas": 5,
    "paleta": 8,
    "chicle": 2,
    "mexicano": 8,
    "galleta": 12
}
cart = []
opcion = ""
print("Bienvenido a la tienda de dulces, DevCandy!")
print("Inventario: ")
while opcion != "6":
    print()
    print("*"*30)
    print("Carrito de Compras:")
    print("Opciones:")
    print("1. Mostrar el inventario")
    print("2. Agregar producto")
    print("3. Eliminar producto del carrito")
    print("4. mostrar carrito")
    print("5. Vaciar carrito")
    print("6. Salir")
    print("*"*30)

    opcion = input("Ingrese la opcion del (1 al 5) para su carrito: ")

    if opcion == "1":
        print("Nuestro Inventario:")
        for key, value in inventary.items():
            print(f"{key.capitalize()}:{value}")
    
    if opcion == "2":
        producto = input("Agrega el producto: ").lower()
        cantidad = int(input("Agrega la cantidad: "))
        if producto in inventary:
            if inventary[producto] >= cantidad:
                cart.append({"producto":producto, "cantidad":cantidad})   
                inventary[producto] -= cantidad
                print("Producto y cantidad agregados a tu carrito")
            else:
                print("No hay suficiente stock disponible")
        else:
            print("Producto no disponible en el inventario") 

    if opcion == "3":
        producto = input("Ingrese el producto a eliminar del carrito: ")
        cantidad = int(input("ingrese la cantidad del producto a eliminar del carrito: "))
        
        producto_encontrado = False
        for item in cart:
          if item['producto'] == producto:
           producto_encontrado = True
           
           if item["cantidad"] >= cantidad:
               inventary[producto] += cantidad
               if item["cantidad"] == cantidad:
                   cart.remove(item)
                   print(f"se elimino la cantidad de {cantidad} del producto {producto}")

    if opcion == "4":
        print("Tu carrito contiene: ")   
        for item in cart:
            print(f"{item['producto']}: {item['cantidad']}")

    if opcion == "5":
        producto = input("Deseas eliminar el carrito: 'si', 'no':  ").lower()
        if producto == "si":
            producto = cart.clear()
            print(f"El carrito ha sido eliminado correctamente: {cart}")
        elif producto == "no":
            print(f"El carrito no se Elimino: {cart}")
        else:
            print('opcion no valida')   
    
else:
    print("Hata luego Muchas gracias por comprar en dulcerias DevCandy!")   

for item in cart:
    print(f"{item['producto']}: {item['cantidad']}")
