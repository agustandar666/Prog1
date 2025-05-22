def imprimir_dias():
    print("¿Qué día es hoy?\n")
    print("1 - Lunes")
    print("2 - Martes")
    print("3 - Miércoles")
    print("4 - Jueves")
    print("5 - Viernes")
    print("6 - Sábado")
    print("7 - Domingo")


dia = False

imprimir_dias()

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
