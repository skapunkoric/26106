"""
# =====================================================================
# FUNCIÓN 1: La "Limpiadora" (Responsabilidad Única: un solo string)
# =====================================================================
def limpiar_y_validar_nombre(texto):
    #Recibe un solo texto, le saca los espacios y dice si es válido.
    texto_limpio = texto.strip()

    if texto_limpio != "":
        return texto_limpio  # Si sirve, devuelve el nombre ya limpio
    else:
        return None  # Si no sirve, devuelve un "Nada"


# =====================================================================
# FUNCIÓN 2: La "Jefa" (Responsabilidad Única: manejar el bucle for)
# =====================================================================
def filtrar_lista_completa(lista_sucia):
    #Recibe la lista original, la recorre y arma la lista nueva.
    nombres_validos = []  # La bolsa se crea una sola vez acá arriba

    for dato in lista_sucia:
        # Le mandamos el dato sucio a la Función 1
        resultado = limpiar_y_validar_nombre(dato)

        # Si el resultado no es None (significa que es un nombre válido)
        if resultado is not None:
            nombres_validos.append(resultado)  # Lo guardamos limpio

    return nombres_validos  # Cuando termina el for, escupe la lista llena


# =====================================================================
# FUNCIÓN 3: Tu Reporte (Responsabilidad Única: Mostrar los datos pro)
# =====================================================================
def mostrar_reporte_final(datos_originales, datos_limpios):
    #Muestra la tabla formateada en la consola.
    print("*" * 60)
    print(f"Los datos ORIGINALES son: \n{datos_originales}")
    print("*" * 60)
    print(f"Los nuevos datos SIN ESPACIOS VACÍOS: \n{datos_limpios}")
    print("*" * 60)
    print("\n" + "=" * 40)
    print(f"{'Índice':<10} | {'Nombre Válido':<20}")
    print("-" * 40)

    # Tu enumerate que quedó espectacular (eliminamos el return de adentro)
    for i, nombre in enumerate(datos_limpios):
        print(f"{i:<10} | {nombre:<20}")
    print("=" * 40)


# =====================================================================
# FLUJO PRINCIPAL (Los datos reales que viajan por el circuito)
# =====================================================================
lista_datos = ["Ana", "", "Luis", "   ", "María", "Pedro", ""]

# Paso 1: La jefa filtra la lista usando a la limpiadora internamente
lista_final = filtrar_lista_completa(lista_datos)

# Paso 2: Le pasamos los resultados al reporte para que dibuje la tabla
mostrar_reporte_final(lista_datos, lista_final)
def mostrar_reporte(suma, maxima, minima, promedio, altas):
    # Multiplicar strings es un lujo de Python que en Java requiere un for
    print("\n" + "=" * 45)
    print(" 🌡️  REPORTE DE TEMPERATURAS (QA TEST)  🌡️")
    print("=" * 45)

    # Las f-strings te dejan meter variables directo en el texto
    print(f"🔹 Suma total de temps:   {suma} grados")

    # Magia extra: el :.2f le dice a Python que redondee el promedio a 2 decimales
    print(f"🔹 Promedio general:      {promedio:.2f} grados")
    print(f"🔺 Temperatura más alta:  {maxima} grados")
    print(f"🔻 Temperatura más baja:  {minima} grados")
    print(f"🔥 Días calurosos (>=25): {altas} días")

    print("=" * 45 + "\n")

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
    # Valida el input y busca la coincidencia uniendo ambas listas

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
    #Muestra el ticket de búsqueda
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


# ------------------------------------------------------------
# FLUJO PRINCIPAL (Conexión de los cables)
# ------------------------------------------------------------

# 1. El controlador procesa y devuelve dos cosas: un estado (True/False) y el mensaje/producto
estado_busqueda, mensaje_salida = buscar_producto(codigos_db, productos_db, input_usuario)

# 2. La vista recibe el código que buscamos y los resultados del controlador para imprimirlos
mostrar_resultado_busqueda(input_usuario, estado_busqueda, mensaje_salida)


codigos = [101, 102, 103, 104]
productos = ["Teclado", "Mouse", "Monitor", "Auriculares"]


# ------------------------------------------------------------
# CAPA 1: CONTROLADOR (No imprime NADA, solo busca y devuelve)
# ------------------------------------------------------------
def procesar_busqueda(codigo_ingresado):
    # 1. Validamos que sean números (lo pasamos a string por las dudas)
    if not str(codigo_ingresado).isdigit():
        return False, "El código debe ser un número entero."

    codigo_valido = int(codigo_ingresado)

    # 2. Tu lógica impecable con enumerate
    for i, codigo in enumerate(codigos):
        if codigo == codigo_valido:
            # ¡Lo encontró! Este return corta el bucle al instante y devuelve la data
            return True, productos[i]

    # 3. Si el for dio TODAS las vueltas y nunca entró al if de arriba, llega hasta acá
    return False, f"Código {codigo_valido} no existe en la base de datos."


# ------------------------------------------------------------
# CAPA 2: VISTA (Tu diseño visual, solo se dedica a imprimir)
# ------------------------------------------------------------
def mostrar_ticket(exito, resultado):
    print("\n" + "=" * 40)

    if exito:  # Si el controlador devolvió True
        print(f"{'ID':<10} | {'DESCRIPCIÓN':<20}")
        print("-" * 40)
        print(f"✅ ÉXITO | {resultado}")
    else:  # Si el controlador devolvió False
        print(f"❌ ERROR | {resultado}")

    print("=" * 40 + "\n")


# ------------------------------------------------------------
# FLUJO PRINCIPAL
# ------------------------------------------------------------
# Simulamos un texto que pone el usuario (probá cambiarlo por "104", "999" o "Hola")
input_usuario = "104"

# Atajamos el estado (True/False) y el mensaje (El producto o el error)
estado, mensaje = procesar_busqueda(input_usuario)

# Lo mandamos a la pantalla
mostrar_ticket(estado, mensaje)


# 1. Definimos las reglas del juego arriba de todo
password_correcto = "python123"
max_intentos = 3


def ingreso_login():
    # 2. El bucle arranca
    for nro_intento in range(1, max_intentos + 1):

        # Todo esto está ADENTRO del for (tiene sangría)
        passwordIngresado = input(f"Intento {nro_intento} / {max_intentos} - Ingresa tu Contraseña: ").strip()

        # Validamos si es correcta
        if passwordIngresado == password_correcto:
            # Si acierta, el return destruye el bucle y devuelve el éxito
            return True, "✅ Acceso permitido"

        # Si llega acá, es porque le erró (o lo mandó vacío).
        # Calculamos la resta de intentos.
        intentos_restantes = max_intentos - nro_intento

        # Si todavía le queda vida, le avisamos para que el bucle dé la próxima vuelta
        if intentos_restantes > 0:
            print(f"❌ Password no válido. Te quedan {intentos_restantes} intentos.")

    # 3. AFUERA DEL BUCLE: Si el for dio las 3 vueltas y nunca acertó...
    return False, "🚫 Acceso bloqueado. Te quedaste sin intentos."


# ==========================================
# FLUJO PRINCIPAL
# ==========================================
estado, mensaje = ingreso_login()

print("\n" + "=" * 30)
print(mensaje)
print("=" * 30)

# ------------------------------------------------------------
# Ejercicio complejo 6: Menú interactivo
# ------------------------------------------------------------

cursos = ["Introduccion a Python", "Java", "IA Inteligencia Artificial"]


def saludo():
    print("\n>>>>>>...Hola Bienvenido/a ......")
    input("\nPresioná Enter para volver al menú...")


def menu():
    print("\n==== Opciones: ====")
    print("*" * 30)
    print("1 - Saludar ")
    print("2 - Mostrar los números del 1 al 5")
    print("3 - Mostrar una lista de cursos")
    print("4 - Salir")
    print("*" * 30)


def mostra_numeros():
    # 1. La lista nace y muere acá adentro, así no engorda con cada pasada
    lista_numerica = []

    for i in range(1, 6):
        lista_numerica.append(i)

    # 2. Los prints y el input van AFUERA del for para que lo pida 1 sola vez
    print("\n>>> Procesando números...")
    print(".........numeros del 1 al 5...........")
    print(f"La lista numerica es: {lista_numerica}")
    input("\nPresioná Enter para volver al menú...")


def lista_cursos():
    print(f"\nLos cursos disponibles son: {cursos}")
    input("\nPresioná Enter para volver al menú...")


def finally_program():
    print("\n..PROGRAMA Finalizado ....")


def error():
    print("\n[!] Opcion invalida. Elige una opción del 1 al 4.")
    input("\nPresioná Enter para volver al menú...")


def error_dos():
    print("\n[!] Error: Por favor, ingresa solo números.")
    print(".........OPCION INVALIDA ....")
    input("\nPresioná Enter para volver al menú...")


# El Chef Controlador
def validacion_menu():
    # Arranca el bucle infinito
    while True:
        # A. Mostramos el menú EN CADA VUELTA
        menu()

        # B. Pedimos la opción EN CADA VUELTA (El strip previene vacíos molestos)
        opcion = input("\nSeleccione su opción: ").strip()

        # El Patovica evalúa
        if opcion.isdigit():
            opcion = int(opcion)
            match opcion:
                case 1:
                    saludo()
                case 2:
                    mostra_numeros()
                case 3:
                    lista_cursos()
                case 4:
                    finally_program()
                    break  # C. LA CLAVE DE TODO: El break mata el while True
                case _:
                    error()
        else:
            error_dos()
validacion_menu()

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

from tabulate import tabulate

lista_de_puntajes = [1200, 900, 450, 300, 750, 1200, 100]

# --- 1. Cálculos de métricas ---
maximo = max(lista_de_puntajes)
minimo = min(lista_de_puntajes)
promedio = sum(lista_de_puntajes) / len(lista_de_puntajes)
tops = [p for p in lista_de_puntajes if p >= 800]

# --- 2. Armamos una lista "plana" con absolutamente todo lo que queremos mostrar ---
elementos_grilla = []

# Metemos los 7 puntajes originales con su ID
for i, p in enumerate(lista_de_puntajes, start=1):
    elementos_grilla.append(f"[{i:02d}] Pts: {p}")

# Agregamos las métricas como si fueran más celdas de la grilla
elementos_grilla.append(f"🥇 Max: {maximo}")
elementos_grilla.append(f"🥉 Min: {minimo}")
elementos_grilla.append(f"📊 Prom: {promedio:.1f}")
elementos_grilla.append(f"🏆 Tops: {len(tops)}")

# --- 3. RELLENO AUTOMÁTICO (El truco pro) ---
# Queremos columnas de 3. Si el total no es divisible por 3, agregamos strings vacíos ""
while len(elementos_grilla) % 3 != 0:
    elementos_grilla.append("") # Rellena los huecos del final

# --- 4. Convertimos la lista plana en una matriz de 3 columnas (filas de 3 elementos) ---
matriz_4x3 = []
for i in range(0, len(elementos_grilla), 3):
    matriz_4x3.append(elementos_grilla[i : i + 3])

# --- 5. Dibujamos con Tabulate ---
headers = ["SECTOR A", "SECTOR B", "ESTADÍSTICAS"]
print("\n🖥️ TABLERO DE CONTROL INTEGRADO (MATRIZ 4x3)\n")
print(tabulate(matriz_4x3, headers=headers, tablefmt="grid"))
print()

import re
from tabulate import tabulate
from colorama import init, Fore, Style

# Inicializamos los colores en la terminal
init(autoreset=True)

puntajes = [450, 900, 1200, 300, 750, 1200, 100]


def analizar_ranking(lista_puntajes):
    # Validamos por seguridad si la lista viene vacía (Buen hábito de QA)
    if not lista_puntajes:
        print(Fore.RED + "⚠️ La lista de puntajes está vacía.")
        return

    # Inicializamos variables con el primer elemento para empezar a comparar
    maximo = lista_puntajes[0]
    minimo = lista_puntajes[0]
    suma_total = 0
    contador_mayores_800 = 0
    destacados = []

    # --- El Bucle de Análisis ---
    for puntaje in lista_puntajes:
        suma_total += puntaje

        # Encontramos máximos y mínimos sobre la marcha
        if puntaje > maximo:
            maximo = puntaje
        if puntaje < minimo:
            minimo = puntaje

        # Requisito extra: Filtrar destacados >= 800
        if puntaje >= 800:
            contador_mayores_800 += 1
            destacados.append([puntaje])  # Lo guardamos como lista interna para tabulate

    # Calculamos el promedio general
    promedio = suma_total / len(lista_puntajes)

    # Contamos cuántas veces se repite el máximo ya encontrado
    cantidad_maximos = lista_puntajes.count(maximo)

    # ==========================================
    # DISEÑO DE SALIDA VISUAL (Tabulate + Colorama)
    # ==========================================
    print("\n" + Fore.CYAN + "=" * 50)
    print(Fore.CYAN + "📊 REPORTE ESTADÍSTICO DE PUNTAJES")
    print(Fore.CYAN + "=" * 50)

    # 1. Tabla de métricas generales
    datos_metricas = [
        ["🏆 Puntaje Máximo", f"{Fore.GREEN}{maximo} ({cantidad_maximos} veces)"],
        ["📉 Puntaje Mínimo", f"{Fore.RED}{minimo}"],
        ["⚖️ Promedio General", f"{Fore.YELLOW}{promedio:.2f}"],
        ["🚀 Cantidad con ≥ 800", f"{Fore.BLUE}{contador_mayores_800}"]
    ]

    headers_resumen = [Fore.MAGENTA + "Métrica", Fore.MAGENTA + "Resultado" + Style.RESET_ALL]
    print(tabulate(datos_metricas, headers=headers_resumen, tablefmt="grid"))

    # 2. Tabla secundaria para los destacados (Opcional)
    if destacados:
        print(Fore.YELLOW + "\n⭐ RANKING DE JUGADORES DESTACADOS (≥ 800) ⭐")
        headers_destacados = [Fore.YELLOW + "Puntaje"]
        print(tabulate(destacados, headers=headers_destacados, tablefmt="grid"))


# Ejecutamos el análisis
analizar_ranking(puntajes)
"""

from tabulate import tabulate


def ranking_puntajes():
    lista_puntajes = [450, 900, 1200, 300, 750, 1200, 100]

    maximo = max(lista_puntajes)
    minimo = min(lista_puntajes)
    promedio_puntajes = sum(lista_puntajes) / len(lista_puntajes)

    # List comprehension profesional para filtrado
    lista_tops = [p for p in lista_puntajes if p >= 800]
    repeticiones_maximo = lista_puntajes.count(maximo)

    # Construcción de matriz para visualización unificada
    elementos_grilla = [
        ["🥇 Puntaje Máximo", f"{maximo} (Repetido {repeticiones_maximo} veces)"],
        ["🥉 Puntaje Mínimo", f"{minimo}"],
        ["📊 Promedio General", f"{promedio_puntajes:.1f}"],
        ["🚀 Cantidad Destacados (≥800)", f"{len(lista_tops)}"]
    ]

    headers = ["Métrica de Rendimiento", "Resultado Análisis"]
    print("\\n" + tabulate(elementos_grilla, headers=headers, tablefmt="grid"))


ranking_puntajes()