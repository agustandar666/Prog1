vocales = ["a", "e", "i", "o", "u", "á", "é", "í", "ó", "ú"]


def en_equilibrio(c):
    vocales_en_c = ""
    for car in c.lower():
        if car in vocales:
            vocales_en_c += car

    if len(vocales_en_c) % 2 != 0:
        v = int((len(vocales_en_c)) / 2)
        pos_v = vocales_en_c[v]
        return pos_v
    else:
        return -1

print(en_equilibrio("Programación"))
