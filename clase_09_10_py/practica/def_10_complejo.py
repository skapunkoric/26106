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
"""
from tabulate import tabulate

lista_puntajes = [450, 900, 1200, 300, 750, 1200, 100]
lista_puntajes_mayor_a_800 = []

def ranking_puntajes():
    
    maximo = max(lista_puntajes)
    minimo = min(lista_puntajes)
    promedio_puntajes = sum(lista_puntajes) / len(lista_puntajes)
    lista_puntajes_mayor_a_800 = [p800 for p800 in lista_puntajes if p800 >= 800]
    repeticiones_max = lista_puntajes.count(maximo)
    
# armar la grilla
    elementos_grilla = [
        [f"🥇 Max : {maximo}"],
        [f"🥉 Min : {minimo}"],
        [f"📊 ️Prom : {promedio_puntajes:.1f}"],
        [f"🥇 Tops800 : {len(lista_puntajes_mayor_a_800)}"],
        [f"🥇 TopsMax : {repeticiones_max}"],
        [f"🥇 lista800 : {lista_puntajes_mayor_a_800}"]
]
    headers = ["Métrica de Rendimiento", "Resultado Análisis"]
    #print("\\n" + tabulate(elementos_grilla, headers=headers, tablefmt="grid"))
    print(tabulate(elementos_grilla, headers=headers, tablefmt="grid"))
ranking_puntajes()

        