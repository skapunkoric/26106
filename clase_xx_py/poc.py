"""
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
#-------------------------------------------------------------------------------------------
def registro_gastos():
    print("=== REGISTRO DE GASTOS CONTABLES ===")

    total_gastado = 0
    cantidad_gastos = 0

    # Usamos una variable de control inicializada para entrar al bucle de forma limpia
    gasto_ingresado = -1

    while gasto_ingresado != 0:
        texto_gasto = input(f"💵 Ingrese el importe del gasto #{cantidad_gastos + 1} (Escriba 0 para terminar): ").strip()

        # Validamos que sea un número (puede ser decimal) antes de convertirlo
        try:
            gasto_ingresado = float(texto_gasto)

            if gasto_ingresado < 0:
                print("⚠️ Error: El importe no puede ser un número negativo. Intente de nuevo.")
                gasto_ingresado = -1  # Forzamos que se mantenga en el bucle ignorando el negativo
            elif gasto_ingresado > 0:
                total_gastado += gasto_ingresado
                cantidad_gastos += 1

        except ValueError:
            print("⚠️ Error: Por favor, ingrese un monto numérico válido.")
            gasto_ingresado = -1

    # --- Resumen Final ---
    print("\\n" + "="*40)
    print("📊 RESUMEN FINAL DE GASTOS")
    print("="*40)
    print(f"💰 Total gastado: ${total_gastado:.2f}")
    print(f"📋 Cantidad de gastos cargados: {cantidad_gastos}")

    if cantidad_gastos > 0:
        promedio = total_gastado / cantidad_gastos
        print(f"⚖️ Promedio por gasto: ${promedio:.2f}")
    else:
        print("ℹ️ No se registraron gastos para calcular el promedio.")

registro_gastos()
import re
patron_estricto = r"^[0-9]+(\.[0-9]+)?$"
acumulaGastos = 0.0
contadorGastos= 0
print("📋 REGISTRO DE GASTOS tipo BILLETERA VIRTUAL")
print("-" * 40)

