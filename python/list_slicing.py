# lista slicing

tienda = ['Camisas','Tenis','Calcetas','Pantalones']



# copiar lista
nueva_tienda = tienda[:]

nueva_tienda[0] = 'Playera'
print(nueva_tienda)
print(tienda)
# ['Playera', 'Tenis', 'Calcetas', 'Pantalones']
# ['Camisas', 'Tenis', 'Calcetas', 'Pantalones']

numeros = [0, 1, 2, 3, 4, 5, 6]
print(numeros[2:5])   # [2, 3, 4]
print(numeros[:3])    # [0, 1, 2]
print(numeros[::2])   # [0, 2, 4, 6]


frutas = ["manzana", "pera", "uva"]
for fruta in frutas:
    print(fruta)
