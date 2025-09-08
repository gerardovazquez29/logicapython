
# suma de dos numeros
num1 = int(input( "Ingresa el primer numero: "))
num2 = int(input("Ingresa el segundo numero: "))
suma = num1 + num2
print(f"La suma es: {suma}")


# Numero par o impar
num = int(input("Ingresa un numero: "))
if num % 2 == 0:
    print(f"El numero: {num} es par")
else:
    print(f"El numero: {num} es impar")


# Recibas de forma dinamica nombre, año nacimiento, correo y contraseña

"""
nombre: Gerardo
Email: gerardo@correo.com
tendras 55 años en el 2050
tu contraseña es: *****  
"""

nombre = input("Ingresa tu nombre: ")
email = input("Ingresa tu correo electronico: ")
anio_nacimiento = int(input("Ingresa tu año de nacimiento: "))
contraseña = input("Ingresa tu contraseña: ")


anio_2050 = 2050 - anio_nacimiento

contraseña_modificada = '*' * len(contraseña)

print(f"""
Nombre: {nombre}
Email: {email}
Tendras {anio_2050} años en el 2050
Tu contraseñaes:{contraseña_modificada}
""")
"""
Nombre: Santiago
Email: neowhatup@gmail.com
Tendras 69 años en el 2050
Tu contraseñaes:**************
"""

