"""
EJERCICIOS - CLASE 05: BUCLES WHILE
Talento Tech - Iniciación a la Programación con Python

Tema central:
- Bucles while
- Contadores
- Acumuladores
- break
- continue
- Listas
- Índices positivos y negativos
- Recorrido de listas con while

Instrucciones generales para estudiantes:
1. Resolver cada ejercicio debajo de su consigna.
2. Usar while cuando la consigna lo indique.
3. Evitar usar for.
4. Probar el código varias veces con distintos datos.
5. Cuidar que los bucles no sean infinitos.
"""

# ============================================================
# 10 EJERCICIOS SENCILLOS
# ============================================================

# ------------------------------------------------------------
# Ejercicio sencillo 1: Contar del 1 al 10
# ------------------------------------------------------------
"""
Consigna:
Crear un programa que muestre los números del 1 al 10 usando un bucle while.

Requisitos:
- Crear una variable contador que empiece en 1.
- Mientras el contador sea menor o igual a 10, mostrar su valor.
- Incrementar el contador en cada vuelta.

Salida esperada aproximada:
1
2
3
...
10
"""
for i  in range (1,11):
    print(i)


# ------------------------------------------------------------
# Ejercicio sencillo 2: Contar de 10 a 1
# ------------------------------------------------------------
"""
Consigna:
Crear un programa que muestre una cuenta regresiva desde 10 hasta 1 usando while.

Requisitos:
- Crear una variable contador que empiece en 10.
- Mostrar el valor del contador en cada vuelta.
- Restar 1 al contador en cada iteración.
- Al finalizar, mostrar el mensaje "Despegue".
"""
for  contador_vuelta in range (10, 0, -1):
    print(f"Cuanta Regresiva -->N°: {contador_vuelta}<---")

print(" 🚀 ----> Despegue: ")


# ------------------------------------------------------------
# Ejercicio sencillo 3: Mostrar números pares
# ------------------------------------------------------------
"""
Consigna:
Mostrar todos los números pares entre 2 y 20 usando while.

Requisitos:
- El programa debe comenzar en 2.
- Debe avanzar de 2 en 2.
- Debe mostrar solamente números pares.
"""
numeros_pares = []
for numero in range (2,22,2):
    numeros_pares.append(numero)
print(f"lista de numeros patres {numeros_pares}")

# ------------------------------------------------------------
# Ejercicio sencillo 4: Pedir nombre válido
# ------------------------------------------------------------
"""
Consigna:
Pedir al usuario su nombre hasta que escriba un valor no vacío.

Requisitos:
- Usar input().
- Usar strip() para quitar espacios al inicio y al final.
- Mientras el nombre esté vacío, volver a pedirlo.
- Cuando el nombre sea válido, mostrar un saludo.

Ejemplo:
Ingresá tu nombre: 
El nombre no puede estar vacío.
Ingresá tu nombre: Ana
Hola, Ana
"""
print("--- Iniciando experimento con FOR (No lo intenten en casa) ---")
for intento in range(1000):
    nombre = input("debes ingresar tu nombre: ").strip()
    if nombre != "":
        break
    else:
        print(f"(Intento {intento + 1}) El nombre no puede estar vacío. ¡Escribí algo!")

print(f"-" * 35)
print(f"Hola {nombre}")
print(f"-" * 35)

# ------------------------------------------------------------
# Ejercicio sencillo 5: Sumar números del 1 al 5
# ------------------------------------------------------------
"""
Consigna:
Calcular la suma de los números del 1 al 5 usando while.

Requisitos:
- Usar una variable contador.
- Usar una variable acumuladora llamada suma.
- Mostrar el total final.

Resultado esperado:
La suma total es 15
"""
numeros_1_al_5 = [num for num in range(1, 6,)]
resulado_suma = sum(numeros_1_al_5)
print(f"--------->{numeros_1_al_5}")
print(f"el resultado es: {resulado_suma}")


# ------------------------------------------------------------
# Ejercicio sencillo 6: Recorrer una lista de frutas
# ------------------------------------------------------------
"""
Consigna:
Dada la lista frutas = ["manzana", "banana", "cereza", "durazno"], mostrar cada fruta usando while.

Requisitos:
- Usar una variable indice que empiece en 0.
- Usar len(frutas) en la condición del while.
- Mostrar cada elemento accediendo con frutas[indice].
"""
lista_frutas = ["manzana", "banana", "cereza", "durazno"]
print("=" *30)
print("Reporte de frutas")
print("=" *30)
for i, fruta in enumerate (lista_frutas):
 print(f"|{i:02d}|Fruta:|-->{fruta.capitalize()}")

