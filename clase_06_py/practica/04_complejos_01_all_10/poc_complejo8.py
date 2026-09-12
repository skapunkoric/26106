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
emails_Validos = []
emails_Invalidos = []

print("="*50)
print("Sistema De Validacion De Emails")
print("="*50)

for email in emails:
    if " " in email:
        emails_Invalidos.append(email)
    
    elif email.startswith('@') or email.endswith('@'):
        emails_Invalidos.append(email)
    
    elif  email.count('@') != 1:
        emails_Invalidos.append(email)
        
    elif "." not in email:
        emails_Invalidos.append(email)
    else:
        emails_Validos.append(email)
        
print("")
print(f"INVALIDOS: ❌", emails_Invalidos) 
print(F"VALIDOS: ✅", emails_Validos) 

