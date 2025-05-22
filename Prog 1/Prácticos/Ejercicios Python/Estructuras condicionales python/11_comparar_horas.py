def tiempo(h, m, s):           # Esta función muestra la hora en formato hh:mm:ss
    return f"{h}:{m}:{s}"


comparar = True     # Bandera para el loop

while comparar:

    print("\n")

    print("Hora 1\n")                       # Pide la Hora 1 al usuario
    hora1 = int(input("Ingresar hora: "))
    min1 = int(input("Ingresar minutos: "))
    seg1 = int(input("Ingresar segundos: "))

    print("\n")

    print("Hora 2\n")                       # Pide la hora 2 al usuario
    hora2 = int(input("Ingresar hora: "))
    min2 = int(input("Ingresar minutos: "))
    seg2 = int(input("Ingresar segundos: "))

    print("\n")

    # Posibles salidas almacenadas en variables para no repetir código
    hora2_antesque1 = f"La hora 2 ({tiempo(hora2, min2, seg2)}) es anterior a la hora 1 ({tiempo(hora1, min1, seg1)})"
    hora1_antesque2 = f"La hora 1 ({tiempo(hora1, min1, seg1)}) es anterior a la hora 2 ({tiempo(hora2, min2, seg2)})"

    # Se revisa validez de los datos ingresados por el usuario
    if hora1 < 24 and hora2 < 24 and min1 < 60 and min2 < 60 and seg1 < 60 and seg2 < 60:
        if hora1 > hora2:
            print(hora2_antesque1)
            comparar = False
        elif hora1 == hora2:
            if min1 > min2:
                print(hora2_antesque1)
                comparar = False
            elif min1 == min2:
                if seg1 > seg2:
                    print(hora2_antesque1)
                    comparar = False
                elif seg1 == seg2:
                    print("Has ingresado la misma hora")
                    comparar = False
                else:
                    print(hora1_antesque2)
                    comparar = False
            else:
                print(hora1_antesque2)
                comparar = False
        else:
            print(hora1_antesque2)
            comparar = False
    else:
        print("Valores inválidos, intente de nuevo.")
