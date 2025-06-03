# Pedidos al usuario de texto a evaluar y letra a contar
texto = input("Ingresar texto: ").lower()
letra = input("Ingresar letra: ").lower()


def contar_letra(text, letter):
    # Cuenta las veces que aparece la letra en el texto usando el método
    veces = text.count(letter)
    return f"La letra '{letter}' aparece {veces} en el texto."


print(contar_letra(texto, letra))
