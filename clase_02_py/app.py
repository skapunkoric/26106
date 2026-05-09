"""
Clase 02 - Variables y E/S de datos
Archivo de apoyo con ejemplos y comentarios.

Basado en los temas de la clase:
- Variables
- Tipos de datos simples
- Operador de asignación
- Operadores aritméticos
- print() e input()
- Conversión de tipos
- Programas con entrada, procesamiento y salida

Importante:
Este archivo está pensado como material de lectura y práctica.
Podés ejecutar todo junto o ir probando bloque por bloque.
"""

# ==========================================================
# 1) VARIABLES
# ==========================================================

# Una variable es un espacio en memoria donde guardamos un dato.
# El signo = en Python NO significa "igual que" como en matemática,
# sino "asignar" un valor a una variable.

nombre = "Emi"
edad = 30
altura = 1.92
es_estudiante = True

print("VARIABLES BÁSICAS")
print("Nombre:", nombre)
print("Edad:", edad)
print("Altura:", altura)
print("¿Es estudiante?:", es_estudiante)
print("-" * 50)


# ==========================================================
# 2) TIPOS DE DATOS SIMPLES
# ==========================================================

# int    -> números enteros
# float  -> números con decimales
# str    -> texto
# bool   -> True o False

numero_entero = 10
numero_decimal = 3.14
texto = "Hola, Python"
booleano = False

print("TIPOS DE DATOS")
print(numero_entero, "es de tipo", type(numero_entero))
print(numero_decimal, "es de tipo", type(numero_decimal))
print(texto, "es de tipo", type(texto))
print(booleano, "es de tipo", type(booleano))
print("-" * 50)


# ==========================================================
# 3) FORMAS DE ASIGNACIÓN
# ==========================================================

# Asignación única
ciudad = "Buenos Aires"

# Asignación múltiple
x, y, z = 1, 2, 3

# Cambio de valor
contador = 0
contador = contador + 1   # También podría escribirse: contador += 1

print("FORMAS DE ASIGNACIÓN")
print("Ciudad:", ciudad)
print("x =", x, "| y =", y, "| z =", z)
print("Contador después de incrementarlo:", contador)
print("-" * 50)


# ==========================================================
# 4) BUENAS PRÁCTICAS CON NOMBRES DE VARIABLES
# ==========================================================

# Correcto: nombres descriptivos y en snake_case
nombre_completo = "Ana Pérez"
correo_electronico = "ana@email.com"
cantidad_productos = 5

# Evitar nombres poco descriptivos como:
# a = "Ana"
# b = "ana@email.com"
# c = 5

print("BUENAS PRÁCTICAS")
print("Nombre completo:", nombre_completo)
print("Correo electrónico:", correo_electronico)
print("Cantidad de productos:", cantidad_productos)
print("-" * 50)


# ==========================================================
# 5) FUNCIÓN print()
# ==========================================================

# print() sirve para mostrar información en pantalla.

print("FUNCIÓN print()")
print("Hola", "mundo")
print("Nombre:", nombre, "Edad:", edad)

# También podemos usar caracteres especiales:
print("\nEJEMPLOS CON CARACTERES ESPECIALES")
print("Hola\nMundo")  # salto de línea
print("Nombre:\tJuan")  # tabulación
print("Edad:\t30")

# end evita el salto de línea automático al final
print("Hola,", end=" ")
print("mundo")
print("-" * 50)


# ==========================================================
# 6) FUNCIÓN input()
# ==========================================================

# input() permite pedir datos al usuario.
# IMPORTANTE: lo que input() devuelve siempre es texto (str).

print("FUNCIÓN input()")
print("Descomentá las líneas siguientes para probar input manualmente:")

# nombre_usuario = input("Ingresá tu nombre: ")
# print("Hola,", nombre_usuario)

# edad_usuario = input("Ingresá tu edad: ")
# print("Tu edad es:", edad_usuario)
# print("El tipo de dato de edad_usuario es:", type(edad_usuario))

# print("En este archivo, las líneas de input están comentadas para que no frenen la ejecución automática.")
# print("-" * 50)


# ==========================================================
# 7) FUNCIÓN type()
# ==========================================================

# type() nos dice qué tipo de dato tiene una variable o valor.

print("FUNCIÓN type()")
print(type(10))
print(type(3.14))
print(type("Hola"))
print(type(True))
print("-" * 50)


# ==========================================================
# 8) CONVERSIÓN DE TIPOS
# ==========================================================

print("CONVERSIÓN DE TIPOS")

# De int a float
numero1 = 10
numero1_float = float(numero1)
print("int a float:", numero1, "->", numero1_float, "|", type(numero1_float))

# De float a int
numero2 = 8.99
numero2_int = int(numero2)
print("float a int:", numero2, "->", numero2_int, "|", type(numero2_int))

# De int a str
numero3 = 25
numero3_str = str(numero3)
print("int a str:", numero3, "->", numero3_str, "|", type(numero3_str))

# De str a int
numero4 = "123"
numero4_int = int(numero4)
print("str a int:", numero4, "->", numero4_int, "|", type(numero4_int))

# De bool a int
valor_logico = True
valor_logico_int = int(valor_logico)
print("bool a int:", valor_logico, "->", valor_logico_int)

# De int a bool
print("0 convertido a bool:", bool(0))
print("7 convertido a bool:", bool(7))
print("-" * 50)


# ==========================================================
# 9) OPERADORES ARITMÉTICOS
# ==========================================================

print("OPERADORES ARITMÉTICOS")

a = 10
b = 3

print("a =", a, "| b =", b)
print("Suma:", a + b)              # +
print("Resta:", a - b)             # -
print("Multiplicación:", a * b)    # *
print("División:", a / b)          # /
print("Módulo:", a % b)            # %
print("Exponenciación:", a ** b)   # **
print("División entera:", a // b)  # //
print("-" * 50)


# ==========================================================
# 10) PROGRAMAS CON ENTRADA, PROCESAMIENTO Y SALIDA
# ==========================================================

# Todo programa suele tener 3 partes:
# 1. Entrada de datos
# 2. Procesamiento
# 3. Salida de información

print("ENTRADA - PROCESAMIENTO - SALIDA")

# Ejemplo simple sin input para que se ejecute directo:
precio = 1500
cantidad = 4
total = precio * cantidad

print("Precio unitario:", precio)
print("Cantidad:", cantidad)
print("Total a pagar:", total)
print("-" * 50)
