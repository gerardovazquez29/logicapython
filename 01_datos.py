from datetime import datetime

now = datetime.now()

print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)

from datetime import date

current_date = date.today()

print(current_date.year)
print(current_date.month)
print(current_date.day)

timestamp = now.timestamp()

print(timestamp)
year_2026 = datetime(2026,1,1)

def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.timestamp())

print_date(year_2026)

from datetime import time

current_time = time()

current_date = date.today()
print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(2025, 8,16)

print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(current_date.year + 1, current_date.month, current_date.day)

print(current_date.year)

diff = year_2026 - now
print(diff)
diff = year_2026.date() - current_date
print(diff)

print("-"*30)

# 1. Crea una variable con la fecha y hora actual
from datetime import date
dia_hoy = date.today()
# 2. Imprime solo el año, mes y día de la fecha actual. 
print(dia_hoy)

# 3. Crea una fecha específica: 25 de diciembre de 2025 y 
#    muéstrala.
dia = date(2023,10, 16)
print(dia)

#  4. Muestra solo la hora, los minutos y los segundos de un 
#     objeto time.

from datetime import datetime
ahora = datetime.now()
print(ahora)
print("Hora actual:", ahora.strftime("%H:%M:%S"))

# 5. Calcula cuántos días faltan para el 1 de enero del año siguiente.
# Creamos una fecha que representa el 1 de enero del año siguiente al actual
proximo_enero = date(dia_hoy.year + 1, 1, 1)
# Restamos la fecha de hoy a la fecha del próximo 1 de enero para obtener la diferencia en días
faltan_dias = (proximo_enero - dia_hoy).days
# Mostramos cuántos días faltan para el 1 de enero del próximo año
print(faltan_dias)
from datetime import date, time, datetime, timedelta

# 1. Crea una variable con la fecha y hora actual.

now = datetime.now()
print(now)

# 2. Imprime solo el año, mes y dia de la fecha actual.

print(now.year)
print(now.month)
print(now.day)

# 3. Crea una fecha especÃ­fica: 25 de diciembre de 2025 y muÃ©strala.

christmas = datetime(2025, 12, 25)
print(christmas)

# 4. Muestra solo la hora, los minutos y los segundos de un objeto time.

hour = time(14, 30, 15)
print(hour.hour)
print(hour.minute)
print(hour.second)

# 5. Calcula cuÃ¡ntos dÃ­as faltan para el 1 de enero del aÃ±o siguiente.

today = date.today()
year_init = date(today.year + 1, 1, 1)
diff = year_init - today
print(diff.days)

# 6. Crea una funcion que reciba una fecha y devuelva su timestamp.


def get_timestamp(date):
    return date.timestamp()


print(get_timestamp(datetime.now()))

# 7. Suma 30 dias a la fecha actual usando timedelta.

future_date = datetime.now() + timedelta(days=30)
print(future_date)

# 8. Crea una fecha y añade 1 mes (consejo: hazlo sumando 30 dÃ­as como simplificaciÃ³n).

init_date = datetime(2024, 3, 15)
new_date = init_date + timedelta(days=30)
print(new_date)

# 9. Compara dos fechas y muestra cuÃ¡l es anterior.

dato1 = datetime(2023, 6, 1)
dato2 = datetime(2024, 1, 1)

if dato1 < dato2:
    print("dato1 es anterior")
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
