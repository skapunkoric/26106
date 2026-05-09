# ------------------------------------------------------------
# Ejercicio complejo 4: Buscador de producto por código
# ------------------------------------------------------------
"""
Consigna:
Dadas dos listas relacionadas:

codigos = [101, 102, 103, 104]
productos = ["Teclado", "Mouse", "Monitor", "Auriculares"]

Crear un programa que pida un código al usuario y muestre el producto correspondiente.

Requisitos:
- Recorrer la lista codigos con while.+
- Si el código ingresado coincide con un código de la lista, mostrar el producto de la misma posición.+
- Usar break cuando se encuentre el producto.+
- Si no se encuentra, mostrar "Producto no encontrado".+
- Validar que el código ingresado sea numérico antes de convertirlo a int.+

Conceptos a practicar:
listas paralelas, índices, while, break, validación con isdigit().
"""
codigos = [101, 102, 103, 104]
productos = ["Teclado", "Mouse", "Monitor", "Auriculares"]
indice= 0
productoEncontrado = False


codigo_a_Buscar = input("ingrese codigo a buscar debe ser numerico: ")
if codigo_a_Buscar.isdigit():
    codigo_a_Buscar =int(codigo_a_Buscar)
    
    while indice < len(codigos) and indice <len(productos):
        
        if codigo_a_Buscar == codigos[indice]:
            productoEncontrado=True
            print(f"El producto encontrado es:{productos[indice]}")
            print(f"Con el Codigo Ingresado :{codigo_a_Buscar}")
            break
        indice += 1        
    if not productoEncontrado:
            print (f"Producto no encontrado: \n")            
else:
    print(f"codigo a INGRESAR debe ser numerico:")
            




        

    

