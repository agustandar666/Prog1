# Importamos módulo unicodedata
from unicodedata import *


# Función que muestra el menú en la consola
def menu():
    print("[1] Descifrar mensaje")
    print("[2] Cifrar mensaje")
    print("[0] Salir")


# Función que normaliza el texto ingresado
def normalizar(text):

    # La función normalize() del módulo unicodedata separa símbolos de letras permitiendo que el intérprete
    # lea cada símbolo por separado (ej: á = a + ´ ).
    # Además, se usa el método .lower() para pasar todo a minúsculas antes de normalizarlo.
    text_normalizado = normalize('NFKD', text.lower())

    # Se evalúa cada caracter verificando que se corresponda con la categoría 'Ll' que corresponde a letras minúsculas
    for caracter in text_normalizado:
        if category(caracter) != 'Ll':
            text_normalizado = text_normalizado.replace(caracter, "")

    # Devuelve una cadena compuesta únicamente de letras minúsculas sin acentuaciones ni símbolos de ningún tipo
    return text_normalizado


# La función permutar() toma pares de caracteres consecutivos, invierte su orden y los va sumando en una cadena nueva
def permutar(text):

    # Se define la variable que almacenará la cadena que se formará de la suma de pares permutados
    text_permutado = ""

    # "Mientras haya contenido en la cadena"
    while len(text) > 0:

        # Se emplea el método de slicing.
        # El primer par de corchetes toma los primeros dos caracteres de la cadena ingresada
        # El segundo par invierte su orden
        par_permutado = text[:2][::-1]

        # Se agrega el par permutado en la variable final
        text_permutado += par_permutado

        # Se restan los dos primeros caracteres de la cadena original para seguir trabajando con los restantes
        text = text[2:]

    # Cuando no quedan caracteres en la cadena original, devuelvela cadena con los pares permutados
    return text_permutado


# Esta función desplaza 3 lugares (en el alfabeto) los caracteres de una cadena
def desplazar(text, n):

    # Se define la variable final
    palabra_desplazada = ""

    # Se busca el índice de cada letra de la cadena de entrada dentro de la lista 'alfabeto' y se le suma 3 para tomar
    # la letra que se encuentra tres lugares después
    for letra in text:
        num = alfabeto.index(letra) + n

        # Para evitar errores, se verifica si el índice 'num' excede el largo de la lista 'alfabeto'.
        # Si esto sucede, se le resta al índice (luego de haberle sumado 3) el largo de la lista, resultando el índice
        # correcto.
        if num > len(alfabeto) - 1:
            palabra_desplazada += alfabeto[num - len(alfabeto)]
        else:
            palabra_desplazada += alfabeto[num]

    return palabra_desplazada


alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i",
            "j", "k", "l", "m", "n", "o", "p", "q",
            "r", "s", "t", "u", "v", "w", "x", "y", "z"]
