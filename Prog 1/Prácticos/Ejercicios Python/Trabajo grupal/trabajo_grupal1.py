from tg1_funciones_descifrar import *

# Bandera para el loop principal
salir = False

while not salir:
    menu()
    try:

        opcion = int(input("Elija opción y presione enter: "))

        if opcion == 1:
            texto = input("Ingrese el mensaje a descifrar:\n> ")
            texto_normalizado = normalizar(texto)
            texto_invertido = texto_normalizado[::-1]
            texto_permutado = permutar(texto_normalizado)
            texto_revelado = desplazar(texto_permutado, -3)
            input(f"Se ha descifrado el mensaje:\n> {texto_revelado}\nENTER para volver al menú.")

        elif opcion == 2:
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
