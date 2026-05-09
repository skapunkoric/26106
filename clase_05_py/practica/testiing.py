intentos = 0
max_intentos = 3
password_correcta = "python123"

while intentos < max_intentos:
    # Usamos f-string para mostrar cuántos intentos van
    password_ingresada = input(f"Intento {intentos + 1}: Ingresá tu contraseña: ")
    intentos += 1

    if password_ingresada == password_correcta:
        print("Acceso permitido.")
        intentos = 0 # Opcional: reseteamos para que no entre al mensaje de bloqueo
        break
    
    # Si no es la clave, avisamos cuántos quedan
    if intentos < max_intentos:
        print(f"Clave incorrecta. Te quedan {max_intentos - intentos} intentos.")
    else:
        print("Acceso bloqueado.")