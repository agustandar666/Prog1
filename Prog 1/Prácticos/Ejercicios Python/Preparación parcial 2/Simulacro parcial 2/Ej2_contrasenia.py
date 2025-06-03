from random import randint


def generar_contrasenia(n):
    contrasenia = ""
    while n > 0:
        contrasenia += str(randint(0, 9))
        n -= 1
    return contrasenia


digitos = int(input("Ingrese número de dígitos para su contraseña\n> "))

print(generar_contrasenia(digitos))
