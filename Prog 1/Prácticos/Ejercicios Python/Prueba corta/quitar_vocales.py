# Lista con vocales
vocales = ["a", "e", "i", "o", "u"]

# Solicita texto al usuario
palabra = input("Ingrese un texto: ").lower()


def quitar_vocales(texto):
    # Loop for compara cada caracter con el contenido de la lista de vocales
    for caracter in texto:
        # Si el caracter coincide con algún elemento de la lista de vocales, se reemplaza por un espacio vacío ("")
        if caracter in vocales:
            texto = texto.replace(caracter, "")
    return texto


print(quitar_vocales(palabra))