# ------------------------------------------------------------
# Ejercicio sencillo 7: Mostrar posición y valor
# ------------------------------------------------------------
"""
Consigna:
Dada la lista numeros = [4, 8, 15, 16, 23, 42], mostrar cada número junto con su posición.

Requisitos:
- Usar while.
- Mostrar el índice y el valor.

Salida esperada aproximada:
Posición 0: 4
Posición 1: 8
Posición 2: 15
"""

lista_Numeros = [4, 8, 15, 16, 23, 42]
for lista in enumerate (lista_Numeros):
    print(f"{lista}")  

# ------------------------------------------------------------
# Ejercicio sencillo 8: Buscar un color
# ------------------------------------------------------------
"""
Consigna:
Dada la lista colores = ["rojo", "azul", "verde", "amarillo"], buscar si existe el color "verde".

Requisitos:
- Usar while para recorrer la lista.
- Usar una variable encontrado con valor inicial False.
- Si se encuentra el color, cambiar encontrado a True.
- Al final, mostrar si el color fue encontrado o no.
"""
lista_colores = ["rojo", "azul", "verde", "amarillo"]
encontrado = False
for color in lista_colores:
      if color == "verde":
         encontrado = True

if encontrado:   
   print("el color ✅ VERDE esta en la lista")
else:
   print("el color BUSCADO NO ,esta en la lista y no se encuentra")

# ------------------------------------------------------------
# Ejercicio sencillo 9: Cortar búsqueda con break
# ------------------------------------------------------------
"""
Consigna:
Dada la lista claves = ["abc", "123", "python", "admin"], buscar la clave "python".

Requisitos:
- Usar while.
- Cuando se encuentre "python", mostrar "Clave encontrada".
- Usar break para detener el bucle inmediatamente.
"""
claves = ["abc", "123", "python", "admin"]
for clave in claves:
    if  "python" == clave:
      print(" clave ✅ encontrada")

# ------------------------------------------------------------
# Ejercicio sencillo 10: Sumar solo positivos
# ------------------------------------------------------------
"""
Consigna:
Dada la lista numeros = [10, -5, 3, -2, 8, 0], sumar solamente los números positivos.

Requisitos:
- Usar while para recorrer la lista.
- Ignorar los números negativos y el cero.
- Usar continue cuando el número no deba sumarse.
- Mostrar la suma final.
"""
numeros = [10, -5, 3, -2, 8, 0]
numero_positivo = []
for numero in numeros:
    if numero > 0:
        numero_positivo.append(numero)
suma_positivo= sum(numero_positivo)

print("-" * 40)            
print(f"La Suma Total DE NUMEROS Positivos es: -> {suma_positivo}")
print("-" * 40)



# ============================================================
# 10 EJERCICIOS COMPLEJOS
# ============================================================

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

Conceptos a practicar:
while, contador, break, validación de entrada.
"""
max_intentos = 3
password_correcto = "python123"

for nro_intento in range(1, max_intentos +1):

    passwordIngresado = input(f"Intento {nro_intento} / {max_intentos} - Ingresa tu Contraseña: ").strip()

    if not passwordIngresado:
        print("⚠️ Error: El campo no puede estar vacío.")
        continue

    if passwordIngresado == password_correcto:
            print(f"Acceso permitido")
            break
    else:
        intentos_restantes = max_intentos - nro_intento

        if intentos_restantes > 0:
            print(f"❌ Password no válido. Te quedan {intentos_restantes} intentos.")
        else:
          print("🚫 Acceso bloqueado. Te quedaste sin intentos.")




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

Conceptos a practicar:
while, acumulador, contador, validaciones, break o condición centinela.
"""
import re
patron_estricto = r"^[0-9]+(\.[0-9]+)?$"
acumulaGastos = 0.0
contadorGastos= 0
print("📋 REGISTRO DE GASTOS tipo BILLETERA VIRTUAL")
print("-" * 40)

for i in range (100):

    gastoIngresado= input("Ingresá tus gastos (ó 0 para salir): ").strip()
    if re.match(patron_estricto,gastoIngresado):
        gastoReal= float(gastoIngresado)
        if gastoReal == 0:
         break
        acumulaGastos +=gastoReal
        contadorGastos += 1
        print(f"   ✅ Sumado: ${gastoReal:.2f}")

    else:
            print(f"error el gasto debe ser mayor a cerp")

print("\n" + "=" * 25)
print("     RESUMEN DE GASTOS")
print("=" * 25)

