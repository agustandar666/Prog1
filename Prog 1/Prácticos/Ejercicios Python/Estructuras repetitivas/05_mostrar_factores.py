n = int(input("Ingrese un número: "))
factor1 = 1

while factor1 != n / 2:

    if n % factor1 == 0:
        factor2 = n / factor1
        print(f"{int(factor2)} x {int(factor1)} = {int(n)}")
        factor1 += 1
        pass
    else:
        factor1 += 1
        pass
