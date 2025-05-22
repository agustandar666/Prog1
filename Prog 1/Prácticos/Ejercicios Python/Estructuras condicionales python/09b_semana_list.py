semana = ['lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado', 'domingo']

hoy = input("Ingrese el día de la semana: ").lower()

for i in semana:
    if hoy == i:
        dia_semana = i.index() + 1
        break
    else:
        print("Inválido")

dia = False

while not dia:
    hoy = int(input("Ingrese número del día de la semana: "))

    if hoy == 1:
        print("Hoy comienza la semana. Animo!")
        dia = True
    elif hoy == 5:
        print("Ya casi termina!")
        dia = True
    elif hoy == 6 or hoy == 7:
        print("Siiii! Fin de semana!")
        dia = True
    elif 1 <= hoy <= 5:
        print("Vamos que se puede!")
        dia = True
    else:
        print("Inválido")