if contadorGastos>0:
     promedioDeGastos = acumulaGastos / contadorGastos
     print(f"Total Gastado: ${acumulaGastos:.2f}")
     print(f"Cantidad de Gastos cargados: {contadorGastos}")
     print(f"Promedio de Gastos cargados: ${promedioDeGastos:.2f}")
     print("-" * 25)
          
else:
    print(f"no cargaste nada, vuelve pronto")


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

Conceptos a practicar:
listas, índices, while, acumuladores, comparación de máximos y mínimos.
"""
temperaturas = [22, 25, 19, 30, 28, 18, 24]
contador_temperatura= 0

print() 
print("-" * 70)
print( " RESUMEN FINAL DE TEMPERATURAS " )
print("-" * 70)
print("lista de temperaturas con su corrrespondiente indice en la lista")
 
for temperatura in temperaturas:
    if temperatura >= 25:
        contador_temperatura += 1

    suma_temperaturas =sum(temperaturas)
    maxima_tmperatura =max(temperaturas)
    minima_tmperatura =min(temperaturas)
    promedio_de_temperaturas = suma_temperaturas / len(temperaturas)

print("-" * 70)
print(f"total suma de temperaturas: {suma_temperaturas}°C")
print(f"total promedio de temperaturas: {promedio_de_temperaturas:.2F}°C")
print(f"total cantidad de temperaturas MAYOR A 25°C: {contador_temperatura}")
print(f"total temperatura mas alta : {maxima_tmperatura}°C")
print(f"total temperatura mas baja : {minima_tmperatura}°C")
print("-" * 70)

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

Conceptos a practicar:
listas paralelas, índices, while, break, validación con isdigit().
"""
codigos = [101, 102, 103, 104]
productos = ["Teclado", "Mouse", "Monitor", "Auriculares"]

producto_encontrado = False


codigo_a_buscar = input("ingrese codigo a buscar debe ser numerico: ")
if codigo_a_buscar.isdigit():
    codigo_a_buscar =int(codigo_a_buscar)

    print("\n" + "=" * 35)
    print(f"{'ID':<10} | {'DESCRIPCIÓN':<20}")
    print("-" * 35)
    
    for i, codigo in enumerate(codigos):
        if codigo == codigo_a_buscar:
            print(f"{codigo:<10} | {productos[i]:<20}")
            producto_encontrado=True
            print(f"El producto encontrado es:{productos[i]}")
            break

    if not producto_encontrado:
        print(f"{'ERROR':<10} | Código {codigo_a_buscar} no existe.")

        print("=" * 35)

else:
    print("\n[!] Error: El código debe ser un número entero.")
            

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

Conceptos a practicar:
while, listas, append(), continue, limpieza de strings.
"""
datos = ["Ana", "", "Luis", "   ", "María", "Pedro", ""]
nombres_validos = []
for  dato in datos:
    dato = dato.strip()
    if dato != "":
        nombres_validos.append(dato)

print("*" *60)
print(f"los datos ORGINALES son: \n{datos} ")
print("*" *60)
print(f"los nuevos datos originales SIN ESPACIOS VACIOS;n{nombres_validos}")
print("*" *60)
print("\n" + "=" * 40)
print(f"{'indice':<10} |{'nombre_valido':<20}" )
for i, nombre_valido in enumerate(nombres_validos):
  print(f"{i:<10} |{nombre_valido:<20}" )
  print("")


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

Conceptos a practicar:
while, menú, condicionales, listas, bucles anidados simples.
"""
cursos=["Introduccion a Python","Java","IA Inteligencia Artificial"]
lista_numerica =[]

for _ in range (999999):
 
    print("\n==== Opciones: ====")
    print("*"*30)
    print("1 - Saludar ")
    print("2 - Mostrar los números del 1 al 5") 
    print("3 - Mostrar una lista de cursos")
    print ("4 - Salir")
    print("*"*30)
    opcion = input("\nSelecione su opcion: ")
 
    if opcion.isdigit():
        opcion = int(opcion)
        match opcion:
            case  1:
                print ("\n>>>>>>...Hola Bienvenido/a ......")
                input(f"\nPresioná Enter para volver al menú...")

            case 2:
                for i in range (1,6) :
                    lista_numerica.append(i)
                    
                print("\n>>> Procesando números...")
                print(".........numeros del 1 al 5...........")
                print(f"La lista numerica es :{lista_numerica}")
                input(f"\nPresioná Enter para volver al menú...")

            case 3:
                 print(f"Los cursos disponibles son:{cursos}")
                 input(f"\nPresioná Enter para volver al menú...")

            case 4:
                print ("\n..PROGRAMA Finalizado ....")             
                break
            
            case _:
                print("\n[!] Opcion invalida. Elige una opción del 1 al 4.")
                input("\nPresioná Enter para volver al menú...")
    else:
        print("\n[!] Error: Por favor, ingresa solo números.")
        print (".........OPCION INVALIDA ....")
        input(f"\nPresioná Enter para volver al menú...")

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
# ****Si el stock es menor o igual a 3 pero mayor que 0, mostrar "Stock bajo". <----------- VER ***###
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
   

