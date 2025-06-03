def mostrar_hora(hh, mm, ss):
    if hh > 12:
        hh -= 12
        mediodia = "PM"

    else:
        mediodia = "AM"
    return f"Hora: {hh} {mediodia} Minutos: {mm} Segundos: {ss}"


hora_mostrada = False

while not hora_mostrada:
    hora_usuario = input("Ingrese la hora en formato hh:mm:ss\n> ")

    hora = int(hora_usuario[0:2])
    mins = int(hora_usuario[3:5])
    segs = int(hora_usuario[6:])

    if hora < 24 and mins < 60 and segs < 60:
        print(mostrar_hora(hora, mins, segs))
        hora_mostrada = True
    else:
        print("Ingrese valores válidos")
