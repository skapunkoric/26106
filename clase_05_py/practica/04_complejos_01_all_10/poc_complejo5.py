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
indice = 0
nombres_Validos =[]
nuevosDatosViejos = []
nuevosDatosTotales = []
while indice <len(datos):
    nuevosDatos= datos[indice].strip()
    nuevosDatosTotales.append(nuevosDatos)
    
    if nuevosDatos  != "":
      nombres_Validos.append(nuevosDatos)
    
    indice +=1
print("")
print("*" *60)
print(f"los datos ORGINALES son: \n{datos} ")
print("*" *60)
print(f"los datos originales con los strip aplicado CON ESPACIOS VACIOS; \n{nuevosDatosTotales} ")
print("*" *60)
print(f"los nuevos datos originales SIN ESPACIOS VACIOSson \n:{nombres_Validos} ")
print("*" *60)