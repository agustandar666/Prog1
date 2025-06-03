def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return "fizzbuzz"
    elif n % 3 == 0:
        return "fizz"
    elif n % 5 == 0:
        return "buzz"
    else:
        f"{n}"


num = int(input("Ingresá un numero del 1 al 100: "))
mostrar_num = False

while not mostrar_num:
    if 1 <= num <= 100:
        print(fizzbuzz(num))
        mostrar_num = True
    else:
        input("Inválido. ENTER para reintentar")
