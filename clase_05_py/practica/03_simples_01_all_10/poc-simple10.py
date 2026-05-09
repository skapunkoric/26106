
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

