# Esta función toma los parámetros de saldos, descuentos y adiciones e imprime un informe completo
def sueldo_y_descuentos(sa, an, dm, dr, dg, sf):
    return (f"\nSueldo acordado: ${sa}\n"
            f"Adición por antigüedad: +${an}\n"
            f"\n"
            f"Descuentos:\n"
            f"Seguro médico: -${dm}\n"
            f"Seguro de retiro: -${dr}\n"
            f"Impuesto a la ganancia: -${dg}\n"
            f"Total descontado: ${round(dm + dr + dg, 2)}\n"
            f"\n"
            f"Sueldo a cobrar: ${sf}")


# Entradas del usuario
sueldo_acordado = int(input("Digite su sueldo acordado: "))
antig = int(input("Digite sus años de antigüedad: ")) / 100     # Se divide entre 100 para facilitar operaciones

# Se define el valor de los descuentos
desc_medico = round(sueldo_acordado * 0.06, 2)
desc_retiro = round(sueldo_acordado * 0.11, 2)

# Se define la adición por antigüedad evaluando la cantidad de años
if antig < 0.2:
    suma_antig = round(sueldo_acordado * antig, 2)
else:
    suma_antig = round(sueldo_acordado * 0.2, 2)

# Se define el descuento por ganancia evaluando el sueldo acordado
if sueldo_acordado > 120000:
    desc_ganancia = round(sueldo_acordado * 0.25, 2)

elif 120000 > sueldo_acordado > 70000:
    desc_ganancia = round(sueldo_acordado * 0.2, 2)
else:
    desc_ganancia = 0

# Se calcula el sueldo después de los impuestos y la adición por antigüedad
sueldo_final = round(sueldo_acordado + suma_antig - desc_retiro - desc_medico - desc_ganancia, 2)

# Se usa la función 'sueldo_y_descuentos' creada al principio del algoritmo
# ingresándole todos los parámetros necesarios y se almacena en la variable 'informe'
informe = sueldo_y_descuentos(sueldo_acordado, suma_antig, desc_medico, desc_retiro, desc_ganancia, sueldo_final)

# Se imprime el informe con todos los datos
print(informe)
