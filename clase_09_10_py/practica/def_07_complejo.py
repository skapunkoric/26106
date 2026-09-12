# ------------------------------------------------------------
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
"""
from tabulate import tabulate
lista_stock = [5, 0, 12, 3, 0, 8]  
productos = ["A", "B", "C", "D", "E", "F"]
  
def mensaje_stock(stock_actual):
    if stock_actual == 0:
        return "❌ [SIN STOCK]"
    elif stock_actual <=3 and stock_actual >0:
        return " ⚠️  [STOCK BAJO]"
    else:
        return"✅ [STOCK OK]"

def mostra_producto():
    datos_tabla = []
    for prod, stock in zip(productos, lista_stock):
        estado = mensaje_stock(stock)
        headers = ["¨Producto","Cantidad"]
        datos_tabla.append([prod,stock,estado])
    headers=["Prodcto", "Cantidad", "Estado"]
    print(tabulate(datos_tabla, headers=headers, tablefmt="grid"))

def reporte():
    cantidad_cero = lista_stock.count(0)
    suma_stock =sum(lista_stock)
    
    print("\n" + "=" * 34)
    print("== REPORTE DE CONTROL DE STOCK ==")
    print("=" * 34)
    print(f"📦 Total de unidades: {suma_stock}")
    print(f"🚨 Productos agotados (Stock 0): {cantidad_cero}")
    print("=" * 34 + "\n")    
    



mostra_producto()
reporte()