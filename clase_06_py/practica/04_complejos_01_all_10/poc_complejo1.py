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
max_intentos = 3
password_correcto = "python123"

for nro_intento in range(1, max_intentos +1):

    passwordIngresado = input(f"Intento {nro_intento} / {max_intentos} - Ingresa tu Contraseña: ").strip()

    if not passwordIngresado:
        print("⚠️ Error: El campo no puede estar vacío.")
        continue

    if passwordIngresado == password_correcto:
            print(f"Acceso permitido")
            break
    else:
        intentos_restantes = max_intentos - nro_intento

        if intentos_restantes > 0:
            print(f"❌ Password no válido. Te quedan {intentos_restantes} intentos.")
        else:
          print("🚫 Acceso bloqueado. Te quedaste sin intentos.")
        
    
        

    

