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
- Recorrer la lista codigos con while.
- Si el código ingresado coincide con un código de la lista, mostrar el producto de la misma posición.
- Usar break cuando se encuentre el producto.
- Si no se encuentra, mostrar "Producto no encontrado".
- Validar que el código ingresado sea numérico antes de convertirlo a int.
"""
codigos = [101, 102, 103, 104]
productos = ["Teclado", "Mouse", "Monitor", "Auriculares"]
producto_encontrado = False

def code_input(codigo_ingresado):
    if not str(codigo_ingresado).isdigit():
      return False, "\n[!] Error: El código debe ser un número entero."
       
    codigo_valido = int(codigo_ingresado)
   
    for cod, prod  in zip(codigos,productos):
        if cod == codigo_valido:    
           return True, prod
        
    return False, "Producto no Encontrado"   
def mostrar_resultado(codigo_buscado,exito,resultado):
        print("\n" + "=" * 45)
        print(f"{'🔎 SISTEMA DE BÚSQUEDA DE INVENTARIO':^45}")
        print("=" * 45)
        print(f"🔹 Código ingresado: '{codigo_buscado}'")
        print("-" * 45)
        if exito:
            print(f"✅ PRODUCTO ENCONTRADO: {resultado}")
        else:
            print(f"❌ FALLA EN BÚSQUEDA: {resultado}")
            print("=" * 45 + "\n")
  
# busqueda positiva
estado, mensaje = code_input(101)
mostrar_resultado(101,estado,mensaje)
# busqueda negativa
estado, mensaje = code_input(105)
mostrar_resultado(105,estado,mensaje)
