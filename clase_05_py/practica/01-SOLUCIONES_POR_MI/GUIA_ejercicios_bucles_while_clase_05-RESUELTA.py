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
numero =1
while numero <= 10:
    print(f"numero: {numero}")
    numero += 1


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
contador_vuelta=10
while  contador_vuelta >= 1:
    print(f"Cuanta Regresiva N°: {contador_vuelta}")
    contador_vuelta -= 1
print(f"Despuegue")


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
numeroPar = 2
while numeroPar <=20:
    print(f"el numero par es: {numeroPar}")
    numeroPar+=2

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
while True:
    nombre = input("Ingresá tu nombre: ").strip()
    if nombre != "" and nombre.isalpha():
        break 
    else:
        print("Error: El campo no puede estar vacío y solo puede contener letras .")
        
print("-" * 35)
print(f"Hola {nombre}") 
print("-" * 35)

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
contador = 0
suma = 0
while contador <= 5:
    suma += contador
    contador +=1
print("-" * 45)
print("-------(0 + 1 + 2 + 3 + 4 + 5)--------")
print(f"la suma de los numeros (1 al 5) es total :[{suma}]")
print("-" * 45)
print("")

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
indice = 0

while indice < len(lista_frutas):
    print("")            
    print(f"==[elemento: {indice}] | fruta:[{lista_frutas[indice]}]")   
    indice +=1

print("=-------lista de frutas=-----")
print(f"{lista_frutas}")

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

reporte_de_Numeros = ""
indice = 0
lista_Numeros = [4, 8, 15, 16, 23, 42]
while indice < len(lista_Numeros):
    
    lista_de_Numeros_por_renglon =f"Posición {indice}: {lista_Numeros[indice]}"   
    indice +=1
    reporte_de_Numeros += lista_de_Numeros_por_renglon + "\n"

print(reporte_de_Numeros)

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
indice = 0
encontrado = False

while indice < len(lista_colores):
      color_de_Lista = lista_colores[indice]

      if   color_de_Lista == "verde":
            encontrado = True
            break
      
      indice += 1
      
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

indice = 0
while indice < len(claves):
    lista_actual_clave = claves[indice]

    if "python" == lista_actual_clave:
        print(" ✅ clave encontrada")
        break
    indice += 1

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
total_positivos = 0
indice = 0

while indice < len(numeros):
    numero = numeros[indice]
    indice += 1
    if numero <= 0:
        continue
    total_positivos += numero
    print(f" -> sumando positivos: {numero}")

print("-" * 40)            
print(f"La Suma Total DE NUMEROS Positivos es: -> {total_positivos}")
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
intentos = 0
password_correcto = "python123"

while intentos < max_intentos:
    passwordIngresado = input("Ingresá tu contraseña: ")
    intentos +=1    
    
    if passwordIngresado == password_correcto:
            print(f"Acceso permitido")
            break
    else: 
        intentos_restantes = max_intentos - intentos
            
        if intentos_restantes>0:
            print(f"password no valido. Te quedan {intentos_restantes} intentos ")

        else:    
            print(f"Acceso bloqueado te quedaste sin intentos")

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
acumulaGastos = 0.00
contadorGastos= 0
while True:
    gastoIngresado= input("Ingresá tus gastos (ó 0 para salir): ").strip().replace(",",".")
    if gastoIngresado.replace(".", "",1).isdigit():
        gastoReal= float(gastoIngresado)
        if gastoReal == 0:
         break
        elif  gastoReal>0:
            acumulaGastos +=gastoReal
            contadorGastos += 1     
            promedioDeGastos = acumulaGastos/contadorGastos
            #print(f"Total Cargado: ${acumulaGastos:.2f}")
            

                            
        else:
            print(f"error el gasto debe ser mayor a cerp")

    else:
        print(f"no es numero valido")       
print(f"---RESUMEN DE GASTOS-----")        
if contadorGastos>0:
     
     print(f"Total Gastado: ${acumulaGastos:.2f}")
     print(f"Cantidad de Gastos cargados: {contadorGastos}")
     print(f"Promedio de Gastos cargados: ${promedioDeGastos:.2f}")      
          
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
indice = 0
sumaTemperatura = 0
contadorTemperatura = 0
temperaturaMasAlta = temperaturas[0]
temperaturaMasBaja = temperaturas[0]
print() 
print("-" * 70)
print( " RESUMEN FINAL DE TEMPERATURAS " )
print("-" * 70)
print("lista de temperaturas con su corrrespondiente indice en la lista")
 
