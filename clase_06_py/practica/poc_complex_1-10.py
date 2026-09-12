"""""
max_intentos = 3
password_correcto = "python123"

# El range(1, 4) nos da los números 1, 2 y 3.
for nro_intento in range(1, max_intentos + 1):
    
    passwordIngresado = input(f"Intento {nro_intento}/{max_intentos} - Ingresá tu contraseña: ")
    
    if passwordIngresado == password_correcto:
        print("✅ Acceso permitido")
        break
    else:
        intentos_restantes = max_intentos - nro_intento
        
        if intentos_restantes > 0:
            print(f"❌ Password no válido. Te quedan {intentos_restantes} intentos.")
        else:
            print("🚫 Acceso bloqueado. Te quedaste sin intentos.")

     

max_intentos = 3
password_correcto = "python123"

for nro_intento in range(1, max_intentos + 1):
    # Usamos .strip() para limpiar espacios accidentales en los extremos
    password_ingresado = input(f"Intento {nro_intento}/{max_intentos} - Ingresá tu contraseña: ").strip()
    
    # --- BLOQUE DE VALIDACIÓN DE CALIDAD ---
    if not password_ingresado:
        print("⚠️ Error: El campo no puede estar vacío.")
        # No gastamos intento si se equivocó así, usamos continue para volver a pedir
        continue 
        
    if " " in password_ingresado:
        print("⚠️ Error: La contraseña no debe contener espacios internos.")
        continue
    # ---------------------------------------

    if password_ingresado == password_correcto:
        print("✅ Acceso permitido. ¡Bienvenido, Gombre!")
        break
    else:
        intentos_restantes = max_intentos - nro_intento
        
        if intentos_restantes > 0:
            print(f"❌ Password incorrecto. Te quedan {intentos_restantes} intentos.")
        else:
            print("🚫 Acceso bloqueado. Sistema de seguridad activado.")


max_intentos = 3
password_correcto = "python123"

for nro_intento in range(1, max_intentos + 1):
    password_ingresado = input(f"Intento {nro_intento}/{max_intentos}: ").strip()

    if not password_ingresado:
        print("⚠️ El campo está vacío.")
        continue

    if password_ingresado == password_correcto:
        print("✅ Acceso permitido.")
        break
    
    intentos_restantes = max_intentos - nro_intento
    if intentos_restantes > 0:
        print(f"❌ Error. Quedan {intentos_restantes} intentos.")
else:
    # Este bloque solo corre si el for terminó y NUNCA se hizo break
    print("🚫 Acceso bloqueado. Sistema de seguridad activado.")


temperaturas = [22, 25, 19, 30, 28, 18, 24]

# Cálculos directos (Clean Code)
suma_t = sum(temperaturas)
promedio = suma_t / len(temperaturas)
t_max = max(temperaturas)
t_min = min(temperaturas)

# Filtrado nivel Pro
mayores_25 = [t for t in temperaturas if t >= 25]

print("=" * 40)
print(f"{'REPORTE METEOROLÓGICO':^40}") # Centrado
print("=" * 40)
print(f"Promedio: {promedio:.2f}°C")
print(f"Máxima:   {t_max}°C")
print(f"Mínima:   {t_min}°C")
print(f"Días >= 25°C: {len(mayores_25)}")
print("=" * 40)


codigos = [101, 102, 103, 104]
productos = ["Teclado", "Mouse", "Monitor", "Auriculares"]

print(f"{'CÓDIGO':<10} | {'PRODUCTO':<15}") # Encabezado
print("-" * 30)

for i, codigo in enumerate(codigos):
    # Reservamos 10 espacios para el código y 15 para el producto
    print(f"{codigo:<10} | {productos[i]:<15}")



codigos = [101, 102, 103, 104]
productos = ["Teclado", "Mouse", "Monitor", "Auriculares"]
producto_encontrado = False

# --- Entrada de datos con validación ---
entrada = input("Ingrese código a buscar: ").strip()

if entrada.isdigit():
    codigo_a_buscar = int(entrada)
    
    # --- Encabezado del reporte (Visual Pro) ---
    print("\n" + "="*35)
    print(f"{'ID':<10} | {'DESCRIPCIÓN':<20}")
    print("-" * 35)

    # --- Búsqueda con Enumerate (Nivel Pro) ---
    for i, codigo in enumerate(codigos):
        if codigo == codigo_a_buscar:
            # Imprimimos la fila alineada
            print(f"{codigo:<10} | {productos[i]:<20}")
            producto_encontrado = True
            break # Encontrado, salimos del bucle
    
    # --- Manejo del "Camino Infeliz" (QA Mindset) ---
    if not producto_encontrado:
        print(f"{'ERROR':<10} | Código {codigo_a_buscar} no existe.")
    
    print("="*35)

else:
    print("\n[!] Error: El código debe ser un número entero.")

datos = ["Ana", "", "Luis", "   ", "María", "Pedro", ""]
nuevos_datos = []

for dato in datos:
    dato = dato.strip()  # MAGIA: Guardamos el string limpio en la variable
    if dato != "":       # Ahora sí, el que era "   " pasa a ser "" y no entra al IF
        nuevos_datos.append(dato)

print("\n" + "*" * 60)
print(f"Los datos ORIGINALES son: \n{datos}")
print("*" * 60)
print(f"Los NUEVOS datos SIN ESPACIOS VACÍOS son: \n{nuevos_datos}")
print("*" * 60)


import re

deposito_acumulado = 0
contador_depositos = 0

print("=" * 50)
print("=== OBJETIVO DE AHORRO ===")
print("=" * 50)

objetivo_input = input("\nIngresá el monto que querés ahorrar: $")

if re.match(r"^[0-9]+$", objetivo_input) and int(objetivo_input) > 0:
    objetivo = int(objetivo_input)

    for _ in range(1000):  # límite arbitrario alto
        deposito_input = input("\nIngresá un depósito: $")

        if not re.match(r"^[0-9]+$", deposito_input) or int(deposito_input) <= 0:
            print("❌ Ingreso no válido.")
            continue

        deposito_acumulado += int(deposito_input)
        contador_depositos += 1
        falta = max(0, objetivo - deposito_acumulado)
        print(f"✅ Acumulado: ${deposito_acumulado} | Falta: ${falta}")

        if deposito_acumulado >= objetivo:  # condición de corte
            print("\n🎯 ¡Objetivo alcanzado!")
            print(f"   Total depósitos: {contador_depositos}")
            break
else:
    print("❌ Objetivo inválido.")

import re

deposito_acumulado = 0
contador_depositos = 0

print("=" * 50)
print("=== OBJETIVO DE AHORRO ===")
print("=" * 50)

objetivo_input = input("\nIngresá el monto que querés ahorrar: $")

if re.match(r"^[1-9][0-9]*$", objetivo_input):
    objetivo = int(objetivo_input)

    for _ in range(1000):
        deposito_input = input("\nIngresá un depósito: $")

        if not re.match(r"^[1-9][0-9]*$", deposito_input):
            print("❌ Ingreso no válido, solo números enteros positivos.")
            continue

        deposito_acumulado += int(deposito_input)
        contador_depositos += 1

        if deposito_acumulado >= objetivo:
            print("\n🎯 ¡Objetivo alcanzado!")
            print(f"   Total ahorrado: ${deposito_acumulado}")
            print(f"   Total depósitos: {contador_depositos}")
            break

        falta = objetivo - deposito_acumulado  # nunca negativo, el break corta antes
        print(f"✅ Acumulado: ${deposito_acumulado} | Falta: ${falta}")

else:
    print("❌ Objetivo inválido.")


lista_de_puntajes = [1200, 900, 450, 300, 750, 1200, 100]
lista_puntajes_mayor_a_800 = []

# esto va AFUERA del for, operan sobre la lista completa
maximo = max(lista_de_puntajes)
minimo = min(lista_de_puntajes)
promedio_puntajes = sum(lista_de_puntajes) / len(lista_de_puntajes)
cantidad_maxima = lista_de_puntajes.count(maximo)

for puntaje in lista_de_puntajes:
    if puntaje >= 800:
        lista_puntajes_mayor_a_800.append(puntaje)

cantidad_puntaje_800 = len(lista_puntajes_mayor_a_800)

print("")
print("="*50)
print("           REPORTE DE PUNTAJES ")
print("="*50)
print(f"La lista de puntajes son      {lista_de_puntajes}")
print(f"Puntaje Mas Alto:             {maximo} y aparece: {cantidad_maxima} veces")
print(f"Puntaje Mas Bajo:             {minimo}")
print(f"Promedio General de Puntajes: {promedio_puntajes:.2f}")
print(f"PUNTAJES ARRIBA DE (>=800):   {cantidad_puntaje_800} cant")
print("="*50)
print(" Detalle opcional nueva lista con puntajes TOP (>=800): ")
print(f"---------------------------->{lista_puntajes_mayor_a_800}")


lista_de_puntajes = [1200, 900, 450, 300, 750, 1200, 100]
lista_puntajes_mayor_a_800 = []

maximo = max(lista_de_puntajes)
minimo = min(lista_de_puntajes)
promedio_puntajes = sum(lista_de_puntajes) / len(lista_de_puntajes)
cantidad_maxima = lista_de_puntajes.count(maximo)

for puntaje in lista_de_puntajes:
    if puntaje >= 800:
        lista_puntajes_mayor_a_800.append(puntaje)

cantidad_puntaje_800 = len(lista_puntajes_mayor_a_800)

# ── helpers visuales ──────────────────────────────────────
ANCHO = 52

def linea(car="─"):
    print(car * ANCHO)

def fila(etiqueta, valor):
    print(f"  {etiqueta:<30} {valor}")

# ── reporte ───────────────────────────────────────────────
print()
linea("═")
print("🏆  REPORTE DE PUNTAJES".center(ANCHO))
linea("═")

fila("📋 Lista completa:",       str(lista_de_puntajes))
linea()
fila("🥇 Puntaje más alto:",     f"{maximo}  (aparece {cantidad_maxima}x)")
fila("🥉 Puntaje más bajo:",     f"{minimo}")
fila("📊 Promedio general:",     f"{promedio_puntajes:.2f}")
fila("🔥 Puntajes TOP (≥800):",  f"{cantidad_puntaje_800} encontrados")
linea("═")

print("  📌 Detalle TOP:".ljust(ANCHO))
for p in lista_puntajes_mayor_a_800:
    print(f"     {'█' * (p // 100)}  {p}")

linea("═")
print()

lista_de_puntajes = [1200, 900, 450, 300, 750, 1200, 100]
lista_puntajes_mayor_a_800 = []

# --- MÉTRICAS (Usemos las funciones de Python limpio) ---
maximo = max(lista_de_puntajes)
minimo = min(lista_de_puntajes)
promedio_puntajes = sum(lista_de_puntajes) / len(lista_de_puntajes)

print("=" * 55)
print(f"| {'ID':<4} | {'PUNTAJE':<12} | {'ESTADO / ALERTA':<25} |")
print("=" * 55)

# --- BUCLE PRO CON ENUMERATE ---
for i, puntaje in enumerate(lista_de_puntajes, start=1):

    # IF ternario para meterle color y alertas visuales en una sola línea
    if puntaje == maximo:
        estado = "🥇 MÁXIMO HISTÓRICO"
    elif puntaje == minimo:
        estado = "🥉 MÍNIMO REGISTRADO"
    elif puntaje >= 800:
        estado = "🔥 TOP CRACK"
        lista_puntajes_mayor_a_800.append(puntaje)  # Lo guardamos si es >= 800
    else:
        estado = "⚡ REGULAR"

    # Encolumnamos todo con grosores fijos: ID (4), Puntaje (12), Estado (25)
    print(f"| {i:02d} | {puntaje:<12} | {estado:<25} |")

print("=" * 55)
# --- RESUMEN FINAL ---
print(f"📊 Promedio General:  {promedio_puntajes:.2f}")
print(f"🏆 Cantidad de TOPs:  {len(lista_puntajes_mayor_a_800)} jugadores")
print("=" * 55)
"""

