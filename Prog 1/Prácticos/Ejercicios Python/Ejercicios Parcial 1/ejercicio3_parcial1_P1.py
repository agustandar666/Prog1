import random
juego = True

print("Voy a pensar en un número entre 1 y el número que tú me digas ¡Intenta adivinarlo!")

tope = int(input("Desde 1 hasta: "))
numero_secreto = random.randint(1, tope)

intentos_restantes = int(input("¿En cuántos intentos crees poder adivinar el número secreto?: "))
print(f"\nMuy bien, tienes {intentos_restantes} intentos para adivinar el número")


while juego:
    print(f"Intentos restantes = {intentos_restantes}")

    if intentos_restantes > 0:

        intento = int(input("Tu intento: "))

        if intento < numero_secreto:
            print(f"\nIncorrecto. {intento} es menor que el número secreto")
            intentos_restantes -= 1
        elif intento > numero_secreto:
            print(f"\nIncorrecto. {intento} es mayor que el número secreto")
            intentos_restantes -= 1
        else:
            print("\n¡Adivinaste el número secreto! ¡¡Ganaste el juego!!")
            juego = False
    else:
        print(f"\nHas agotado tus intentos :(\nEl número secreto era {numero_secreto}")
        juego = False
