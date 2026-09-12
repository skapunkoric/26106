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
lista_stock = [5, 0, 12, 3, 0, 8]  
productos = ["A", "B", "C", "D", "E", "F"]


print("=" * 33)
print("== REPORTE DE CONTROL DE STOCK ==")
print("=" * 33)

for i, prod in enumerate(productos):
        
    stock_actual  = lista_stock[i]

    print(f"producto: {prod} | Cantidad: {stock_actual:<3}", end=" ")
    
    if stock_actual == 0:
        print(">>Estado ❌ [SIN STOCK]")
        
    
    elif stock_actual <=3 and stock_actual >0:
        print(">>Estado ⚠️  [STOCK BAJO]")
    
    else:
        print(">>Estado ✅ [STOCK OK]")
    
cantidad_cero = lista_stock.count(0)
suma_stock =sum(lista_stock)
print("=" * 30) 
print(f"total de unidades:{suma_stock}")
print(f"cantidad de productos con stock en cero:{cantidad_cero}")
print("=" * 30) 
