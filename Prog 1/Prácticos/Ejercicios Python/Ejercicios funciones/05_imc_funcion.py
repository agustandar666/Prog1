def calcular_imc(p, a):
    imc = p / a ** 2

    if imc < 18.5:
        return f"Su imc es {imc}, se encuentra en el rango: Bajo peso"
    elif imc >= 18.5 < 25:
        return f"Su imc es {imc}, se encuentra en el rango: Peso normal"
    elif imc >= 25 < 30:
        return f"Su imc es {imc}, se encuentra en el rango: Sobrepeso"
    else:
        return f"Su imc es {imc}, se encuentra en el rango: Obesidad"


altura = float(input("Ingrese altura: "))
peso = float(input("Ingrese peso: "))

print(calcular_imc(peso, altura))
