from tg2_funciones import *

salir = False

while not salir:

    buscar = normalizar(input("Buscar (escriba 'salir' para salir): "))

    if buscar != 'salir':

        puntaje_por_noticia = {}

        terminos = buscar.split()

        listado_noticias = get_news_content(buscar)

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

        top3 = obtener_top3(puntaje_por_noticia)

        print("\nTOP 3 noticias más relevantes:")
        for i, (noticia, puntaje) in enumerate(top3, start=1):
            print(f"{i}. Puntaje: {puntaje:.4f}")
            print(noticia)
            print("-" * 50)

    else:

        print("Programa finalizado")
        salir = True

