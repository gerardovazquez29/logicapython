## LAMBDAS ##

suma = lambda primer_valor, segundo_valor: primer_valor + segundo_valor
print(suma(3, 4)) # 7


# 1. Crea una lambda que sume dos numeros.
suma = lambda primer_valor, segundo_valor: primer_valor + segundo_valor
print(suma(3, 3)) # 6

# 2. Crea una lambda que calcule el cuadrado de un numero.
cuadrado = lambda numero: numero **2 
print(cuadrado(3)) # 9

# 3. Crea una lambda que devuelva el mayor de dos numeros.
mayor = lambda a,b: max(a,b)
print(mayor(6,8)) # 8

# 4. Crea una lambda que sume 10 a un numero dado.
suma_numero = lambda numero: numero + 10
print(suma_numero(7)) # 17

# 5. Crea una lambda que devuelva el ultimo caracter de una cadena.
ultimo_caracter = lambda texto : texto[-1] # slicing - 1 accedes al ulimo
print(ultimo_caracter("cadena")) # a

# 6. Crea una lambda que indique si una palabra tiene mas de 6 letras.
mas_letras = lambda palabra : len(palabra) > 6
print(mas_letras("mas")) # False

# 7. Crea una lambda que convierta una cadena a minusculas.
cadena = lambda palabras: palabras.lower()
print(cadena("TODOS SON PARDOS")) # todos son pardos

# 8. Crea una lambda que devuelva True si un numero es positivo.
positivo = lambda numero : numero > 0
print(positivo(5)) # True

# 9. Crea una lambda que devuelva "Cadena vacia" si el string esta vaci­o.
cadena_vacia = lambda palabras : "Cadena vacia" if palabras == "" else palabras
print(cadena_vacia("Hola")) # Cadena vacia 

# 10. Crea una lambda que calcule el precio final con un impuesto añadido del 21%.
impuesto = lambda precio : precio * 1.21
print(impuesto(22)) # 26.619999999999997