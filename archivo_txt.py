from pathlib import Path

base = Path('.') # ruta actual
notas = base/'data'/'notas.txt' # construye rutas de forma segura
print(notas.resolve()) # convierte a ruta absoluta


# Texto a agregar
nueva_linea = 'En base de datos me gusta postgres'

# Leer la última línea del archivo (si existe)
ultima_linea = ''
try:
    with open('Archivo.txt', mode='r', encoding='utf-8') as f:
        lineas = f.readlines()
        if lineas:
            ultima_linea = lineas[-1].strip()  # Quita saltos de línea
except FileNotFoundError:
    pass  # El archivo no existe aún

# Solo agregar si la última línea es diferente
if ultima_linea != nueva_linea:
    with open('Archivo.txt', mode='a', encoding='utf-8') as f:
        if lineas and not lineas[-1].endswith('\n'):
            f.write('\n')  # Asegura salto de línea si hace falta
        f.write(nueva_linea + '\n')

# Leer e imprimir el contenido actualizado del archivo
with open('Archivo.txt', mode='r', encoding='utf-8') as f:
    contenido = f.read()
    print(contenido)
f.close()
