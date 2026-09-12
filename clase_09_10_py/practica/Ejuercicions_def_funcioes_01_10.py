# ------------------------------------------------------------
# Ejercicio complejo 1: Sistema de intentos de acceso
# ------------------------------------------------------------
"""
Consigna:
Crear un sistema de acceso que pida una contraseña hasta que el usuario escriba la correcta o agote 3 intentos.

Requisitos:
- La contraseña correcta debe ser "python123".
- Usar un contador de intentos.
- Permitir como máximo 3 intentos.
- Si la contraseña es correcta, mostrar "Acceso permitido" y terminar el bucle con break.
- Si se agotan los intentos, mostrar "Acceso bloqueado".
- El programa debe informar cuántos intentos quedan después de cada error.
"""
password_correcto = "python123"
max_intentos = 3


def ingreso_login():
    for nro_intento in range(1, max_intentos +1):
        passwordIngresado = input(f"Intento {nro_intento} / {max_intentos} - Ingresa tu Contraseña: ").strip()
        if not passwordIngresado:
            print("⚠️ Error: El campo no puede estar vacío.")
    
        elif passwordIngresado == password_correcto:
            return True , ("✅ Acceso permitido")
    
        intentos_restantes = max_intentos - nro_intento
    
        if intentos_restantes > 0:
            print(f"❌ Password no válido. Te quedan {intentos_restantes} intentos.")
    return False ,("🚫 Acceso bloqueado. Te quedaste sin intentos.")

estado , mensaje = ingreso_login()
print(mensaje)
print("=" *30)

# ------------------------------------------------------------
# Ejercicio complejo 2: Registro de gastos
# ------------------------------------------------------------
"""
Consigna:
Crear un programa que registre gastos hasta que el usuario escriba 0.

Requisitos:
- Pedir importes de gastos uno por uno.
- Si el usuario ingresa 0, terminar la carga.
- Si ingresa un número negativo, mostrar un error y volver a pedir el dato.
- Acumular el total de gastos válidos.
- Contar cuántos gastos válidos se ingresaron.
- Al final, mostrar:
  - Total gastado.
  - Cantidad de gastos cargados.
  - Promedio de gasto, solo si se cargó al menos un gasto.
"""
import re
from tabulate import tabulate

def registro_gastos():
    print("=== REGISTRO DE GASTOS CONTABLES ===")
    
    total_gastado = 0
    cantidad_gastos = 0
    
    while True:
    
        texto = input("💵 Ingresá el importe del gasto (0 para terminar): ").strip()
        
    
        if re.match(r"^-?\d+$", texto):
            gasto = int(texto)
            
    
            if gasto == 0:
                break
                
    
            elif gasto < 0:
                print("⚠️ Error: El importe no puede ser un número negativo. Volvé a intentar.")
                
    
            else:
                total_gastado += gasto
                cantidad_gastos += 1
                
        else:
            print("⚠️ Error: Por favor, ingresá solo números enteros válidos.")

    
    print("\n" + "="*40)
    print("📊 RESUMEN FINAL DE GASTOS")
    print("="*40)

    if cantidad_gastos > 0:
        promedio = total_gastado / cantidad_gastos
          
        
        lista_registro_promedio = [
            [f"💰 {total_gastado}", f"📋 {cantidad_gastos}", f"⚖️ {promedio:.2f}"]
        ]
        
        headers = ["Total Gastado", "Cantidad Gastos", "Promedio"]  
        print(tabulate(lista_registro_promedio, headers=headers, tablefmt="grid"))
    else:
        print("ℹ️ No se registraron gastos para procesar.")

registro_gastos()
# ------------------------------------------------------------
# Ejercicio complejo 3: Análisis de temperaturas
# ------------------------------------------------------------
"""
Consigna:
Dada la lista temperaturas = [22, 25, 19, 30, 28, 18, 24], analizar los datos usando while.

Requisitos:
- Recorrer la lista con un índice.
- Calcular la suma total de temperaturas.
- Calcular el promedio.
- Encontrar la temperatura más alta.
- Encontrar la temperatura más baja.
- Contar cuántas temperaturas fueron mayores o iguales a 25.
- Mostrar un resumen final.
"""
temperaturas = [22, 25, 19, 30, 28, 18, 24]

