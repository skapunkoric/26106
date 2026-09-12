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
for intento in range (1000):
    nombre = input ("debes ingresar tu nombre: ").strip()
    if nombre != "":
       break
    else:
        print(f"(Intento {intento + 1}) El nombre no puede estar vacío. ¡Escribí algo!")

        
print(f"-"*35)
print(f"Hola {nombre}")
print(f"-"*35) 

