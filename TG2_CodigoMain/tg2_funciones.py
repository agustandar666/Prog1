# Se importan todos los módulos que se usan en las funciones

import requests             # Se usa en la búsqueda de noticias
import math                 # Se usa la función log() para calcular idf
import heapq                # Se usa para extraer las tres noticias de mayor puntaje tf-idf
from unicodedata import *   # Se usa para normalizar los textos


# Función que normaliza el texto ingresado
def normalizar(text):

    # La función normalize() del módulo unicodedata separa símbolos de letras permitiendo que el intérprete
    # lea cada símbolo por separado (ej: á = a + ´ ).
    # Además, se usa el método .lower() para pasar todo a minúsculas antes de normalizarlo.

    text_normalizado = normalize('NFKD', text.lower())

    # Se evalúa cada caracter verificando que se corresponda con la categoría 'Ll' (que corresponde a letras minúsculas)
    # y que sea distinto de un caracter de espacio, conservando los espacios para luego poder leer cada palabra por
    # separado
    for caracter in text_normalizado:
        if category(caracter) != 'Ll' and caracter != " ":
            text_normalizado = text_normalizado.replace(caracter, "")

    # Devuelve una cadena compuesta únicamente de letras minúsculas sin acentuaciones ni símbolos de ningún tipo
    return text_normalizado


# Función que obtiene las noticias
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


# Función que calcula el tf de cada noticia
def calcular_tf(palabras_noticia, palabras_busqueda):
    terminos_totales = len(palabras_noticia)
    veces_palabras_en_noticia = {}
    tf_palabra = {}

    for palabra in palabras_noticia:
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


    for termino in palabras_busqueda:
        noticias_con_termino = 0
        for noticia in lista_noticias:
            noticia = normalizar(noticia)
            if termino in noticia:
                noticias_con_termino += 1
        if noticias_con_termino > 0:
            idf = math.log(total_noticias / noticias_con_termino, 10)
        else:
            idf = 0
        idf_palabra[termino] = idf

    return idf_palabra


def obtener_top3(diccionario_puntajes):

    return heapq.nlargest(3, diccionario_puntajes.items(), key=lambda x: x[1])

