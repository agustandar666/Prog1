altura = float(input("Ingrese altura: "))
peso = float(input("Ingrese peso: "))

imc = peso / altura**2

if imc < 18.5:
    print(f"Su imc es {imc}, se encuentra en el rango: Bajo peso")

elif imc >= 18.5 < 25:
    print(f"Su imc es {imc}, se encuentra en el rango: Peso normal")

elif imc >= 25 < 30:
    print(f"Su imc es {imc}, se encuentra en el rango: Sobrepeso")
else:
    print(f"Su imc es {imc}, se encuentra en el rango: Obesidad")