# ------------------------------------------------------------
# Ejercicio complejo 8: Validación de emails
# ------------------------------------------------------------
"""
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

Conceptos a practicar:
while, listas, strings, condiciones compuestas, append().
"""
mails = ["ana@gmail.com", "correo_sin_arroba.com", "luis@hotmail.com", "maria@", "pedro@yahoo.com", "@dominio.com"]
emails_Validos = []
emails_Invalidos = []

print("="*50)
print("Sistema De Validacion De Emails")
print("="*50)

for email in emails:
    if " " in email:
        emails_Invalidos.append(email)
    
    elif email.startswith('@') or email.endswith('@'):
        emails_Invalidos.append(email)
    
    elif  email.count('@') != 1:
        emails_Invalidos.append(email)
        
    elif "." not in email:
        emails_Invalidos.append(email)
    else:
        emails_Validos.append(email)
        
print("")
print(f"INVALIDOS: ❌", emails_Invalidos) 
print(F"VALIDOS: ✅", emails_Validos) 

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

Conceptos a practicar:
while, acumulador, contador, validación, condición de corte.
"""
import re

deposito_acumulado = 0
contador_depositos = 0
mensaje_invalido = " | ESTADO: ❌ Ingreso no valido" 

print("="*50)
print ("=== OBJETIVO DE AHORRO ===")
print("="*50)
print("")
 
ingreso_futuro_ahorro = input("Ingresa la Cantidad de DINERO que Deseas Ahorrar: $")
if re.match(r"^[1-9][0-9]*$",ingreso_futuro_ahorro): 
    ahorro_ingresado = int(ingreso_futuro_ahorro)
    
    for dinero_a_ingresar in range (1000):    
        dinero_a_ingresar = input("Ingresa la cantidad de Dinero a Depositar: $") 
        
        if not re.match(r"^[1-9][0-9]*$",dinero_a_ingresar):
            print(mensaje_invalido)
            continue
            
        deposito_acumulado += int(dinero_a_ingresar)
        contador_depositos += 1
         

        if  deposito_acumulado >= ahorro_ingresado:
            print("Objetivo alcanzado" "✅")
            break
        
        
        resultado_ahorro = (ahorro_ingresado - deposito_acumulado)        

        if deposito_acumulado < ahorro_ingresado:
            print(f"Te faltan: ${resultado_ahorro}")
            print("-"*40)
            print(f"Ingresaste: {contador_depositos} cant de Deposito/s Valido/os✅")
            print("\nVolve a ingresar DINERO para tus deposito/os y cunplir tu Objetivo de Ahorro")  

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

Conceptos a practicar:
while, listas, índices, acumuladores, máximos, mínimos, contadores, append().
"""
lista_de_puntajes = [1200, 900, 450, 300, 750, 1200, 100]
lista_puntajes_mayor_a_800 = []

maximo = max(lista_de_puntajes)
minimo = min(lista_de_puntajes)
promedio_puntajes = sum(lista_de_puntajes) /len(lista_de_puntajes)
cantidad_maxima = lista_de_puntajes.count(maximo)
for puntaje in lista_de_puntajes:
    if puntaje >=800:
        lista_puntajes_mayor_a_800.append(puntaje)
cantidad_puntaje_800 = len(lista_puntajes_mayor_a_800)

print("")
print("="*50)
print("           REPORTE DE PUNTAJES ")
print("="*50)
print(f"La lista de puntajes son      {lista_de_puntajes}")
print(f"Puntaje Mas Alto:             {maximo} y aparece : {cantidad_maxima} veces") 
print(f"Puntaje Mas Bajo:             {minimo}") 
print(f"Promedio General de Puntajes: {promedio_puntajes:.2f}")
print(f"PUNTAJES ARRIBA DE (>=800):   {cantidad_puntaje_800} cant")
print("="*50)    
print(" Detalle opcional nueva lista con puntajes TOP (>=800): ")
print (f"---------------------------->{lista_puntajes_mayor_a_800}")
print("")


# ============================================================
# FIN DEL ARCHIVO
# ============================================================
