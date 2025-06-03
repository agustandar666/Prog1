def permutar_caracteres(text):
    text_permutado = ""
    while len(text) > 0:

        par_permutado = text[:2][::-1]
        text_permutado += par_permutado
        text = text[2:]

    return text_permutado

print(permutar_caracteres("jpigmxmgesmirwwtmiyihzwviwiixiqwrnelidesgwrkimyshihgwjmevivqpriewiniwvgxitsveiexwhiwijesm"))