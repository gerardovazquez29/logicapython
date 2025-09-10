# Crearás un carrito de compras que haga las siguientes funcionalidades:
# Agregar producto
# Eliminar producto
# Mostrar la lista ordenada
# Buscar producto
# Contar productos del carrito
# Vaciar el carrito

print("Carrito de compras")
print("Opciones: ")
print("1. Agregar producto")
print("2. Eliminar producto")
print("3. Mostrar la lista ordenada")
print("4. Buscar producto")
print("5. Contar productos del carrito")
print("6. Vaciar el carrito")

shopping_cart = ['Laptop', 'Vaso', 'Cafe', 'Audifonos']
option = input("Elige una opcion (1-6): ")
shopping_cart1 = shopping_cart[:]

if option == "1":
    product_add = input("agrega un nuevo producto: ").capitalize()
    if product_add  not in shopping_cart:
        shopping_cart.append(product_add)
        print("Producto añadido correctamente")
    else:
        print("producto ya existe en el inventario")

elif option == "2":
    product_remove = input("Ingresa el producto que quieras eliminar: ").capitalize()
    if product_remove in shopping_cart1:
        shopping_cart1.remove(product_remove)
        print(f"El producto: {product_remove} ha sido eliminado correctamente" )
        print(shopping_cart1)
    else:
        print("producto no encontrado")
elif option == "3":
    pass
elif option == "4":
    pass
elif option == "5":
    pass
elif option == "6":
    pass
else:
    print("opcion no valida")
