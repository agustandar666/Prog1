def obtener_entero(mensaje, minimo, maximo):
    while True:
        entero = int(input(f"{mensaje} [{minimo}; {maximo}]\n> "))
        if minimo <= entero <= maximo:
            return entero
        else:
            print(f"Debe ingresar un valor entre {minimo} y {maximo}")

n = obtener_entero("Elija un número dentro del siguiente rango: ", 1, 10)

print(f"Número obtenido: {n}")