# ------------------------------------------------------------
# Ejercicio complejo 10: Ranking de puntajes
# ------------------------------------------------------------
"""
Consigna:
Dada la lista puntajes = [450, 900, 1200, 300, 750, 1200, 100], analizar el ranking usando while.

Requisitos:
- Recorrer la lista con while.
- Encontrar el puntaje máximo.
- Encontrar el puntaje mínimo.
- Calcular el promedio de puntajes.
- Contar cuántos puntajes son mayores o iguales a 800.
- Contar cuántas veces aparece el puntaje máximo.
- Mostrar un resumen final con todos los datos.

Extra opcional:
- Crear una nueva lista llamada destacados con los puntajes mayores o iguales a 800.

Conceptos a practicar:
while, listas, índices, acumuladores, máximos, mínimos, contadores, append().
"""
lista_de_puntajes = [1200, 900, 450, 300, 750, 1200, 100]
lista_puntajes_mayor_a_800 = []

maximo = max(lista_de_puntajes)
minimo = min(lista_de_puntajes)
promedio_puntajes = sum(lista_de_puntajes) /len(lista_de_puntajes)
cantidad_maxima = lista_de_puntajes.count(maximo)
for puntaje in lista_de_puntajes:
    if puntaje >=800:
        lista_puntajes_mayor_a_800.append(puntaje)
cantidad_puntaje_800 = len(lista_puntajes_mayor_a_800)

print("")
print("="*50)
print("           REPORTE DE PUNTAJES ")
print("="*50)
print(f"La lista de puntajes son      {lista_de_puntajes}")
print(f"Puntaje Mas Alto:             {maximo} y aparece : {cantidad_maxima} veces") 
print(f"Puntaje Mas Bajo:             {minimo}") 
print(f"Promedio General de Puntajes: {promedio_puntajes:.2f}")
print(f"PUNTAJES ARRIBA DE (>=800):   {cantidad_puntaje_800} cant")
print("="*50)    
print(" Detalle opcional nueva lista con puntajes TOP (>=800): ")
print (f"---------------------------->{lista_puntajes_mayor_a_800}")
print("")





