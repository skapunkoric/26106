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

nombre = ""
while nombre == "":
        nombre = input ("debes ingresar tu nombre: ").strip()
        if nombre == "":
            print(F"debes ingresar reingresar tu nombre: ")
        
print(f"-"*35)
print(f"Hola {nombre}")
print(f"-"*35) 

# ------------------------------------------------------------
# Ejercicio sencillo 4: Pedir nombre válido otra forma
# ------------------------------------------------------------

while True:
    nombre = input("Ingresá tu nombre: ").strip()
    if nombre != "" and nombre.isalpha():
        break 
    else:
        print("Error: El campo no puede estar vacío y solo puede contener letras .")
        
print("-" * 35)
print(f"Hola {nombre}") 
print("-" * 35)

    
       
              