def calcular_estadisticas(temperaturas):
    """funcion que calcula promedio/suma/temp alta / temp baja / y temp mayor a 25"""
    suma = sum(temperaturas)
    maxima = max(temperaturas)
    minima = min(temperaturas)
    promedio = float (suma / len(temperaturas))
    contador_temperatura = 0
    for temperatura in temperaturas:
    
        if temperatura >= 25:
            contador_temperatura += 1
    return (suma, maxima, minima, promedio, contador_temperatura)


def mostrar_reporte(temperaturas,suma, maxima, minima, promedio, contador_temperatura):
        
        """funcion que muestra promedio/suma/temp alta / temp baja / y temp mayor a 25"""
        print("\n" + "=" * 30)
        print(f"{'Índice_Temp':<10} | {'Dato_Temp':<20}")
        print("-" * 30)
        for i, temp in enumerate(temperaturas):
            print(f"{i:<10} | {temp:<20}")
            print("=" * 30)
        print(f"total suma de temperaturas: {suma}°C")
        print(f"total promedio de temperaturas: {promedio:.2F}°C")
        print(f"total cantidad de temperaturas MAYOR A 25°C: {contador_temperatura}")
        print(f"total temperatura mas alta : {maxima}°C")
        print(f"total temperatura mas baja : {minima}°C")
        print("-" * 50)

suma_total, max_temp, min_temp, prom, calurosos = calcular_estadisticas(temperaturas)
mostrar_reporte(temperaturas, suma_total, max_temp, min_temp, prom, calurosos)

# ------------------------------------------------------------
# Ejercicio complejo 4: Buscador de producto por código
# ------------------------------------------------------------
"""
Consigna:
Dadas dos listas relacionadas:

codigos = [101, 102, 103, 104]
productos = ["Teclado", "Mouse", "Monitor", "Auriculares"]

Crear un programa que pida un código al usuario y muestre el producto correspondiente.

Requisitos:
- Recorrer la lista codigos con while.
- Si el código ingresado coincide con un código de la lista, mostrar el producto de la misma posición.
- Usar break cuando se encuentre el producto.
- Si no se encuentra, mostrar "Producto no encontrado".
- Validar que el código ingresado sea numérico antes de convertirlo a int.
"""
codigos = [101, 102, 103, 104]
productos = ["Teclado", "Mouse", "Monitor", "Auriculares"]
codigos = [101, 102, 103, 104]
productos = ["Teclado", "Mouse", "Monitor", "Auriculares"]
producto_encontrado = False

def code_input(codigo_ingresado):
    if not str(codigo_ingresado).isdigit():
      return False, "\n[!] Error: El código debe ser un número entero."
       
    codigo_valido = int(codigo_ingresado)
   
    for cod, prod  in zip(codigos,productos):
        if cod == codigo_valido:    
           return True, prod
        
    return False, "Producto no Encontrado"   
def mostrar_resultado(codigo_buscado,exito,resultado):
        print("\n" + "=" * 45)
        print(f"{'🔎 SISTEMA DE BÚSQUEDA DE INVENTARIO':^45}")
        print("=" * 45)
        print(f"🔹 Código ingresado: '{codigo_buscado}'")
        print("-" * 45)
        if exito:
            print(f"✅ PRODUCTO ENCONTRADO: {resultado}")
        else:
            print(f"❌ FALLA EN BÚSQUEDA: {resultado}")
            print("=" * 45 + "\n")
  
# busqueda positiva
estado, mensaje = code_input(101)
mostrar_resultado(101,estado,mensaje)
# busqueda negativa
estado, mensaje = code_input(105)
mostrar_resultado(105,estado,mensaje)


