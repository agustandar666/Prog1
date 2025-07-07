import requests
import math
from unicodedata import *
import heapq


def get_news_content(busqueda):
    # Parámetros de consulta
    params = {'q': busqueda,'apiKey': "b3d238f8fad0471f865cfe444d89fe8a", "language":"e" "s"}
    response = requests.get("https://newsapi.org/v2/everything", params=params)
    # Obtiene los artículos del json
    articles = response.json()['articles']
    lista_noticias = []
    # Toma la descripción de cada noticia
    for article in articles:
        lista_noticias.append(article['content'])
    return lista_noticias


# Función que normaliza el texto ingresado
def normalizar(text):

    # La función normalize() del módulo unicodedata separa símbolos de letras permitiendo que el intérprete
    # lea cada símbolo por separado (ej: á = a + ´ ).
    # Además, se usa el método .lower() para pasar todo a minúsculas antes de normalizarlo.

    text_normalizado = normalize('NFKD', text.lower())

    # Se evalúa cada caracter verificando que se corresponda con la categoría 'Ll' que corresponde a letras minúsculas
    for caracter in text_normalizado:
        if category(caracter) != 'Ll' and caracter != " " and not caracter.isnumeric():
            text_normalizado = text_normalizado.replace(caracter, "")

    # Devuelve una cadena compuesta únicamente de letras minúsculas sin acentuaciones ni símbolos de ningún tipo
    return text_normalizado


def borrar_palabras_restringidas(busqueda):
    with open("RestringidasNormalizado.txt", "r", encoding="utf-8") as palabras_no_van:
        palabras_noticia = busqueda.split()
        busqueda_filtrada = []

        for palabra in palabras_noticia:
            if palabra not in palabras_no_van.read():
                busqueda_filtrada.append(palabra)

        return busqueda_filtrada


def calcular_tf(noticia, busqueda):
    terminos_totales = len(noticia)
    palabras_busqueda = busqueda.split()
    veces_palabras_en_noticia = {}
    tf_palabra = {}

    for palabra in noticia:
        if palabra in palabras_busqueda:
            if palabra in veces_palabras_en_noticia:
                veces_palabras_en_noticia[palabra] += 1
            else:
                veces_palabras_en_noticia[palabra] = 1

    for item in veces_palabras_en_noticia:

            tf_palabra[item] = veces_palabras_en_noticia[item] / terminos_totales

    return tf_palabra


def calcular_idf(lista_noticias, palabras_busqueda):
    idf_palabra = {}
    total_noticias = len(lista_noticias)
    noticias_con_termino = 0

    for noticia in lista_noticias:
        for termino in palabras_busqueda:
            if termino in noticia:
                noticias_con_termino += 1

            idf = math.log(total_noticias / noticias_con_termino, 10)

            idf_palabra[termino] = idf

    return idf_palabra


def top3(tf, idf, noticia):

    noticias_puntaje = {}


    for elemento in tf:
        tf_x_idf = tf[elemento] * idf[elemento]

        noticias_puntaje[noticia] = tf_x_idf

    top_3 = heapq.nlargest(3, noticias_puntaje.items(), key=lambda x: x[1])

    return top_3






####################################################################################################

api = ("Una API (del inglés, application programming interface, en español, interfaz de programación de aplicaciones)[1]​ es \n"
       "una pieza de código que permite a dos aplicaciones comunicarse entre sí para compartir información y funcionalidades. Se \n"
       "usan generalmente en bibliotecas de programación")

texto_normalizado = normalizar(api)

lista_noticia = texto_normalizado.split()

busqueda = "como usar una api de programacion"

busqueda_restringida = borrar_palabras_restringidas(busqueda)

# print(calcular_tf(lista_noticia, busqueda_restringida))

