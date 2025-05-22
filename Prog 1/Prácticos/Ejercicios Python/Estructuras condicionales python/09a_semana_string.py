dia = False

while not dia:
    hoy = input("Ingrese el día de la semana: ").lower()

    if hoy == "lunes":
        print("Hoy comienza la semana. Animo!")
        dia = True
    elif hoy == "viernes":
        print("Ya casi termina!")
        dia = True
    elif hoy == "sabado" or hoy == "domingo":
        print("Siiii! Fin de semana!")
        dia = True
    elif hoy == "martes" or hoy == "miercoles" or hoy == "jueves":
        print("Vamos que se puede!")
        dia = True
    else:
        print("Inválido")
