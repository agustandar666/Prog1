def adicion_por_antiguedad(suel_acor, antig):
    if antig < 20:
        sueldo_con_antig = suel_acor + (suel_acor * 0.01 * antig)
    else:
        sueldo_con_antig = suel_acor + (suel_acor * 0.2)
    return sueldo_con_antig


def descuentos(monto):
    seg_ret = monto * 0.11
    seg_med = monto * 0.06

    if monto > 120000:
        descuento_ganancia = monto * 0.25
    elif 70000 < monto <= 120000:
        descuento_ganancia = monto * 0.2
    else:
        descuento_ganancia = 0

    sueldo_con_descuentos = monto - seg_ret - seg_med - descuento_ganancia
    return sueldo_con_descuentos


sueldo = float(input("Ingrese su sueldo acordado: "))
antiguedad = int(input("Ingrese sus años de antigüedad: "))

sueldo_con_antiguedad = adicion_por_antiguedad(sueldo, antiguedad)
sueldo_final = descuentos(sueldo_con_antiguedad)
print(f"Su sueldo a cobrar es: {sueldo_final}")
