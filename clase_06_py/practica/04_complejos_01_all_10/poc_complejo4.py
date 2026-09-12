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

producto_encontrado = False


codigo_a_buscar = input("ingrese codigo a buscar debe ser numerico: ")
if codigo_a_buscar.isdigit():
    codigo_a_buscar =int(codigo_a_buscar)

    print("\n" + "=" * 35)
    print(f"{'ID':<10} | {'DESCRIPCIÓN':<20}")
    print("-" * 35)
    
    for i, codigo in enumerate(codigos):
        if codigo == codigo_a_buscar:
            print(f"{codigo:<10} | {productos[i]:<20}")
            producto_encontrado=True
            print(f"El producto encontrado es:{productos[i]}")
            break

    if not producto_encontrado:
        print(f"{'ERROR':<10} | Código {codigo_a_buscar} no existe.")

        print("=" * 35)

else:
    print("\n[!] Error: El código debe ser un número entero.")
            




        

    

