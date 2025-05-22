meses31 = [1, 3, 5, 7, 8, 10, 12]
meses30 = [4, 6, 9, 11]

fecha = False


def mostrar_fecha(dd, mm, aaaa):
    print(f"{dd}/{mm}/{aaaa}, fecha válida")


def bisiesto(aaaa):
    if (aaaa % 4 == 0 and aaaa % 100 != 0) or aaaa % 400 == 0:
        return True
    else:
        return False


while not fecha:
    dia = int(input("Ingrese número de día: "))
    mes = int(input("Ingrese número de mes: "))
    anio = int(input("Ingrese año: "))

    if mes in meses30 and dia <= 30:
        mostrar_fecha(dia, mes, anio)
        fecha = True
    elif mes in meses31 and dia <= 31:
        mostrar_fecha(dia, mes, anio)
        fecha = True
    elif mes == 2:
        if bisiesto(anio) and dia <= 29:
            mostrar_fecha(dia, mes, anio)
            fecha = True
        elif not bisiesto(anio) and dia <= 28:
            mostrar_fecha(dia, mes, anio)
            fecha = True
        else:
            print("Inválido")
