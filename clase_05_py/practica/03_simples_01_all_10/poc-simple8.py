# ------------------------------------------------------------
# Ejercicio sencillo 8: Buscar un color
# ------------------------------------------------------------
"""
Consigna:
Dada la lista colores = ["rojo", "azul", "verde", "amarillo"], buscar si existe el color "verde".

Requisitos:
- Usar while para recorrer la lista.
- Usar una variable encontrado con valor inicial False.
- Si se encuentra el color, cambiar encontrado a True.
- Al final, mostrar si el color fue encontrado o no.


# forma compleja

lista_colores = ["rojo", "azul", "verde", "amarillo"]
indice = 0
encontrado = False
    
while True:
      color_ingresado = input("ingrese el coloar a busar: ").strip().lower()
      if color_ingresado != "" and color_ingresado.isalpha():
            break
      print(" debes reingresar la busqueda de COLORES ")      
    
while indice < len(lista_colores):
      color_de_Lista = lista_colores[indice]

      if   color_de_Lista == color_ingresado:
            encontrado = True
            break
      
      indice += 1
      
if encontrado:
    print(f"el color,{color_ingresado} esta en la lista")
else:
    print(f"el color,{color_ingresado} NO  esta en la lista y no se encuentra")
         
             
"""

# forma simplicity


lista_colores = ["rojo", "azul", "verde", "amarillo"]
indice = 0
encontrado = False

while indice < len(lista_colores):
      color_de_Lista = lista_colores[indice]

      if   color_de_Lista == "verde":
            encontrado = True
            break
      
      indice += 1
      
if encontrado:
  print("el color ✅ VERDE esta en la lista")
else:
    print("el color BUSCADO NO ,esta en la lista y no se encuentra")