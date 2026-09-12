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

print("=" * 45)
print(f"| {'ÍNDICE':<8} | {'NÚMERO':<10} | {'PROPIEDAD':<15} |")
print("=" * 45)

# Desempaquetamos el índice (i) y el valor (numero)
for i, numero in enumerate(lista_Numeros):

    # Lógica rápida para auditar si el número es par o impar
    if numero % 2 == 0:
        tipo = "🔹 PAR"
    else:
        tipo = "🔸 IMPAR"

    # Formateo con anchos fijos de columna: 8, 10 y 15 espacios
    print(f"| Pos [{i}]  | {numero:<10} | {tipo:<15} |")

print("=" * 45)
print(f" Cantidad de registros auditados: {len(lista_Numeros)}")
print("=" * 45)
    

