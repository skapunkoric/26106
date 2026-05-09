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


