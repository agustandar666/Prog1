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

            dicc_tf_x_idf = {}

            for termino in terminos:
                if termino in dicc_tf:
                    dicc_tf_x_idf[termino] = dicc_tf[termino] * dicc_idf[termino]
                else:
                    dicc_tf_x_idf[termino] = 0

            for elemento in dicc_tf_x_idf:

                suma_tfidf += dicc_tf_x_idf[elemento]

            puntaje_por_noticia[noticia] = suma_tfidf

        print(puntaje_por_noticia)

    else:

        print("Programa finalizado")
        salir = True

