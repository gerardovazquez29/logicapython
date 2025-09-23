# uso de split()

texto = "Python;Java;JavaScript;C++"
lenguajes = texto.split(";")
for lenguaje in lenguajes:
    print(f"- {lenguaje}")

"""
- Python
- Java      
- JavaScript
- C++ 
"""

email = "usuario@example.com"
usuario, dominio = email.split("@")
print(f"Usuario: {usuario}, Dominio: {dominio}")
#  Usuario: usuario, Dominio: example.com

linea_csv = "Juan,Pérez,25,Ingeniero"
datos = linea_csv.split(",")
nombre, apellido, edad, profesion = datos
print(f"Nombre: {nombre}, Edad: {edad}")
#  Nombre: Juan, Edad: 25

