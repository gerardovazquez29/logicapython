# Crearás un carrito de compras que haga las siguientes funcionalidades:
# Agregar producto
# Eliminar producto
# Mostrar la lista ordenada
# Buscar producto
# Contar productos del carrito
# Vaciar el carrito

shopping_cart = ['Laptop', 'Vaso', 'Cafe', 'Audifonos']
option = ""
while option != "7":
    print()
    print("*"*30)
    print("Carrito de compras")
    print("Opciones: ")
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Mostrar la lista ordenada")
    print("4. Buscar producto")
    print("5. Contar productos del carrito")
    print("6. Vaciar el carrito")
    print("7. Salir")
    print("*"*30)

    option = input("Elige una opcion (1-7): ")
    if option == "1":
        product = input("agrega un nuevo producto: ").capitalize()
        if product not in shopping_cart:
            shopping_cart.append(product)
            print("Producto añadido correctamente")
        else:
            print("producto ya existe en el inventario")

    elif option == "2":
        product = input("Ingresa el producto que quieras eliminar: ").capitalize()
        if product in shopping_cart:
            shopping_cart.remove(product)
            print(f"El producto: {product} ha sido eliminado correctamente" )
            print(shopping_cart)
        else:
            print("producto no encontrado")

    elif option == "3":
        print("Lista de Productos Ordenados: ")
        product = sorted(shopping_cart)
        print(product)

    elif option == "4":
        product = input("Ingresa el Producto que Buscas: ").capitalize()
        if product in shopping_cart:
            print(f"El Producto: {product} esta en la lista")
        else:
            print("Producto no encontrado")

    elif option == "5":
        product = len(shopping_cart)
        print(f"El total de Productos es de: {product} ")

    elif option == "6":
        product = input("Deseas eliminar el carrito: 'si', 'no':  ")
        if product == "si":
            product = shopping_cart.clear()
            print(f"el carrito ha sido Eliminado correctamente: {product} ")
        elif product == "no":
            print(f"El carrito no se Elimino: {shopping_cart}")

    else:
        print('opcion no valida')
           
else: 
    print("Hasta luego. muchas Gracias")
