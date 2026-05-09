# ------------------------------------------------------------
# Ejercicio complejo 8: Validación de emails
# ------------------------------------------------------------
"""
Consigna:
Dada una lista de emails, separar los válidos de los inválidos.

emails = ["ana@gmail.com", "correo_sin_arroba.com", "luis@hotmail.com", "maria@", "pedro@yahoo.com", "@dominio.com"]

Un email será considerado válido si:
- Tiene exactamente un arroba.
- Contiene un punto.
- No empieza con arroba.
- No termina con arroba.
- No contiene espacios.

Requisitos:
- Recorrer la lista con while.
- Crear una lista emails_validos.
- Crear una lista emails_invalidos.
- Usar continue si querés evitar procesar emails inválidos.
- Mostrar ambas listas al final.

Conceptos a practicar:
while, listas, strings, condiciones compuestas, append().
"""
emails = ["ana@gmail.com", "correo_sin_arroba.com", "luis@hotmail.com", "maria@", "pedro@yahoo.com", "@dominio.com"]
indice =0
emails_Validos = []
emails_Invalidos = []
print("="*50)
print("Sistema De Validacion De Emails")
print("="*50)
while indice <len(emails):
    email_actual = emails[indice]
    
    print(f"Analizando: {email_actual:<25}", end=" ")
    
    error_detectado = False
    motivo = ""
    
    if " " in email_actual:
        error_detectado = True
        motivo = "[ESPACIOS]"
 
    elif email_actual.startswith('@')  or email_actual.endswith('@'):
        error_detectado = True
        motivo = "[POSISCION @]"

    elif  email_actual.count('@') != 1:
        error_detectado = True
        motivo = "[FALTA/SOBRA @]"
    elif "." not in email_actual:
        error_detectado = True
        motivo = "[FALTA PUNTO (.)]"
    
    if error_detectado:
        print(f"| ESTADO: ❌ INVÁLIDO {motivo}")
        emails_Invalidos.append(email_actual)        

    else:
        print("| ESTADO: ✅ VÁLIDO")
        emails_Validos.append(email_actual)

    indice +=1
print("="*50)
print("RESUMEN FINAL ")
print(f"TOTAL VALIDOS: {len(emails_Validos)}, ->{emails_Validos}") 
print(F"TOTAL INVALIDOS:{len,emails_Invalidos}, -> {emails_Invalidos}") 