# ------------------------------------------------------------
# Ejercicio complejo 5: Limpieza de lista con continue
# ------------------------------------------------------------

"""
Consigna:
Dada la lista datos = ["Ana", "", "Luis", "   ", "María", "Pedro", ""], crear una nueva lista solo con nombres válidos.

Requisitos:
- Recorrer la lista con while.
- Usar strip() para limpiar espacios.
- Si el dato queda vacío, ignorarlo usando continue.
- Agregar los nombres válidos a una lista nueva llamada nombres_validos.
- Mostrar la lista final.
"""
def funcion1_limpia_nombre_vacios(dato):
    """
    recibe por parametro una lista de datos 
    recorre con un for de otra funcion
    y usa strip() para limpiar espacios.
    """
    dato_limpio = dato.strip()
    
    if dato_limpio != "":
        return dato_limpio
    else:
        return None

def funcion2_recorre_lista(lista_dato):

#recorre con un for una lista de datos y la recorre la lista 
    nombres_validos= []    
    for dato in lista_dato:
        resultado_lista =funcion1_limpia_nombre_vacios(dato)

        if resultado_lista is not None:
            nombres_validos.append(resultado_lista)
    return nombres_validos
         
def funcion3_mostrar_reporte_final(lista_datos,datos_nueva_lista):
    """muestra la lista en forma de funcion parametrizada"""
    print("*" * 60)
    print(f"Los datos ORIGINALES son: \n{lista_datos}")
    print("*" * 60)
    print(f"Los nuevos datos SIN ESPACIOS VACÍOS: \n{datos_nueva_lista}")
    print("*" * 60)
    print("\n" + "=" * 40)
    print(f"{'Índice':<10} | {'Nombre Válido':<20}")
    print("-" * 40)

    for i, nombre in enumerate(datos_nueva_lista):
        print(f"{i:<10} | {nombre:<20}")
    print("=" * 40)
    
lista_datos = ["Ana", "", "Luis", "   ", "María", "Pedro", ""]

lista_final = funcion2_recorre_lista(lista_datos)

funcion3_mostrar_reporte_final(lista_datos, lista_final)
# ------------------------------------------------------------
# Ejercicio complejo 6: Menú interactivo
# ------------------------------------------------------------
"""
Consigna:
Crear un menú que se repita hasta que el usuario elija salir.

Opciones:
1 - Saludar
2 - Mostrar los números del 1 al 5
3 - Mostrar una lista de cursos
4 - Salir

Requisitos:
- Usar while para mantener el menú activo.
- Si elige 1, mostrar un saludo.
- Si elige 2, usar otro while para mostrar los números del 1 al 5.
- Si elige 3, recorrer una lista de cursos con while.
- Si elige 4, mostrar "Programa finalizado" y terminar.
- Si elige otra opción, mostrar "Opción inválida".
"""
cursos = ["Introduccion a Python", "Java", "IA Inteligencia Artificial"]


def saludo():
    print("\n>>>>>>...Hola Bienvenido/a ......")
    input(f"\nPresioná Enter para volver al menú...")


def menu():
    print("\n==== Opciones: ====")
    print("*" * 30)
    print("1 - Saludar ")
    print("2 - Mostrar los números del 1 al 5")
    print("3 - Mostrar una lista de cursos")
    print("4 - Salir")
    print("*" * 30)


def mostra_numeros():
    lista_numerica = []
    for i in range(1, 6):
        lista_numerica.append(i)
    print("\n>>> Procesando números...")
    print(".........numeros del 1 al 5...........")
    print(f"La lista numerica es :{lista_numerica}")
    input(f"\nPresioná Enter para volver al menú...")


def lista_cursos():
    print(f"Los cursos disponibles son:{cursos}")
    input(f"\nPresioná Enter para volver al menú...")


def finally_program():
    print("\n..PROGRAMA Finalizado ....")


def error():
    print("\n[!] Opcion invalida. Elige una opción del 1 al 4.")
    input("\nPresioná Enter para volver al menú...")


