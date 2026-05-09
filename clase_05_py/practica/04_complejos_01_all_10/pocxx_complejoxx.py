"""""
stock = [5, 0, 12, 3, 0, 8]
productos = ["A", "B", "C", "D", "E", "F"]
indice = 0

cantidadDeStockTotal = 0
contador_de_Stock_en_cero = 0
contador_de_Stock_bajo = 0

print("=== REPORTE DE CONTROL DE STOCK ===\n")

while indice < len(productos):
    producto_actual = productos[indice]
    stock_actual = stock[indice]
    
    print(f"Producto: {producto_actual} | Cantidad: {stock_actual}")
    
    # Acumulamos el total
    cantidadDeStockTotal += stock_actual
    
    # Lógica de estados del producto
    if stock_actual == 0:
        print(">> Estado: [SIN STOCK]") # Esto pide la consigna
        contador_de_Stock_en_cero += 1
    
    elif stock_actual <= 3: # Si no es 0, pero es <= 3
        print(">> Estado: [STOCK BAJO]") # Esto pide la consigna
        contador_de_Stock_bajo += 1
    
    print("-" * 30) # Separador visual
    
    indice += 1 # El motor siempre al final

# Resultados finales
print(f"\nTotal de unidades disponibles: {cantidadDeStockTotal}")
print(f"Productos agotados: {contador_de_Stock_en_cero}")
print(f"Productos con stock bajo: {contador_de_Stock_bajo}")

stock = [5, 0, 12, 3, 0, 8]
productos = ["A", "B", "C", "D", "E", "F"]
indice = 0

# Acumuladores y contadores
total_unidades = 0
agotados = 0
stock_bajo = 0

print("="*40)
print("       REPORTE DE INVENTARIO")
print("="*40)

while indice < len(productos):
    prod = productos[indice]
    cant = stock[indice]
    total_unidades += cant
    
    # 1. Mostramos la línea básica del producto
    print(f"Producto {prod}: {cant} unidades", end=" ")
    
    # 2. Agregamos las alertas visuales (Feedback)
    if cant == 0:
        print(" <--- [!] AGOTADO")
        agotados += 1
    elif cant <= 3:
        print(" <--- [!] STOCK BAJO")
        stock_bajo += 1
    else:
        print(" <--- [OK]") # Confirmamos que está bien
        
    # 3. El motor al final
    indice += 1

print("="*40)
print(f"RESUMEN FINAL:")
print(f"Total unidades en depósito: {total_unidades}")
print(f"Productos para reponer (0):  {agotados}")
print(f"Productos en alerta (1-3):   {stock_bajo}")
print("="*40)

lista_frutas = ["manzana", "banana", "cereza", "durazno"]

indice = 0

while indice < len(lista_frutas):
    
    mensaje=(f"==[elemento: {indice}] | fruta:[{lista_frutas[indice]}]")   
    indice +=1

print("=-------lista de frutas=-----")
print(f"{mensaje}")
print(f"{lista_frutas}")

lista_frutas = ["manzana", "banana", "cereza", "durazno"]
reporte_de_Frutas = ""
indice = 0

while indice < len(lista_frutas):
    
    frutas_renglon =f"==[elemento: {indice}] | fruta:[{lista_frutas[indice]}]"   
    indice +=1
    reporte_de_Frutas += frutas_renglon + "\n"

print(reporte_de_Frutas)
print(f"{lista_frutas}")
print("=-------lista de frutas=-----")

lista_frutas = ["manzana", "banana", "cereza", "durazno"]
reporte_acumulado = ""  # Empezamos con un texto vacío
indice = 0

while indice < len(lista_frutas):
    # Creamos el renglón actual
    renglon = f"==[elemento: {indice}] | fruta:[{lista_frutas[indice]}]"
    
    # Lo sumamos al reporte y agregamos un salto de línea (\n)
    reporte_acumulado += renglon + "\n"
    
    indice += 1

print("=------- REPORTE FINAL ACUMULADO -------=")
# Imprimimos la variable que guardó TODOS los renglones
print(reporte_acumulado)

print("Lista original:")
print(lista_frutas)
lista_frutas = ["manzana", "banana", "cereza", "durazno"]
reporte_de_Frutas_acumulado = ""
indice = 0

while indice < len(lista_frutas):
    
    frutas_por_renglon =f"==[elemento: {indice}] | fruta:[{lista_frutas[indice]}]"   
    indice +=1
    reporte_de_Frutas_acumulado += frutas_por_renglon + "\n"

    
print(reporte_de_Frutas_acumulado)
print("=-------lista de frutas=-----")
print(f"{lista_frutas}")

emails = ["ana@gmail.com", "correo_sin_arroba.com", "luis@hotmail.com", "maria@", "pedro@yahoo.com", "@dominio.com", "con espacio@gmail.com"]
indice = 0

emails_Validos = []
emails_Invalidos = []

while indice < len(emails):
    email = emails[indice]
    
    # --- FILTROS DE INVALIDEZ ---
    
    # 1. ¿Tiene espacios?
    if " " in email:
        emails_Invalidos.append(email)
        indice += 1
        continue # Salta al siguiente email
        
    # 2. ¿Empieza o termina con @?
    if email.startswith('@') or email.endswith('@'):
        emails_Invalidos.append(email)
        indice += 1
        continue
        
    # 3. ¿Tiene exactamente UN arroba? (Debe ser diferente a 1 para ser error)
    if email.count('@') != 1:
        emails_Invalidos.append(email)
        indice += 1
        continue
        
    # 4. ¿Tiene al menos un punto?
    if "." not in email:
        emails_Invalidos.append(email)
        indice += 1
        continue

    # --- SI PASÓ TODOS LOS FILTROS, ES VÁLIDO ---
    emails_Validos.append(email)
    indice += 1

print("=== REPORTE DE EMAILS ===")
print(f"VÁLIDOS: {emails_Validos}")
print(f"INVÁLIDOS: {emails_Invalidos}")


emails = ["ana@gmail.com", "correo_sin_arroba.com", "luis@hotmail.com", "maria@", "pedro@yahoo.com", "@dominio.com"]
indice = 0

emails_Validos = []
emails_Invalidos = []

print("="*50)
print("       SISTEMA DE VALIDACIÓN DE EMAILS")
print("="*50)

while indice < len(emails):
    email = emails[indice]
    
    # Imprimimos la primera parte sin saltar de línea
    print(f"Analizando: {email:<25}", end=" ")
    
    # Variable para saber si encontramos un error
    error_detectado = False
    motivo = ""

    # --- FILTROS DE SEGURIDAD ---
    if " " in email:
        error_detectado = True
        motivo = "[ESPACIOS]"
    elif email.startswith('@') or email.endswith('@'):
        error_detectado = True
        motivo = "[POSICIÓN @]"
    elif email.count('@') != 1:
        error_detectado = True
        motivo = "[FALTA/SOBRA @]"
    elif "." not in email:
        error_detectado = True
        motivo = "[FALTA PUNTO]"

    # --- RESULTADO DEL ANÁLISIS ---
    if error_detectado:
        print(f"| ESTADO: ❌ INVÁLIDO {motivo}")
        emails_Invalidos.append(email)
    else:
        print("| ESTADO: ✅ VÁLIDO")
        emails_Validos.append(email)

    indice += 1

print("="*50)
print(f"RESUMEN FINAL:")
print(f"Total Válidos: {len(emails_Validos)} -> {emails_Validos}")
print(f"Total Inválidos: {len(emails_Invalidos)} -> {emails_Invalidos}")
print("="*50)


# Variables iniciales
deposito_Acumulado = 0
contador_de_Depositos = 0
mensajeInvalido = " | ESTADO: ❌ Ingreso no válido. Debe ser un número positivo." 

print("="*50)
print("           SISTEMA DE AHORRO INTELIGENTE")
print("="*50)

# FILTRO INICIAL: Objetivo de ahorro
while True:
    ahorro_input = input("\n¿Cuál es tu objetivo de ahorro final?: $")
    if ahorro_input.isdigit() and int(ahorro_input) > 0:
        ahorro = int(ahorro_input)
        break
    print(mensajeInvalido)

print(f"\nPerfecto. Tu meta es llegar a: ${ahorro}")
print("-" * 50)

# BUCLE PRINCIPAL DE DEPÓSITOS
while True:
    deposito_raw = input(f"Ingresá dinero para tu depósito N°{contador_de_Depositos + 1}: $")
    
    # Validación de entrada
    if not deposito_raw.isdigit():
        print(mensajeInvalido)
        continue
    
    deposito_actual = int(deposito_raw)
    
    if deposito_actual <= 0:
        print(" | ESTADO: ❌ El depósito debe ser mayor a $0.")
        continue

    # Procesamiento de datos
    deposito_Acumulado += deposito_actual
    contador_de_Depositos += 1
    faltante = ahorro - deposito_Acumulado

    # Verificación de meta
    if deposito_Acumulado >= ahorro:
        print("\n" + "⭐" * 40)
        print("¡OBJETIVO ALCANZADO! ✅")
        print(f"Total ahorrado: ${deposito_Acumulado}")
        print(f"Cantidad de depósitos realizados: {contador_de_Depositos}")
        print("⭐" * 40)
        break
    else:
        print(f" -> OK. Depositaste: ${deposito_actual}")
        print(f" -> Te faltan: ${faltante}")
        print("-" * 40)

deposito_Acumulado = 0
contador_de_Depositos = 0
ahorro = 0  # Empezamos en 0 para saber que todavía no se cargó

print("="*50)
print("=== OBJETIVO DE AHORRO ===")
print("="*50)

while True:
    # 1. Este bloque solo corre si el ahorro sigue en 0
    if ahorro == 0:
        ingreso = input("Ingresa la Cantidad que deseas Ahorrar: $")
        if ingreso.isdigit() and int(ingreso) > 0:
            ahorro = int(ingreso)
            print(f"Meta fijada en: ${ahorro}")
            print("-" * 30)
        else:
            print("❌ Error: Ingresá un objetivo válido (solo números).")
        continue # El continue vuelve al inicio del while para empezar con los depósitos

    # 2. Una vez que ahorro tiene valor, el bloque de arriba se saltea
    deposito_raw = input("Ingresa la cantidad a Depositar: $")
    
    if not deposito_raw.isdigit():
        print("❌ Ingreso no válido.")
        continue
    
    # 3. Procesamos el depósito
    deposito_actual = int(deposito_raw)
    deposito_Acumulado += deposito_actual
    contador_de_Depositos += 1
    
    if deposito_Acumulado >= ahorro:
        print(f"✅ ¡Objetivo alcanzado! Depósitos: {contador_de_Depositos}")
        break
    else:
        print(f"Te faltan: ${ahorro - deposito_Acumulado}")


 #otra forma del 9
 # --- Variables ---
deposito_Acumulado = 0
contador_de_Depositos = 0
ahorro_objetivo = 0

print("="*50)
print("=== OBJETIVO DE AHORRO (SIN WHILE TRUE) ===")
print("="*50)

# 1. Primero pedimos el objetivo (fuera del while principal)
# Usamos un while corto solo para validar este dato
while ahorro_objetivo <= 0:
    ingreso = input("Ingresa la Cantidad que Deseas Ahorrar: $")
    if ingreso.isdigit():
        ahorro_objetivo = int(ingreso)
        if ahorro_objetivo <= 0:
            print("❌ El objetivo debe ser mayor a 0.")
    else:
        print("❌ Por favor, ingresá solo números.")

# 2. BUCLE PRINCIPAL: "Mientras no llegue a la meta..."
while deposito_Acumulado < ahorro_objetivo:
    dinero = input(f"Depósito N°{contador_de_Depositos + 1}: $")
    
    if dinero.isdigit() and int(dinero) > 0:
        deposito_actual = int(dinero)
        deposito_Acumulado += deposito_actual
        contador_de_Depositos += 1
        
        # Solo mostramos lo que falta si todavía no llegamos
        if deposito_Acumulado < ahorro_objetivo:
            falta = ahorro_objetivo - deposito_Acumulado
            print(f"-> Te faltan: ${falta}")
    else:
        print("❌ Depósito no válido.")

# 3. Al salir del while, ya sabemos que llegamos o superamos
print("\n" + "⭐" * 30)
print("¡OBJETIVO ALCANZADO! ✅")
print(f"Total ahorrado: ${deposito_Acumulado}")
print(f"Depósitos realizados: {contador_de_Depositos}")
print("⭐" * 30)
 # ver 

lista_de_Puntajes = [450, 900, 1200, 300, 750, 1200, 100]

# Inicialización
puntaje_Maximo = lista_de_Puntajes[0]
puntaje_Minimo = lista_de_Puntajes[0]
suma_de_Puntajes = 0
lista_de_Puntajes_Mayor_a_800 = []
indice = 0

# --- PROCESAMIENTO ---
while indice < len(lista_de_Puntajes):
    actual = lista_de_Puntajes[indice]
    
    # Buscar Máximo y Mínimo
    if actual > puntaje_Maximo:
        puntaje_Maximo = actual
    if actual < puntaje_Minimo:
        puntaje_Minimo = actual

    # Filtro de niveles altos
    if actual >= 800:
        lista_de_Puntajes_Mayor_a_800.append(actual)
    
    suma_de_Puntajes += actual
    indice += 1

# --- CÁLCULOS FINALES ---
promedio = suma_de_Puntajes / len(lista_de_Puntajes)
# Contamos cuántas veces aparece el máximo de forma precisa
cantidad_maximos = lista_de_Puntajes.count(puntaje_Maximo)

# --- REPORTE VISUAL PROFESIONAL ---
print("="*50)
print("       ANÁLISIS DE RENDIMIENTO - SISTEMA PRO")
print("="*50)
print(f"📊 Puntaje Más Alto:    {puntaje_Maximo} (Aparece {cantidad_maximos} veces)")
print(f"📉 Puntaje Más Bajo:    {puntaje_Minimo}")
print(f"⚖️  Promedio General:   {promedio:.2f}")
print(f"🚀 Puntajes Top (>=800): {len(lista_de_Puntajes_Mayor_a_800)}")
print("-" * 50)
print(f"Detalle de Puntajes Top: {lista_de_Puntajes_Mayor_a_800}")
print("="*50)



lista_colores = ["rojo", "azul", "verde", "amarillo"]
indice = 0
encontrado = False

print("=== BUSCADOR DE COLORES ===")

# 1. PEDIMOS EL COLOR AFUERA (Una sola vez)
while True:
    busqueda = input("Ingrese el color a buscar: ").strip().lower()
    if busqueda != "" and busqueda.isalpha():
        break # Dato válido, salimos a buscar
    print("❌ Error: Debes ingresar un nombre de color válido.")

# 2. RECORREMOS LA LISTA
while indice < len(lista_colores):
    color_actual = lista_colores[indice]
    
    if color_actual == busqueda:
        encontrado = True
        break # Si lo encontramos, no hace falta seguir mirando
    
    indice += 1

# 3. RESULTADO FINAL (Afuera del bucle)
if encontrado:
    print(f"✅ ¡Éxito! El color '{busqueda}' está en la lista.")
else:
    print(f"❌ El color '{busqueda}' no se encuentra.")

    # Ejemplo 13: Mostrar solo elementos pares
print("Ejemplo 13: Mostrar solo elementos pares de una lista")
print("-" * 70)

numeros = [5, 10, 15, 20, 25, 30, 35, 40]
indice = 0

print(f"Lista: {numeros}")
print("Números pares:")
print()

while indice < len(numeros):
    numero = numeros[indice]
    if numero % 2 == 0:
        print(f"  - {numero} (en posición {indice})")
    indice += 1

print()
"""
numeros = [10, -5, 3, -2, 8, 0]
total_positivos = 0
indice = 0

print("="*40)
print("   SUMADOR DE POSITIVOS (Modo Tester)")
print("="*40)

while indice < len(numeros):
    numero = numeros[indice]
    
    # 1. Primero aumentamos el índice para no trabarnos
    indice += 1

    # 2. Aplicamos la lógica de la consigna:
    # Si es menor o igual a cero, lo ignoramos y saltamos
    if numero <= 0:
        continue 

    # 3. Solo llegamos acá si el número es positivo
    total_positivos += numero
    print(f" -> Sumando positivo: {numero}")

print("-" * 40)
print(f"✅ La Suma Total de números POSITIVOS es: {total_positivos}")
print("="*40)