from datetime import datetime

now = datetime.now()

print(now.year) # 2025
print(now.month) # 8
print(now.day) # 17
print(now.hour) # 20
print(now.minute) # 54


from datetime import date

current_date = date.today()

print(current_date.year) # 2025
print(current_date.month) # 8
print(current_date.day) # 17

timestamp = now.timestamp()

print(timestamp)
year_2026 = datetime(2026,1,1)

def print_date(date):
    print(date.year) # 2026
    print(date.month) # 1
    print(date.day) # 1
    print(date.hour) # 0
    print(date.minute) # 0
    print(date.timestamp()) # 1767247200.0

print_date(year_2026)

from datetime import time

current_time = time()

current_date = date.today()
print(current_date.year) # 2025
print(current_date.month) # 8
print(current_date.day) # 17


current_date = date(2025, 8,16)

print(current_date.year) # 2025
print(current_date.month) # 8
print(current_date.day) # 16

current_date = date(current_date.year + 1, current_date.month, current_date.day)

print(current_date.year) # 2026

diff = year_2026 - now
print(diff) # 136 days, 2:56:05.171552

diff = year_2026.date() - current_date
print(diff) # -227 days, 0:00:00

print("-"*30)

# EJERCICIOS
from datetime import date, time, datetime, timedelta

# 1. Crea una variable con la fecha y hora actual
# 2. Imprime solo el año, mes y día de la fecha actual.
dia_hoy = date.today()
print(dia_hoy)  # 2025-08-17
# 1. Crea una variable con la fecha y hora actual.
now = datetime.now()
print(now) # 2025-08-17

# 2. Imprime solo el año, mes y dia de la fecha actual.
print(now.year) # 2025
print(now.month) # 8
print(now.day) # 17

# 3. Crea una fecha específica: 25 de diciembre de 2025 y 
#    muéstrala.
dia = date(2023,10, 16)
print(dia) # 2023-10-16
# 3. Crea una fecha especÃ­fica: 25 de diciembre de 2025 y muÃ©strala.
christmas = datetime(2025, 12, 25)
print(christmas) # 2025-12-25 00:00:00

#  4. Muestra solo la hora, los minutos y los segundos de un 
#     objeto time.
ahora = datetime.now()
print(ahora) # 2025-08-17 21:08:57.844031
print("Hora actual:", ahora.strftime("%H:%M:%S"))
 # Hora actual: 21:08:57
# 4. Muestra solo la hora, los minutos y los segundos de un objeto time.
hour = time(14, 30, 15)
print(hour.hour) # 14
print(hour.minute) # 30
print(hour.second) # 15

# 5. Calcula cuántos días faltan para el 1 de enero del año siguiente.
# Creamos una fecha que representa el 1 de enero del año siguiente al actual
proximo_enero = date(dia_hoy.year + 1, 1, 1)
# Restamos la fecha de hoy a la fecha del próximo 1 de enero para obtener la diferencia en días
faltan_dias = (proximo_enero - dia_hoy).days
# Mostramos cuántos días faltan para el 1 de enero del próximo año
print(faltan_dias) # 137
# 5. Calcula cuÃ¡ntos dÃ­as faltan para el 1 de enero del aÃ±o siguiente.
today = date.today()
year_init = date(today.year + 1, 1, 1)
diff = year_init - today
print(diff.days) # 137

# 6. Crea una funcion que reciba una fecha y devuelva su timestamp.
def get_timestamp(date):
    return date.timestamp()
print(get_timestamp(datetime.now())) # 1755487572.53452

# 7. Suma 30 dias a la fecha actual usando timedelta.
future_date = datetime.now() + timedelta(days=30)
print(future_date) # 2025-09-16 21:26:12.534520

# 8. Crea una fecha y añade 1 mes (consejo: hazlo sumando 30 dÃ­as como simplificaciÃ³n).
init_date = datetime(2024, 3, 15)
new_date = init_date + timedelta(days=30)
print(new_date) # 2024-04-14 00:00:00

# 9. Compara dos fechas y muestra cuÃ¡l es anterior.
dato1 = datetime(2023, 6, 1)
dato2 = datetime(2024, 1, 1)
if dato1 < dato2:
    print("dato1 es anterior") # dato1 es anterior
else:
    print("dato2 es anterior") 

# 10. Crea una lista con varias fechas y ordenalas cronologicamente.
datos = [
    datetime(2022, 5, 1),
    datetime(2020, 1, 15),
    datetime(2023, 12, 31),
]
sorted_datos = sorted(datos)
for f in sorted_datos:
    print(f)
 # 2020-01-15 00:00:00
 # 2022-05-01 00:00:00
 # 2023-12-31 00:00:00