def error_dos():
    print("\n[!] Error: Por favor, ingresa solo números.")
    print(".........OPCION INVALIDA ....")
    input(f"\nPresioná Enter para volver al menú...")


def validacion_menu():
    while True:
        menu()
        opcion = input("\nSelecione su opcion: ")

        if opcion.isdigit():
            opcion = int(opcion)
            match opcion:
                case 1:
                    saludo()  # lista

                case 2:
                    mostra_numeros()  # mostra numeros del 1 al 5

                case 3:
                    lista_cursos()  # mostra lista de cursos

                case 4:
                    finally_program()
                    break
                case _:
                    error()
        else:
            error_dos()


validacion_menu()


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
# flujo de trabajo
mostra_producto()
reporte()
  
# ------------------------------------------------------------
# Ejercicio complejo 8: Validación de emails
# ------------------------------------------------------------
""""
Consigna:
Dada una lista de emails, separar los válidos de los inválidos.

emails = ["ana@gmail.com", "correo_sin_arroba.com", "luis@hotmail.com", "maria@", "pedro@yahoo.com", "@dominio.com"]

Un email será considerado válido si:
- Tiene exactamente un arroba.
- Contiene un punto.
- No empieza con arroba.
- No termina con arroba.
- No contiene espacios.

Requisitos:
- Recorrer la lista con while.
- Crear una lista emails_validos.
- Crear una lista emails_invalidos.
- Usar continue si querés evitar procesar emails inválidos.
- Mostrar ambas listas al final.
"""
from itertools import zip_longest  # <--- Herramienta pro para emparejar listas de distinto largo

emails = ["ana@gmail.com", "correo_sin_arroba.com", "luis@hotmail.com", "maria@", "pedro@yahoo.com", "@dominio.com"]


def auditar_emails(emails):
    """"" --- PROCESAMIENTO (Tu lógica perfecta con elif) ---"""
    emails_Validos = []
    emails_Invalidos = []
    for email in emails:
    
        if " " in email:
            emails_Invalidos.append(email)
    
        elif email.startswith('@') or email.endswith('@'):
            emails_Invalidos.append(email)
    
        elif email.count('@') != 1:
            emails_Invalidos.append(email)
    
        elif "." not in email:
            emails_Invalidos.append(email)
    
        else:
            emails_Validos.append(email)
    
    
    return emails_Validos, emails_Invalidos

validos, invalidos = auditar_emails(emails)

# Mostramos por consola para verificar
""" modo testing
print(f"✅ Emails válidos aprobados: {validos}")
print(f"❌ Emails inválidos rechazados: {invalidos}")
"""
def mostra_emails(emails_Validos,emails_Invalidos):
    """--REPORTE EN COLUMNAS PRO---"""
    print("=" * 65)
    print(f"{'SISTEMA DE VALIDACIÓN DE EMAILS':^65}") # El :^65 centra el texto en 65 caracteres
    print("=" * 65)
    # Encabezados de las columnas (Ancho de 30 caracteres para cada lado + el separador)
    print(f"{'✅ CORREOS VÁLIDOS':<30} | {'❌ CORREOS INVÁLIDOS':<30}")
    print("-" * 65)
    # zip_longest junta fila por fila. Si una lista es más corta, pone un string vacío ""
    for valido, invalido in zip_longest(emails_Validos, emails_Invalidos, fillvalue=""):
        # El :<30 reserva exactamente 30 espacios alineados a la izquierda para cada celda
        print(f"{valido:<30} | {invalido:<30}")

    print("=" * 65)
    print(f"Totales | Válidos: {len(emails_Validos)} | Inválidos: {len(emails_Invalidos)}")
    print("=" * 65)
#procesa
validos, invalidos = auditar_emails(emails)
#muestra
mostra_emails(validos, invalidos)

