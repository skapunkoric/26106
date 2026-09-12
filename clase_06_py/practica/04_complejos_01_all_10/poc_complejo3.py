# ------------------------------------------------------------
# Ejercicio complejo 3: Análisis de temperaturas
# ------------------------------------------------------------
"""""
Consigna:
Dada la lista temperaturas = [22, 25, 19, 30, 28, 18, 24], analizar los datos usando while.

Requisitos:
- Recorrer la lista con un índice. +
- Calcular la suma total de temperaturas. +
- Calcular el promedio.+
- Encontrar la temperatura más alta.+
- Encontrar la temperatura más baja.+
- Contar cuántas temperaturas fueron mayores o iguales a 25.+
- Mostrar un resumen final.+

Conceptos a practicar:
listas, índices, while, acumuladores, comparación de máximos y mínimos.
"""
temperaturas = [22, 25, 19, 30, 28, 18, 24]
contador_temperatura= 0

print() 
print("-" * 70)
print( " RESUMEN FINAL DE TEMPERATURAS " )
print("-" * 70)
print("lista de temperaturas con su corrrespondiente indice en la lista")
 
for temperatura in temperaturas:
    if temperatura >= 25:
        contador_temperatura += 1

    suma_temperaturas =sum(temperaturas)
    maxima_tmperatura =max(temperaturas)
    minima_tmperatura =min(temperaturas)
    promedio_de_temperaturas = suma_temperaturas / len(temperaturas)

print("-" * 70)
print(f"total suma de temperaturas: {suma_temperaturas}°C")
print(f"total promedio de temperaturas: {promedio_de_temperaturas:.2F}°C")
print(f"total cantidad de temperaturas MAYOR A 25°C: {contador_temperatura}")
print(f"total temperatura mas alta : {maxima_tmperatura}°C")
print(f"total temperatura mas baja : {minima_tmperatura}°C")
print("-" * 70)
        


