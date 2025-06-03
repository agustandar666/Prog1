from tg1_funciones_descifrar import *

texto_i = "msejiwihwxeievstixgvwiniweirpqvivemjwghihsymikrwgsedilenrwqixiiw ivwzhiyimtwwrimsegmxmgipj"
texto_normalizado_i = normalizar(texto_i)
texto_desplazado_i = desplazar(texto_normalizado_i, -3)
texto_permutado_i = permutar(texto_desplazado_i)
texto_revelado_i = texto_permutado_i[::-1]
input(f"Se ha descifrado el mensaje:\n> {texto_revelado_i}\nENTER para volver al menú.")