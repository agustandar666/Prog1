from tg2_pruebas import normalizar


# Con este algoritmo normalizamos el contenido del archivo de stopwords para que coincidan con nuestra normalización

with open("PalabrasRestringidas.txt", "r", encoding='utf-8') as archivo:
    archivoNormalizado = open("RestringidasNormalizado.txt", "w")

    for linea in archivo:
        linea_normalizada = normalizar(linea)
        archivoNormalizado.writelines(f"{linea_normalizada}\n")

archivoNormalizado.close()