def primera_a_mayus(palabra):
    primer_letra = palabra[0].upper()   # Extrae primer caracter del string y lo convierte a mayúscula
    alabra = palabra.lstrip(primer_letra.lower())   # Borra el primer caracter del string original
    return f"{primer_letra}{alabra}"  # Combina la primera letra en mayúscula con el resto de la palabra


print(primera_a_mayus("picaporte"))
