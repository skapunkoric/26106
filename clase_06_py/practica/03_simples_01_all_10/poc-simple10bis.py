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
    if numero <= 0:
      continue
    numero_positivo.append(numero)
suma_positivo= sum(numero_positivo)

print("-" * 40)            
print(f"La Suma Total DE NUMEROS Positivos es: -> {suma_positivo}")
print("-" * 40)
# otra forma
numeros = [10, -5, 3, -2, 8, 0]
numero_positivo = []
for numero in numeros:
    if numero > 0:
        numero_positivo.append(numero)
suma_positivo= sum(numero_positivo)

print("-" * 40)            
print(f"La Suma Total DE NUMEROS Positivos es: -> {suma_positivo}")
print("-" * 40)

