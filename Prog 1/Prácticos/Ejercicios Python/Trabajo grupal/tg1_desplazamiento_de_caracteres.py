alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i",
            "j", "k", "l", "m", "n", "ñ", "o", "p", "q",
            "r", "s", "t", "u", "v", "w", "x", "y", "z"]

car = "a"
lista_car = []
palabra_secreta = ""

for caracter in car:
    lista_car.append(caracter)

for letra in lista_car:
    num = alfabeto.index(letra)
    palabra_secreta += (alfabeto[num - 1])

print(palabra_secreta)

def desplazar_caracteres(text):
        lista_car = []
        palabra_desplazada = ""

        for caracter in text:
            lista_car.append(caracter)

        for letra in lista_car:
            num = alfabeto.index(letra)
            palabra_desplazada += alfabeto[num - 1]

        return palabra_desplazada
