n = int(input("Ingrese un número: "))

while n != 1:
    if n % 2 == 0:
        n /= 2        # n = n / 2
        print(int(n))
        pass
    else:
        n = n * 3 + 1
        print(int(n))
        pass
