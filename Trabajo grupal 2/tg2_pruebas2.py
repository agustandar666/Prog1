from tg2_pruebas import *
'''
def borrar_palabras_restringidas(busqueda):
    with open("RestringidasNormalizado.txt", "r", encoding="utf-8") as archivo:
        palabras_restringidas = [linea.strip() for linea in archivo]

        palabras_noticia = busqueda.split()
        busqueda_filtrada = [palabra for palabra in palabras_noticia if palabra not in palabras_restringidas]


        return busqueda_filtrada



print(borrar_palabras_restringidas("como usar una api de programacion"))
'''

from tg2_funciones import *

salir = False

while not salir:

    buscar = normalizar(input("Buscar (escriba 'salir' para salir): "))

    puntaje_por_noticia = {}

    if buscar != 'salir':

        terminos = buscar.split()

        listado_noticias = ['el pasado martes del presidente anuncio un anuncio de que ya no iba a ser más presidente',
                            'ayer se celebró el día del presidente en conmemoración al presidente porque es el presidente',
                            'este es un anuncio genérico con el que anuncio un anuncio',
                            'me compre una bicicleta del carajo esta muy buena del jaja']            # get_news_content(buscar)

        for noticia in listado_noticias:

            suma_tfidf = 0

            noticia = normalizar(noticia)

            palabras_noticia = noticia.split()

            dicc_tf = calcular_tf(palabras_noticia, terminos)

            dicc_idf = calcular_idf(listado_noticias, terminos)

            top3_noticias = top3(dicc_tf, dicc_idf, noticia)



    else:

        print("Programa finalizado")
        salir = True

