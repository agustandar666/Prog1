n = int(input("Ingrese un número: "))
fact = 1

for num in range(n, 1, -1):
    fact *= num
    print(fact)
