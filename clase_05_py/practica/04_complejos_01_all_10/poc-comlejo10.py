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
lista_de_Puntajes = [1200, 900, 450, 300, 750, 1200, 100]
puntaje_Maximo = lista_de_Puntajes[0]
puntaje_Minimo = lista_de_Puntajes[0]
contador_de_puntaje_maximo =0
suma_de_Puntajes =0
promedio_de_Puntajes = 0.0
contador_de_Mayor_a_800 = 0
lista_de_Puntajes_Mayor_a_800 = []
indice = 0

while indice < len(lista_de_Puntajes):
    lista_de_puntaje = lista_de_Puntajes[indice]
    
    if  lista_de_puntaje>puntaje_Maximo:
        puntaje_Maximo = lista_de_puntaje
    if  lista_de_puntaje == puntaje_Maximo:
        contador_de_puntaje_maximo += 1
    
    
    if  lista_de_puntaje<puntaje_Minimo:
         puntaje_Minimo = lista_de_puntaje

    if  lista_de_puntaje>= 800:
        contador_de_Mayor_a_800 += 1
        lista_de_Puntajes_Mayor_a_800.append(lista_de_puntaje)
    
    
    suma_de_Puntajes += lista_de_puntaje
    promedio_de_Puntajes = suma_de_Puntajes / len(lista_de_Puntajes)
    

    indice += 1
print("")
print("="*50)
print("           REPORTE DE PUNTAJES ")
print("="*50)
print(f"La lista de puntajes son      {lista_de_Puntajes}")
print(f"Puntaje Mas Alto:             {puntaje_Maximo} y aparece : {contador_de_puntaje_maximo} veces") 
print(f"Puntaje Mas Bajo:             {puntaje_Minimo}") 
print(f"Promedio General de Puntajes: {promedio_de_Puntajes:.2f}")
print(f"PUNTAJES ARRIBA DE (>=800):   {contador_de_Mayor_a_800} cant")
print("="*50)    
print(" Detalle opcional nueva lista con puntajes TOP (>=800): ")
print (f"---------------------------->{lista_de_Puntajes_Mayor_a_800}")
print("")





