a = "ROJO"
b = "VERDE"
c = "AZUL"
votar = False

print("Elija el candidato por el que va a votar:")
print(f"[A] Candidato {a}")
print(f"[B] Candidato {b}")
print(f"[C] Candidato {c}")

while not votar:

    voto = input("Elegir opción: ").upper()

    if voto == "A":
        print(f"Usted ha votado por el partido {a}")
        votar = True
    elif voto == "B":
        print(f"Usted ha votado por el partido {b}")
        votar = True
    elif voto == "C":
        print(f"Usted ha votado por el partido {c}")
        votar = True
    else:
        print("Opción inválida")
    