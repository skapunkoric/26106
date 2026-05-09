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