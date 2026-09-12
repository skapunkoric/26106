"""""
from tabulate import tabulate
from colorama import init, Fore, Style

# Inicializamos colorama para que los colores funcionen bien en la terminal
init(autoreset=True)

lista_stock = [5, 0, 12, 3, 0, 8]  
productos = ["A", "B", "C", "D", "E", "F"]
  
def mensaje_stock(stock_actual):
    # Le sumamos color a cada estado para que resalte en la tabla
    if stock_actual == 0:
        return f"{Fore.RED}❌ [SIN STOCK]"
    elif stock_actual <= 3 and stock_actual > 0:
        return f"{Fore.YELLOW}⚠️  [STOCK BAJO]"
    else:
        return f"{Fore.GREEN}✅ [STOCK OK]"

def mostra_producto():
    datos_tabla = []
    
    for prod, stock in zip(productos, lista_stock):
        estado = mensaje_stock(stock)
        datos_tabla.append([prod, stock, estado])
        
    # === LA CLAVE DEL FIX VISUAL Y DRY ===
    # Esto va AFUERA del for (sin indentar), así se imprime 1 sola vez al final.
    # Definimos los headers una sola vez (DRY).
    headers = [f"{Fore.CYAN}Producto", f"{Fore.CYAN}Cantidad", f"{Fore.CYAN}Estado{Style.RESET_ALL}"]
    
    print("\n" + tabulate(datos_tabla, headers=headers, tablefmt="grid"))

def reporte():
    cantidad_cero = lista_stock.count(0)
    suma_stock = sum(lista_stock)
    
    # Pintamos el reporte final para que quede facha
    print("\n" + Fore.MAGENTA + "=" * 34)
    print("== REPORTE DE CONTROL DE STOCK ==")
    print("=" * 34)
    print(f"{Fore.CYAN}📦 Total de unidades: {suma_stock}")
    print(f"{Fore.RED}🚨 Productos agotados (Stock 0): {cantidad_cero}")
    print(Fore.MAGENTA + "=" * 34 + "\n")    

# ==========================================
# FLUJO PRINCIPAL
# ==========================================
mostra_producto()
reporte()
"""

from tabulate import tabulate
from colorama import init, Fore, Style

init(autoreset=True)

lista_stock = [5, 0, 12, 3, 0, 8]  
productos = ["A", "B", "C", "D", "E", "F"]

def mostra_producto():
    # 1. Creamos TRES bandejas separadas en vez de una
    tabla_ok = []
    tabla_bajo = []
    tabla_cero = []
    
    headers = ["Producto", "Cantidad", "Estado"]
    
    # 2. El for clasifica y manda cada producto a su bandeja
    for prod, stock in zip(productos, lista_stock):
        if stock == 0:
            tabla_cero.append([prod, stock, "❌ [SIN STOCK]"])
        elif stock <= 3:
            tabla_bajo.append([prod, stock, "⚠️  [STOCK BAJO]"])
        else:
            tabla_ok.append([prod, stock, "✅ [STOCK OK]"])

    # 3. Imprimimos cada tabla entera pintada de su color (Bordes y letras)
    
    if tabla_ok: # Solo se imprime si hay productos acá
        print(f"\n{Fore.GREEN}=== PRODUCTOS CON STOCK OK ===")
        # Pintamos la tabla entera de verde
        print(Fore.GREEN + tabulate(tabla_ok, headers=headers, tablefmt="grid"))
        
    if tabla_bajo:
        print(f"\n{Fore.YELLOW}=== PRODUCTOS CON STOCK BAJO ===")
        # Pintamos la tabla entera de amarillo
        print(Fore.YELLOW + tabulate(tabla_bajo, headers=headers, tablefmt="grid"))
        
    if tabla_cero:
        print(f"\n{Fore.RED}=== PRODUCTOS SIN STOCK ===")
        # Pintamos la tabla entera de rojo
        print(Fore.RED + tabulate(tabla_cero, headers=headers, tablefmt="grid"))

def reporte():
    cantidad_cero = lista_stock.count(0)
    suma_stock = sum(lista_stock)
    
    print(f"\n{Fore.CYAN}" + "=" * 34)
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