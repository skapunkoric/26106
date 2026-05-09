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
intentos = 0
password_correcto = "python123"

while intentos < max_intentos:
    passwordIngresado = input("Ingresá tu contraseña: ")
    intentos +=1    
    
    if passwordIngresado == password_correcto:
            print(f"Acceso permitido")
            break
    else: 
        intentos_restantes = max_intentos - intentos
            
        if intentos_restantes>0:
            print(f"password no valido. Te quedan {intentos_restantes} intentos ")

        else:    
            print(f"Acceso bloqueado te quedaste sin intentos")
        
    
        

    

