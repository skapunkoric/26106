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
contador = 1
while contador <=3:

  while True:
  password = "python123"
  passwordIngresado = input("Ingresá tu contraseña: ")
  if password=passwordIngresado:
    print(f""Acceso permitido"")
    break

else:
        print(f"Este es el intento número {contador}.")
  
   contador += 1


while nombre == "":
   nombre = input("Ingresá tu nombre: ").strip()
   if nombre == "":
       print("El nombre no puede estar vacío. Intentá de nuevo.")

print(f"¡Hola, {nombre}! Gracias por ingresar tu nombre.")

numero = 0

while numero <= 5:
    print(f"este es le intento {numero}")

    numero = numero + 1




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

Conceptos a practicar:
listas paralelas, while, acumulador, contador, condicionales.
"""


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


# ============================================================
# FIN DEL ARCHIVO
# ============================================================
