def pertenece_al_intervalo(n, lim_sup, lim_inf):
    if lim_inf <= n <= lim_sup:
        return True
    else:
        return False


N = float(input("Ingrese un número: "))
linf = float(input("Ingrese un límite inferior: "))
lsup = float(input("Ingrese un límite superior: "))

if pertenece_al_intervalo(N, lsup, linf):
    print("el número pertenece al intervalo")
else:
    print("el número no pertenece al intervalo")
