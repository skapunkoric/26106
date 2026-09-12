# ==========================================
# FLUJO PRINCIPAL (Encendemos el motor)
# ==========================================
from tabulate import tabulate

lista_stock = [5, 0, 12, 3, 0, 8]
productos = ["A", "B", "C", "D", "E", "F"]


# 1. Tu Chef de los emojis (¡Intacto!)
def mensaje_stock(stock_actual):
    if stock_actual == 0:
        return "❌ [SIN STOCK]"
    elif stock_actual <= 3 and stock_actual > 0:
        return "⚠️ [STOCK BAJO]"
    else:
        return "✅ [STOCK OK]"


# 2. El Mozo que arma la tabla
def mostra_producto():
    # A. Creamos una bandeja vacía
    datos_tabla = []

    # B. Recorremos con zip para tener producto y stock en cada vuelta
    for prod, stock in zip(productos, lista_stock):
        # Le pedimos al Chef el emoji correspondiente
        estado = mensaje_stock(stock)

        # Agregamos la fila (una lista chiquita) a nuestra bandeja grande
        datos_tabla.append([prod, stock, estado])

    # C. AFUERA del for, metemos la bandeja al horno (tabulate) UNA SOLA VEZ
    headers = ["Producto", "Cantidad", "Estado"]
    print(tabulate(datos_tabla, headers=headers, tablefmt="grid"))


# 3. Tu reporte maestro (¡Intacto!)
def reporte():
    cantidad_cero = lista_stock.count(0)
    suma_stock = sum(lista_stock)

    print("\n" + "=" * 34)
    print("== REPORTE DE CONTROL DE STOCK ==")
    print("=" * 34)
    print(f"📦 Total de unidades: {suma_stock}")
    print(f"🚨 Productos agotados (Stock 0): {cantidad_cero}")
    print("=" * 34 + "\n")


# ==========================================
# FLUJO PRINCIPAL
# ==========================================
mostra_producto()
reporte()