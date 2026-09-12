# ------------------------------------------------------------
# Ejercicio sencillo 3: Mostrar números pares
# ------------------------------------------------------------
"""""
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

# nivel pro
# Así lo haría un "Pythonic Coder"
numeros_pares = [num for num in range(2, 22, 2)]

print(f"Lista de números pares: {numeros_pares}")


    