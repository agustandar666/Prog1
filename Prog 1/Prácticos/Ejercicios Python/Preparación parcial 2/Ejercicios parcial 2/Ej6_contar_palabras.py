def contar_palabras(text):
    text = text.strip()
    if len(text) > 0:
        cantidad_palabras = 1
        for caracter in text:
            if caracter == " ":
                cantidad_palabras += 1
        return f"El texto contiene {cantidad_palabras} palabras"
    else:
        return "El texto no contiene palabras"


texto = ("Implementar en Python una función que recibe un párrafo de un libro (como cadena de caracteres) y"
         "devuelve la cantidad de palabras del párrafo. No se puede utilizar el método split() de Python.")

print(contar_palabras(texto))