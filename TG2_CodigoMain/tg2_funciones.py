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

    terminos_totales = len(palabras_noticia) # Se almacena la cantidad de palabras en la noticia
    veces_palabras_en_noticia = {} # Diccionario para contar las apariciones de cada palabra en la noticia
    tf_palabra = {} # Diccionario para almacenar el puntaje tf de cada término en la noticia

# Para cada palabra de la noticia se determina si esta se encuentra en la lista de palabras de la búsqueda
# Si la palabra ya está contenida en la lista, se evalúa si está contenida en el diccionario veces_palabras_en_noticia
# Si está contenida se le suma 1 a su valor, si no, se le asigna el valor 1
    for palabra in palabras_noticia:
        if palabra in palabras_busqueda:
            if palabra in veces_palabras_en_noticia:
                veces_palabras_en_noticia[palabra] += 1
            else:
                veces_palabras_en_noticia[palabra] = 1
# Se realiza el cálculo de tf para cada palabra
    for item in veces_palabras_en_noticia:

            tf_palabra[item] = veces_palabras_en_noticia[item] / terminos_totales

    return tf_palabra

# Función para calcular frecuencia inversa
def calcular_idf(lista_noticias, palabras_busqueda):

# Diccionario vacío para almacenar puntajes idf de cada término
    idf_palabra = {}
    total_noticias = len(lista_noticias) # Se almacena el número de noticias para realizar la operación de idf

# Loop for para evaluar cada término de la búsqueda
    for termino in palabras_busqueda:
        noticias_con_termino = 0

        # Loop for para contar cuántas noticias contienen el término evaluado
        for noticia in lista_noticias:
            noticia = normalizar(noticia) # Normaliza cada noticia para analizarla

            # Si el término está en la noticia, se suma 1 a la variable que cuenta las noticias que contienen el término
            if termino in noticia:
                noticias_con_termino += 1

        # Si al menos una noticia contiene el término, se realiza la operación para calcular el puntaje idf
        if noticias_con_termino > 0:
            idf = math.log(total_noticias / noticias_con_termino, 10)

        # De lo contrario, para evitar una división entre 0 (ya que la cantidad de noticias con el término es el
        # denominador de la división) se le asigna valor 0 al puntaje idf.
        else:
            idf = 0

        # Luego de calcular el valor, dentro del diccionario se almacena el término como clave y su puntaje como valor
        idf_palabra[termino] = idf

    return idf_palabra

# Función que devuelve las tres noticias de mayor puntaje tf-idf
def obtener_top3(diccionario_puntajes):

    return heapq.nlargest(3, diccionario_puntajes.items(), key=lambda x: x[1])

# Función bonus que filtra las palabras de la búsqueda
def bonus(busqueda):

    with open("RestringidasNormalizado.txt", "r", encoding="utf-8") as palabras_no_van:
        palabras_noticia = busqueda.split()
        busqueda_filtrada = []

        for palabra in palabras_noticia:
            if palabra not in palabras_no_van.read():
                busqueda_filtrada.append(palabra)

        return busqueda_filtrada

