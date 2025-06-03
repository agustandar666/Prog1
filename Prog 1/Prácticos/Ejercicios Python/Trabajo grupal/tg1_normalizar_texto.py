from unicodedata import *

texto = "msejiwihwxeievstixgvwiniweirpqvivemjwghihsymikrwgsedilenrwqixiiw ivwzhiyimtwwrimsegmxmgipj"[::-1]

texto_normalizado = normalize('NFKD', texto)

for letra in texto_normalizado:
    if category(letra) != 'Ll':
        texto_normalizado = texto_normalizado.replace(letra, "")

print(texto_normalizado)


def normalizar(text):
    text_normalizado = normalize('NFKD', text)

    for caracter in text_normalizado:
        if category(caracter) != 'Ll':
            text_normalizado = text_normalizado.replace(caracter, "")
