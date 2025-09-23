# Instrucciones:
# crear un programa de evaluacion de candidatos potenciales con conocimiento 
# en python para RH.
# obtener el nombre, años de experiencia y habilidades.
# Evaluar:
# Si el candidato sabe Python/Dyango, tiene +3 años de experiencia: Candidato optimo.
# Si el candidato sabe Python/Dyango, tiene +1 año de experiencia: buen Candidato.
# Si el candidato sabe Python/Dyango, Posible Candidato
# Si el candidato No sabe Python: No optimo, se guardara CV

# Consejo: Ocupa los metodos .split()

nombre = input("Nombre del candidato: ")
experiencia = int(input("Años de experiencia: "))
Habilidades = input("Habilidades del candidato: ").split(",")

evaluacion = "Python" in Habilidades or "Dyango" in Habilidades

resultado = ""
if evaluacion:
    if experiencia >= 3:
        resultado = "Candidato optimo"
    elif experiencia >= 1:
        resultado = "Buen Candidato"
    else:
        resultado = "Posible Candidato"
else:
    resultado = "No optimo, se guardara CV"

print(f"El Candidato: {nombre} es: {resultado}")

#  El Candidato: Santiago es: Buen Candidato