lista_de_puntajes = [1200, 900, 450, 300, 750, 1200, 100]
lista_puntajes_mayor_a_800 = []

# --- TU LÓGICA (Perfecta y eficiente) ---
maximo = max(lista_de_puntajes)
minimo = min(lista_de_puntajes)
promedio_puntajes = sum(lista_de_puntajes) / len(lista_de_puntajes)
cantidad_maxima = lista_de_puntajes.count(maximo)

print("=" * 55)
print(f"| {'ID':<4} | {'PUNTAJE':<12} | {'ANÁLISIS DE RENDIMIENTO':<25} |")
print("=" * 55)

# --- RECORRIDO EN TABLA ENCOLUMNADA ---
for i, puntaje in enumerate(lista_de_puntajes, start=1):
    # Cargamos tu lista de TOPs de forma limpia
    if puntaje >= 800:
        lista_puntajes_mayor_a_800.append(puntaje)

    # Asignamos etiquetas fijas según tus métricas
    if puntaje == maximo:
        estado = "🥇 MÁXIMO (Record)"
    elif puntaje == minimo:
        estado = "🥉 MÍNIMO"
    elif puntaje >= 800:
        estado = "🔥 TOP PLAYER"
    else:
        estado = "⚡ REGULAR"

    # El secreto del éxito: anchos fijos 4, 12 y 25
    print(f"| {i:02d} | {puntaje:<12} | {estado:<25} |")

print("=" * 55)
# --- CUADRO DE METRICAS GENERALES ---
print(f" 📊 Promedio General:  {promedio_puntajes:.2f}")
print(f" 🔁 Repeticiones Max:  El {maximo} aparece {cantidad_maxima} veces")
print(f" 🏆 Jugadores ≥ 800:  {len(lista_puntajes_mayor_a_800)} encontrados")
print("=" * 55)
print(f" 📌 Detalle TOP:       {lista_puntajes_mayor_a_800}")
print("=" * 55)
