def formato_nombre(n, a, ci):
    return f"{a}, {n} tiene el número de cédula: {ci}"


nombre = input("Ingrese nombre: ").capitalize()
apellido = input("Ingrese apellido: ").capitalize()
cedula = int(input("Ingrese cédula: "))

print(formato_nombre(nombre, apellido, cedula))