# ------------------------------------------------------------
# DATOS (El origen)
# ------------------------------------------------------------
codigos_db = [101, 102, 103, 104]
productos_db = ["Teclado", "Mouse", "Monitor", "Auriculares"]

# Simulamos lo que el usuario tipea en la consola (podés cambiarlo para probar)
input_usuario = "103"


# ------------------------------------------------------------
# CAPA 1: EL CONTROLADOR (Procesamiento y validación)
# ------------------------------------------------------------
def buscar_producto(codigos, productos, codigo_ingresado):
    """Valida el input y busca la coincidencia uniendo ambas listas"""

    # 1. Validación de seguridad (QA puro)
    if not str(codigo_ingresado).isdigit():
        return False, "Error crítico: El código debe ser numérico."

    # Si pasó la validación, lo convertimos a entero de forma segura
    codigo_int = int(codigo_ingresado)

    # 2. El for con 'zip' une las dos listas como un cierre relámpago
    for cod, prod in zip(codigos, productos):
        if cod == codigo_int:
            # Si lo encuentra, corta la función al instante con el return (reemplaza al break)
            return True, prod

    # 3. Si el for dio todas las vueltas y nunca entró al if, significa que no existe
    return False, "Producto no encontrado."


# ------------------------------------------------------------
# CAPA 2: LA VISTA (Reporte visual)
# ------------------------------------------------------------
def mostrar_resultado_busqueda(codigo_buscado, exito, resultado):
    """Muestra el ticket de búsqueda"""
    print("\n" + "=" * 45)
    print(f"{'🔎 SISTEMA DE BÚSQUEDA DE INVENTARIO':^45}")
    print("=" * 45)

    print(f"🔹 Código ingresado: '{codigo_buscado}'")
    print("-" * 45)

    # Usamos el booleano 'exito' para saber qué icono y texto mostrar
    if exito:
        print(f"✅ PRODUCTO ENCONTRADO: {resultado}")
    else:
        print(f"❌ FALLA EN BÚSQUEDA: {resultado}")

    print("=" * 45 + "\n")

# 1. El controlador procesa y devuelve dos cosas: un estado (True/False) y el mensaje/producto
estado_busqueda, mensaje_salida = buscar_producto(codigos_db, productos_db, input_usuario)

# 2. La vista recibe el código que buscamos y los resultados del controlador para imprimirlos
mostrar_resultado_busqueda(input_usuario, estado_busqueda, mensaje_salida)

codigos = [101, 102, 103, 104]
productos = ["Teclado", "Mouse", "Monitor", "Auriculares"]