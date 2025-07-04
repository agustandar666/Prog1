from unicodedata import *
import math

import requests
api_key = "b3d238f8fad0471f865cfe444d89fe8a"



'''
Esta función utiliza el servicio newsapi para obtener una lista de noticias.
La función obtiene solo las noticias para Uruguay y las devuelve en una lista
Cada noticia contiene los primeros 200 caracters de la noticia completa.
'''

def get_news_content():
    # Parámetros de consulta
    params = {'q': "uruguay",'apiKey': "b3d238f8fad0471f865cfe444d89fe8a", "language":"e" "s"}
    response = requests.get("https://newsapi.org/v2/everything", params=params)
    # Obtiene los artículos del json
    articles = response.json()['articles']
    lista_noticias = []
    # Toma la descripción de cada noticia
    for article in articles:
        lista_noticias.append(article['content'])
    return lista_noticias

news = get_news_content()
#print(news[0])
print(news[1])
list_palabras = news[1].split()

print(list_palabras)
#print(news[2])
#print(news[3]