while indice<len(temperaturas):
    temperatura =  temperaturas[indice]
    print(f"indice: {indice} / temperatura: {temperaturas[indice]}°C") 
    sumaTemperatura += temperatura
    cantidadDeTemperaturas=len(temperaturas)
    indice += 1 
    if temperatura>=25:
        contadorTemperatura+= 1
    if  temperatura>temperaturaMasAlta:
          temperaturaMasAlta=temperatura
          
    if  temperatura<temperaturaMasBaja:
          temperaturaMasBaja=temperatura    
    
promedioDeTemperaturas = sumaTemperatura / cantidadDeTemperaturas    
print("-" * 70)
print(f"total suma de temperaturas: {sumaTemperatura}°C")
print(f"total promedio de temperaturas: {promedioDeTemperaturas:.2F}°C")
print(f"total cantidad de temperaturas MAYOR A 25°C: {contadorTemperatura}")
print(f"total temperatura mas alta : {temperaturaMasAlta}°C")
print(f"total temperatura mas baja : {temperaturaMasBaja}°C")
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
indice= 0
productoEncontrado = False
codigo_a_Buscar = input("ingrese codigo a buscar debe ser numerico: ")
if codigo_a_Buscar.isdigit():
    codigo_a_Buscar =int(codigo_a_Buscar)
    
    while indice < len(codigos) and indice <len(productos):
        
        if codigo_a_Buscar == codigos[indice]:
            productoEncontrado=True
            print(f"El producto encontrado es:{productos[indice]}")
            print(f"Con el Codigo Ingresado :{codigo_a_Buscar}")
            break
        indice += 1        
    if not productoEncontrado:
            print (f"Producto no encontrado: \n")            
else:
    print(f"codigo a INGRESAR debe ser numerico:")

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
indice = 0
nombres_Validos =[]
nuevosDatosViejos = []
nuevosDatosTotales = []
while indice <len(datos):
    nuevosDatos= datos[indice].strip()
    nuevosDatosTotales.append(nuevosDatos)
    
    if nuevosDatos  != "":
      nombres_Validos.append(nuevosDatos)
    
    indice +=1
print("")
print("*" *60)
print(f"los datos ORGINALES son: \n{datos} ")
print("*" *60)
print(f"los datos originales con los strip aplicado CON ESPACIOS VACIOS; \n{nuevosDatosTotales} ")
print("*" *60)
print(f"los nuevos datos originales SIN ESPACIOS VACIOSson \n:{nombres_Validos} ")
print("*" *60)


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
numero = 1
indice= 0
lista_Numerica =[]
while True:
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
                while numero <=5:
                    lista_Numerica.append(numero)
                    numero+=1
                print("\n>>> Procesando números...")
                print(".........numeros del 1 al 5...........")
                print(f"La lista numerica es :{lista_Numerica}")
                input(f"\nPresioná Enter para volver al menú...")

            case 3:
                while indice>len(cursos):
                    indice +=1          
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
stock = [5, 0, 12, 3, 0, 8]
productos = ["A", "B", "C", "D", "E", "F"]
indice = 0
cantidadDeStockTotal = 0
contador_de_Stock_en_cero = 0
contador_de_Stock_menor_q_3_y_mayor_q_0 = 0
print("=" * 33)
print("== REPORTE DE CONTROL DE STOCK ==")
print("=" * 33)
while indice <len(productos) and indice<len(stock):
    producto_actual = productos[indice]
    stock_actual = stock[indice]
     
    print(f"producto:{producto_actual}|Cantidad:{stock_actual}", end=" ")
    
    cantidadDeStockTotal += stock_actual
    
    if stock_actual == 0:
        print(">> Estado: [SIN STOCK]")
        contador_de_Stock_en_cero += 1
       
    elif stock_actual<= 3 and stock_actual >0: # no lo detecte pero no es rendundante esto lo detecto la IA  
        print(">> Estado: [STOCK BAJO]")
        contador_de_Stock_menor_q_3_y_mayor_q_0 += 1
    else:
      print(" <------- [OK]")
    indice +=1    
print("=" * 30)
print(f"calculo de unidades en stock:{cantidadDeStockTotal}")
print(f"Sin stock en (0):{contador_de_Stock_en_cero}")
print(f"Stock Bajo (con valor menor a 3): {contador_de_Stock_menor_q_3_y_mayor_q_0}")
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
emails = ["ana@gmail.com", "correo_sin_arroba.com", "luis@hotmail.com", "maria@", "pedro@yahoo.com", "@dominio.com"]
indice =0
reporte_de_Emails =""
emails_Validos = []
emails_Invalidos = []


