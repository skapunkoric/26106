# ------------------------------------------------------------
# Ejercicio sencillo 7: Mostrar posición y valor
# ------------------------------------------------------------
"""
Consigna:
Dada la lista numeros = [4, 8, 15, 16, 23, 42], mostrar cada número junto con su posición.

Requisitos:
- Usar while.
- Mostrar el índice y el valor.

Salida esperada aproximada:
Posición 0: 4
Posición 1: 8
Posición 2: 15
"""

reporte_de_Numeros = ""
indice = 0
lista_Numeros = [4, 8, 15, 16, 23, 42]
while indice < len(lista_Numeros):
    
    lista_de_Numeros_por_renglon =f"Posición {indice}: {lista_Numeros[indice]}"   
    indice +=1
    reporte_de_Numeros += lista_de_Numeros_por_renglon + "\n"

print(reporte_de_Numeros)
