import csv

encabesado = ["id", "name", "age", "email"]
Datos = [
    {"id": 1, "name": "Ana", "age": 28, "email": "ana@example.com"},
    {"id": 2, "name": "Luis", "age": 34, "email": "luis@example.com"},
    {"id": 3, "name": "Gerardo", "age": 44, "email": "gerardo@example.com"},
    {"id": 3, "name": "Santiago", "age": 40, "email": "santiago@example.com"},
]

# Crear y sobrescribir (modo 'w')
with open("usuarios.csv", "w", newline="", encoding="utf-8") as archivo:
    writer = csv.DictWriter(archivo, fieldnames=encabesado)
    writer.writeheader()
    writer.writerows(Datos)
    print(Datos)
    # [{'id': 1, 'name': 'Ana', 'age': 28, 'email': 'ana@example.com'}, 
    # {'id': 2, 'name': 'Luis', 'age': 34, 'email': 'luis@example.com'}, 
    # {'id': 3, 'name': 'Gerardo', 'age': 44, 'email': 'gerardo@example.com'}, 
    # {'id': 3, 'name': 'Santiago', 'age': 40, 'email': 'santiago@example.com'}]

# El archivo se cierra automáticamente al salir del with.
# Comentario: writer.writerows espera listas/tuplas; la primera fila suele ser el header.


# Leer un csv

with open("usuarios.csv", "r", newline="", encoding="utf-8") as archivo:
    reader = csv.DictReader(archivo) # automáticamente usa la primera fila como header
    for Datos in reader:
        print(Datos["id"], Datos["name"])  # acceso por nombre de columna
        """
        1 Ana     
        2 Luis    
        3 Gerardo 
        3 Santiago
        """
