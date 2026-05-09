
# ------------------------------------------------------------
# Ejercicio sencillo 9: Cortar búsqueda con break
# ------------------------------------------------------------
"""
Consigna:
Dada la lista claves = ["abc", "123", "python", "admin"], buscar la clave "python".

Requisitos:
- Usar while.
- Cuando se encuentre "python", mostrar "Clave encontrada".
- Usar break para detener el bucle inmediatamente.
"""


claves = ["abc", "123", "python", "admin"]

indice = 0
while indice < len(claves):
    lista_actual_clave = claves[indice]

    if "python" == lista_actual_clave:
        print(" clave encontrada")
        break
    indice += 1