while indice <len(emails):

    lista_emails = f"EMAIL:{emails[indice]}"
    reporte_de_Emails += lista_emails + "\n"
    email_actual = emails[indice]

    if " " in email_actual:
        emails_Invalidos.append(email_actual)
        indice +=1

        continue

    if email_actual.startswith('@')  or email_actual.endswith('@'):
        emails_Invalidos.append(email_actual)
        indice +=1

        continue
    
    if  email_actual.count('@') != 1:
        emails_Invalidos.append(email_actual)
        indice +=1

        continue
        
    if "." not in email_actual:
        emails_Invalidos.append(email_actual)
        indice +=1

        continue
    else:
        emails_Validos.append(email_actual)
        indice +=1
print("")
print(f"{reporte_de_Emails}")
print(f"INVALIDOS:" , emails_Invalidos) 
print(F"VALIDOS:", emails_Validos) 


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
deposito_Acumulado = 0
objetivo_alcanzado = False
deposito_de_Dinero = 0
contador_de_Depositos = 0
mensajeInvalido = " | ESTADO: ❌ Ingreso no valido" 
ahorro_ingresado = 0
print("="*50)
print ("=== OBJETIVO DE AHORRO ===")
print("="*50)
print("")

while True:
    if ahorro_ingresado == 0:
        ingreso_futuro_ahorro = input("Ingresa la Cantidad de DINERO que Deseas Ahorrar: $")
        if ingreso_futuro_ahorro.isdigit() and int(ingreso_futuro_ahorro) >0: 
           ahorro_ingresado = int(ingreso_futuro_ahorro)
        
        else:
            print(mensajeInvalido) 
        
        continue 
    
    dinero_a_Ingresar = input("Ingresa la cantidad de Dinero a Depositar: $") 
    
    if not dinero_a_Ingresar.isdigit():
        print(mensajeInvalido)  
        continue
    
    deposito_de_Dinero = int(dinero_a_Ingresar)
    deposito_Acumulado += deposito_de_Dinero
    resultado_de_Ahorro = (ahorro_ingresado - deposito_Acumulado)
    contador_de_Depositos += 1
    
    if  deposito_Acumulado >= ahorro_ingresado:
        objetivo_alcanzado = True
        print("Objetivo alcanzado" "✅") 
        break
     
    else:
        print(f"Te faltan: ${resultado_de_Ahorro}")
        print("-"*40)
        print(f"Ingresaste: {contador_de_Depositos} cant de Deposito/s Valido/os✅")
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
lista_de_Puntajes = [1200, 900, 450, 300, 750, 1200, 100]
puntaje_Maximo = lista_de_Puntajes[0]
puntaje_Minimo = lista_de_Puntajes[0]
contador_de_puntaje_maximo =0
suma_de_Puntajes =0
promedio_de_Puntajes = 0.0
contador_de_Mayor_a_800 = 0
lista_de_Puntajes_Mayor_a_800 = []
indice = 0

while indice < len(lista_de_Puntajes):
    lista_de_puntaje = lista_de_Puntajes[indice]
    
    if  lista_de_puntaje>puntaje_Maximo:
        puntaje_Maximo = lista_de_puntaje
        contador_de_puntaje_maximo = 1
    elif  lista_de_puntaje == puntaje_Maximo:
        contador_de_puntaje_maximo += 1
    
    
    if  lista_de_puntaje<puntaje_Minimo:
         puntaje_Minimo = lista_de_puntaje

    if  lista_de_puntaje>= 800:
        contador_de_Mayor_a_800 += 1
        lista_de_Puntajes_Mayor_a_800.append(lista_de_puntaje)
    
    
    suma_de_Puntajes += lista_de_puntaje
    promedio_de_Puntajes = suma_de_Puntajes / len(lista_de_Puntajes)
    

    indice += 1
print("")
print("="*50)
print("           REPORTE DE PUNTAJES ")
print("="*50)
print(f"La lista de puntajes son      {lista_de_Puntajes}")
print(f"Puntaje Mas Alto:             {puntaje_Maximo} y aparece : {contador_de_puntaje_maximo} veces") 
print(f"Puntaje Mas Bajo:             {puntaje_Minimo}") 
print(f"Promedio General de Puntajes: {promedio_de_Puntajes:.2f}")
print(f"PUNTAJES ARRIBA DE (>=800):   {contador_de_Mayor_a_800} cant")
print("="*50)    
print(" Detalle opcional nueva lista con puntajes TOP (>=800): ")
print (f"---------------------------->{lista_de_Puntajes_Mayor_a_800}")
print("")

# ============================================================
# FIN DEL ARCHIVO
# ============================================================
