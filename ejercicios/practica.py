
x = 5
y = 3
x = x + y
y = x - y
x = x - y
print(x,y)
#  3 5


nums = [1, 2, 3, 4]
nums.append(nums.pop(1)) # pop elimina 
print(nums) # append agrega al final
# [1, 3, 4, 2]


# Ejercicio
print("-"*20)

students = {
    "Ana": [8,7,9],
    "Luis": [6,5,7],
    "Sofia": [10,9,10]
}
# Agregar nuevos estudiantes
# Sacar el promedio de un estudiante existente
# El promedio del studiante nuevo

students.update({"Gerardo": [7,8,9]})
print(students)
# {'Ana': [8, 7, 9], 'Luis': [6, 5, 7], 'Sofia': [10, 9, 10], 'Gerardo': [7, 8, 9]}

name = "Sofia"
if name in students:
    student_promedio = students["Sofia"]
    total_promedio = sum(student_promedio) / len(student_promedio)
    print(f"El promedio de: {name} es: {total_promedio:.2f} ")
else:
    print("El estudiante no se encuentra en la lista ")
# El promedio de: Sofia es: 9.67 



name = "Gerardo"
if name in students:
    student_promedio = students["Gerardo"]
    total_promedio = sum(student_promedio) / len(student_promedio)
    print(f"El promedio de: {name} es: {total_promedio:.2f} ")
else:
    print("El estudiante no se encuentra en la lista ")
# El promedio de: Gerardo es: 8.00 
