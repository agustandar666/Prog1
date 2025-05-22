import datetime

hoy = datetime.date.today()
dia_semana = hoy.strftime('%A')

if dia_semana == "Monday":
    print("Hoy comienza la semana. Animo!")
elif dia_semana == "Friday":
    print("Ya casi termina!")
elif dia_semana == "Saturday" or dia_semana == "Sunday":
    print("Siiii! Fin de semana!")
else:
    print("Vamos que se puede!")
