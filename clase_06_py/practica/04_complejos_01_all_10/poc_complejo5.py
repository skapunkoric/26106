"""
Consigna:
Dada la lista datos = ["Ana", "", "Luis", "   ", "María", "Pedro", ""], crear una nueva lista solo con nombres válidos.

Requisitos:
- Recorrer la lista con while.
- Usar strip() para limpiar espacios.
- Si el dato queda vacío, ignorarlo usando continue.
- Agregar los nombres válidos a una lista nueva llamada nombres_validos.
- Mostrar la lista final.

Conceptos a practicar:
while, listas, append(), continue, limpieza de strings.
"""
datos = ["Ana", "", "Luis", "   ", "María", "Pedro", ""]
nombres_validos = []
for  dato in datos:
    dato = dato.strip()
    if dato != "":
        nombres_validos.append(dato)

print("*" *60)
print(f"los datos ORGINALES son: \n{datos} ")
print("*" *60)
print(f"los nuevos datos originales SIN ESPACIOS VACIOS;n{nombres_validos}")
print("*" *60)
print("\n" + "=" * 40)
print(f"{'indice':<10} |{'nombre_valido':<20}" )
for i, nombre_valido in enumerate(nombres_validos):
  print(f"{i:<10} |{nombre_valido:<20}" )
  print("")


