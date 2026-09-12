#------------------------------------------------------------
# Ejercicio complejo 7: Control de stock
# ------------------------------------------------------------
"""
Consigna:
Dada la lista stock = [5, 0, 12, 3, 0, 8] y productos = ["A", "B", "C", "D", "E", "F"], generar un reporte.

Requisitos:
- Recorrer ambas listas usando el mismo índice.
- Mostrar cada producto con su cantidad disponible.
- Si el stock es 0, mostrar "Sin stock" y contar cuántos productos están agotados.
- Si el stock es menor o igual a 3 pero mayor que 0, mostrar "Stock bajo".
- Calcular el total de unidades disponibles.
- Mostrar al final:
  - Total de unidades.
  - Cantidad de productos sin stock.

Conceptos a practicar:
listas paralelas, while, acumulador, contador, condicionales.
"""
stock = [5, 0, 12, 3, 0, 8]
productos = ["A", "B", "C", "D", "E", "F"]
indice = 0
cantidadDeStockTotal = 0
contador_de_Stock_en_cero = 0
contador_de_Stock_menor_q_3_y_mayor_q_0 = 0
print("=" * 33)
print("== REPORTE DE CONTROL DE STOCK ==")
print("=" * 33)
while indice <len(productos) and indice<len(stock):
    producto_actual = productos[indice]
    stock_actual = stock[indice]
     
    print(f"producto:{producto_actual}|Cantidad:{stock_actual}", end=" ")
    
    cantidadDeStockTotal += stock_actual
    
    if stock_actual == 0:
        print(">> Estado: [SIN STOCK]")
        contador_de_Stock_en_cero += 1
       
    elif stock_actual<= 3 and stock_actual >0: # no lo detecte pero no es rendundante esto lo detecto la IA  
        print(">> Estado: [STOCK BAJO]")
        contador_de_Stock_menor_q_3_y_mayor_q_0 += 1
    else:
      print(" <------- [OK]")
    indice +=1    
print("=" * 30)
print(f"calculo de unidades en stock:{cantidadDeStockTotal}")
print(f"Sin stock en (0):{contador_de_Stock_en_cero}")
print(f"Stock Bajo (con valor menor a 3): {contador_de_Stock_menor_q_3_y_mayor_q_0}")
print("=" * 30)    