n = int(input("Ingrese un número: "))
fact = n

while n > 1:
    fact *= n-1
    n -= 1
    print(fact)
    pass
