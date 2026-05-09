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
reporte_de_Emails =""
emails_Validos = []
emails_Invalidos = []


while indice <len(emails):

    lista_emails = f"EMAIL:{emails[indice]}"
    reporte_de_Emails += lista_emails + "\n"
    email_actual = emails[indice]

    if " " in email_actual:
        emails_Invalidos.append(email_actual)
        indice +=1

        continue

    if email_actual.startswith('@')  or email_actual.endswith('@'):
        emails_Invalidos.append(email_actual)
        indice +=1

        continue
    
    if  email_actual.count('@') != 1:
        emails_Invalidos.append(email_actual)
        indice +=1

        continue
        
    if "." not in email_actual:
        emails_Invalidos.append(email_actual)
        indice +=1

        continue
    else:
        emails_Validos.append(email_actual)
        indice +=1
print("")
print(f"{reporte_de_Emails}")
print(f"INVALIDOS:" , emails_Invalidos) 
print(F"VALIDOS:", emails_Validos) 

