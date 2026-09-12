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
from itertools import zip_longest  # <--- Herramienta pro para emparejar listas de distinto largo

emails = ["ana@gmail.com", "correo_sin_arroba.com", "luis@hotmail.com", "maria@", "pedro@yahoo.com", "@dominio.com"]
emails_Validos = []
emails_Invalidos = []

# --- PROCESAMIENTO (Tu lógica perfecta con elif) ---
for email in emails:
    if " " in email:
        emails_Invalidos.append(email)
    elif email.startswith('@') or email.endswith('@'):
        emails_Invalidos.append(email)
    elif email.count('@') != 1:
        emails_Invalidos.append(email)
    elif "." not in email:
        emails_Invalidos.append(email)
    else:
        emails_Validos.append(email)

# --- REPORTE EN COLUMNAS PRO ---
print("=" * 65)
print(f"{'SISTEMA DE VALIDACIÓN DE EMAILS':^65}") # El :^65 centra el texto en 65 caracteres
print("=" * 65)

# Encabezados de las columnas (Ancho de 30 caracteres para cada lado + el separador)
print(f"{'✅ CORREOS VÁLIDOS':<30} | {'❌ CORREOS INVÁLIDOS':<30}")
print("-" * 65)

# zip_longest junta fila por fila. Si una lista es más corta, pone un string vacío ""
for valido, invalido in zip_longest(emails_Validos, emails_Invalidos, fillvalue=""):
    # El :<30 reserva exactamente 30 espacios alineados a la izquierda para cada celda
    print(f"{valido:<30} | {invalido:<30}")

print("=" * 65)
print(f"Totales | Válidos: {len(emails_Validos)} | Inválidos: {len(emails_Invalidos)}")
print("=" * 65)