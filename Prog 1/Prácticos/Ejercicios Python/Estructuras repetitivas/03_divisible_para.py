num = int(input("Ingrese el numerador: "))
den = int(input("Ingrese el denominador: "))
result = num

for n in range(num, 0, -den):
    result -= den           # result = result - den

if result == 0:
    print(f"{num} es divisible entre {den}")
else:
    print(f"{num} no es divisible entre {den}")
