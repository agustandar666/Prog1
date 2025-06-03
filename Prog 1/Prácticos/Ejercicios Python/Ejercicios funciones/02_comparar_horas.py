def mostrar_hora(h, m, s):   # Esta función muestra la hora en formato hh:mm:ss
    if len(h) < 2:
        h = f"0{h}"
    if len(m) < 2:
        m = f"0{m}"
    if len(s) < 2:
        s = f"0{s}"

    return f"{h}:{m}:{s}"


hora = input("Ingresa hora: ")
minuto = input("Ingresa minutos: ")
seg = input("Ingresa segundos: ")

if int(hora) < 24 and int(minuto) < 60 and int(seg) < 60:
    print(mostrar_hora(hora, minuto, seg))
else:
    print("Inválido.")
