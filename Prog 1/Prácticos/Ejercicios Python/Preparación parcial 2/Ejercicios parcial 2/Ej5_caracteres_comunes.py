# para saber los caracteres comunes deberíamos evaluar cada caracter de uno de los strings,
# verificando si se encuentran contenidos en el otro, si están, se suman en un string nuevo que se inicia vacío.
# usar loop for para comparar caracteres


def caracteres_comunes(palabra1, palabra2):
    comunes = ""
    palabra1 = palabra1.lower()
    palabra2 = palabra2.lower()
    for caracter in palabra1:
        if caracter in palabra2 and caracter not in comunes:
            comunes += caracter
    return comunes


print(caracteres_comunes("programar", "picar codigo"))
