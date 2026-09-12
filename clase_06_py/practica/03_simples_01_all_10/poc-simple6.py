# ------------------------------------------------------------
# Ejercicio sencillo 6: Recorrer una lista de frutas
# ------------------------------------------------------------
"""
Consigna:
Dada la lista frutas = ["manzana", "banana", "cereza", "durazno"], mostrar cada fruta usando while.

Requisitos:
- Usar una variable indice que empiece en 0.
- Usar len(frutas) en la condición del while.
- Mostrar cada elemento accediendo con frutas[indice].
"""
lista_frutas = ["manzana", "banana", "cereza", "durazno"]
print("=" *30)
print("Reporte de frutas")
print("=" *30)
for i, fruta in enumerate (lista_frutas):
 print(f"|{i:02d}|Fruta:|-->{fruta.capitalize()}")
 



