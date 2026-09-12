
# ------------------------------------------------------------
# Ejercicio sencillo 9: Cortar búsqueda con break
# ------------------------------------------------------------
"""
Consigna:
Dada la lista claves = ["abc", "123", "python", "admin"], buscar la clave "python".

Requisitos:
- Usar while.
- Cuando se encuentre "python", mostrar "Clave encontrada".
- Usar break para detener el bucle inmediatamente.
"""


claves = ["abc", "123", "python", "admin"]


for clave in claves:
    if  "python" ==clave:
      print(" clave ✅ encontrada")

#EN FORMA IF SI ESTA LA LISTA
if "python" in claves:
  print(" clave ✅ encontrada")
else:
  print(" clave NO encontrada") 

