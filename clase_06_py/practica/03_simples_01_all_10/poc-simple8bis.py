# ------------------------------------------------------------
# Ejercicio sencillo 8: Buscar un color
# ------------------------------------------------------------
"""
Consigna:
Dada la lista colores = ["rojo", "azul", "verde", "amarillo"], buscar si existe el color "verde".

Requisitos:
- Usar while para recorrer la lista.
- Usar una variable encontrado con valor inicial False.
- Si se encuentra el color, cambiar encontrado a True.
- Al final, mostrar si el color fue encontrado o no.
"""
lista_colores = ["rojo", "azul", "verde", "amarillo"]

if "verde" in lista_colores:
    print("el color ✅ VERDE esta en la lista")
else:
    print("el color BUSCADO NO esta en la lista")   