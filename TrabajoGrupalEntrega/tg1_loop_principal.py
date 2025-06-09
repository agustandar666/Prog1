from tg1_funciones import *

# Bandera para el loop principal
salir = False

# Loop principal
while not salir:

    # Muestra el menú
    menu()

    try:

        opcion = int(input("Elija opción y presione enter: "))

        if opcion == 1:

            # DESCIFRAR
            # Normaliza el texto, luego invierte el orden de los caracteres, después permuta los pares de caracteres
            # y, finalmente, desplaza los caracteres en el alfabeto n veces.

            texto = input("Ingrese el mensaje a descifrar:\n> ")

            texto_normalizado = normalizar(texto)

            texto_invertido = texto_normalizado[::-1]

            texto_permutado = permutar(texto_invertido)

            texto_revelado = desplazar(texto_permutado, 3)

            input(f"Se ha descifrado el mensaje:\n> {texto_revelado}\nENTER para volver al menú.")

        elif opcion == 2:

            # CIFRAR
            # Cifra un mensaje dado ejecutando el proceso inverso al de descifrado.

            texto_i = input("Ingrese el mensaje a cifrar:\n> ")

            texto_normalizado_i = normalizar(texto_i)

            texto_desplazado_i = desplazar(texto_normalizado_i, -3)

            texto_permutado_i = permutar(texto_desplazado_i)

            texto_revelado_i = texto_permutado_i[::-1]

            input(f"Se ha descifrado el mensaje:\n> {texto_revelado_i}\nENTER para volver al menú.")

        elif opcion == 0:
            salir = True

        else:
            print("Elija una opción válida")

    except ValueError:
        print("Elija una opción válida")