# ------------------------------------------------------------
# Ejercicio complejo 9: Simulador de ahorro
# ------------------------------------------------------------
"""
Consigna:
Crear un programa que simule un objetivo de ahorro.

Requisitos:
- Pedir al usuario un objetivo de ahorro, por ejemplo 50000.
- Luego pedir depósitos uno por uno.
- No aceptar depósitos negativos ni vacíos.
- Acumular los depósitos válidos.
- Mostrar después de cada depósito cuánto falta para llegar al objetivo.
- Cuando el ahorro acumulado llegue o supere el objetivo, mostrar "Objetivo alcanzado".
- Mostrar cuántos depósitos válidos se realizaron.
"""
import re
from tabulate import tabulate


def pedir_numero(mensaje):
    numero_validado = 0
    while numero_validado == 0:
        texto = input(mensaje).strip()
        if re.match(r"^[1-9]\d*$", texto):
            numero_validado = int(texto)
        else:
            print("⚠️ Error: Por favor, ingresá un monto numérico entero y mayor a cero.")

    return numero_validado


def simulador_ahorro():
    ingreso_ahorro = pedir_numero("\n🎯 Ingresá tu meta total de ahorro: $")
    deposito_acumulado = 0
    nro_deposito = 1
    historial_depositos = []

    while deposito_acumulado < ingreso_ahorro:
        deposito_actual = pedir_numero(f"\n💸 Ingresá el monto a depositar #{nro_deposito}: $")
        deposito_acumulado += deposito_actual

        historial_depositos.append([nro_deposito, f"${deposito_actual}", f"${deposito_acumulado}"])

        faltante = ingreso_ahorro - deposito_acumulado

        if faltante > 0:
            print(f"Llevás ahorrado ${deposito_acumulado} (Te faltan ${faltante})")

        nro_deposito += 1

    print(f"\nTotal ahorrado: ${deposito_acumulado} (Tu meta era de ${ingreso_ahorro})")

    headers = ["Nro. Depósito", "Monto Ingresado", "Total Acumulado"]
    print("\n" + tabulate(historial_depositos, headers=headers, tablefmt="grid"))


simulador_ahorro()

# ------------------------------------------------------------
# Ejercicio complejo 10: Ranking de puntajes
# ------------------------------------------------------------
"""
Consigna:
Dada la lista puntajes = [450, 900, 1200, 300, 750, 1200, 100], analizar el ranking usando while.

Requisitos:
- Recorrer la lista con while.
- Encontrar el puntaje máximo.
- Encontrar el puntaje mínimo.
- Calcular el promedio de puntajes.
- Contar cuántos puntajes son mayores o iguales a 800.
- Contar cuántas veces aparece el puntaje máximo.
- Mostrar un resumen final con todos los datos.

Extra opcional:
- Crear una nueva lista llamada destacados con los puntajes mayores o iguales a 800.
"""
from tabulate import tabulate

lista_puntajes = [450, 900, 1200, 300, 750, 1200, 100]
lista_puntajes_mayor_a_800 = []


def ranking_puntajes():
    maximo = max(lista_puntajes)
    minimo = min(lista_puntajes)
    promedio_puntajes = sum(lista_puntajes) / len(lista_puntajes)
    lista_puntajes_mayor_a_800 = [p800 for p800 in lista_puntajes if p800 >= 800]
    repeticiones_max = lista_puntajes.count(maximo)

    # armar la grilla
    elementos_grilla = [
        [f"🥇 Max : {maximo}"],
        [f"🥉 Min : {minimo}"],
        [f"📊 ️Prom : {promedio_puntajes:.1f}"],
        [f"🥇 Tops800 : {len(lista_puntajes_mayor_a_800)}"],
        [f"🥇 TopsMax : {repeticiones_max}"],
        [f"🥇 lista800 : {lista_puntajes_mayor_a_800}"]
    ]
    headers = ["Métrica de Rendimiento", "Resultado Análisis"]
    # print("\\n" + tabulate(elementos_grilla, headers=headers, tablefmt="grid"))
    print(tabulate(elementos_grilla, headers=headers, tablefmt="grid"))


ranking_puntajes()
# ============================================================
# FIN DEL ARCHIVO
# ============================================================
