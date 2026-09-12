productos = []
opcion = 0

def mostrar_menu():

    print("\n" + "=" * 35)
    print("   SISTEMA DE GESTIÓN DE STOCK by Babul")
    print("=" * 35)
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")
    print("=" * 35)

def pedir_texto(mensaje,mensaje_error):
    dato = input(mensaje).strip()
    
    while dato == "":
        print(mensaje_error)
        dato = input(mensaje)
    return dato

def pedir_precio():
    precio_input = input("Ingrese el precio del producto (sin centavos): ").strip()
    while precio_input == "" or not precio_input.isdigit():
        print("El precio debe ser un número entero (puede ser 0).")
        precio_input = input("Ingrese el precio del producto (sin centavos): ").strip()
        return int(precio_input)        
    
def crear_producto():    
    nombre = pedir_texto("Ingrese el nombre del producto: ")
    categoria = pedir_texto("Ingrese la categoría del producto: ")
    precio = pedir_precio()
    # tupla 
    datos_extra = ("Disponible","Sin Descuento")
        
    producto = {
            "nombre": nombre,
            "categoria": categoria,
            "precio" : precio,
            "extra" : datos_extra
        }
    productos.append(producto)

while opcion != 5:
    mostrar_menu()
    
    entrada = input("Elegí una opción (1-5): ").strip()
    
    if entrada.isdigit() and entrada != "" and 1 <= int(entrada) <= 5:
        opcion = int(entrada)
    else:
        print("\n" + "!" * 45)
        print(" [!] ERROR: Opción inválida.")
        print(" Debe ingresar un número entero del 1 al 5.")
        print("!" * 45)
        input("\nPresioná Enter para volver al menú...")
        continue

    
    if opcion == 1:
        nombre = input("\nIngrese el nombre del producto: ").strip()
        
        #while nombre == "":
            #print("El nombre no puede estar vacío.")
            #nombre = input("Ingrese el nombre del producto: ").strip()

        #categoria = input("Ingrese la categoría del producto: ").strip()
        #while categoria == "":
            #print("La categoría no puede estar vacía.")
            #categoria = input("Ingrese la categoría del producto: ").strip()
            #producto = [nombre, categoria, precio]
        
        

        print("\n¡Producto agregado correctamente!")

        print(f"\n{'N°':<5} | {'NOMBRE':<20} | {'CATEGORÍA':<15} | {'PRECIO':<10}")
        print("-" * 60)
        print(f"{len(productos):<5} | {nombre:<20} | {categoria:<15} | ${precio:<10}")

        input("\nPresioná Enter para volver al menú anterior...")

    
    elif opcion == 2:
        if not productos:
            print("\n" + "*" * 45)
            print(" [!] SIN STOCK: No hay productos registrados.")
            print(" Use la Opción 1 para dar de alta un producto.")
            print("*" * 45)
        else:
            numero = 1
            print(f"\n{'N°':<5} | {'NOMBRE':<20} | {'CATEGORÍA':<15} | {'PRECIO':<10}")
            print("-" * 60)
            for prod in productos:
                print(f"{numero:<5} | {prod["nombre"]:<20} | {prod["categoria"]:<15} | ${prod["precio"]:<10}")
                numero += 1

        input("\nPresioná Enter para volver al menú anterior...")

    
    elif opcion == 3:
        if not productos:
            print("\n" + "*" * 45)
            print(" No se puede buscar si no hay productos cargados.")
            print("*" * 45)
        else:
            busqueda = input("\nIngresá el nombre del producto a buscar: ").strip()
            while busqueda == "":
                print("La búsqueda no puede estar vacía.")
                busqueda = input("Ingresá el nombre del producto a buscar: ").strip()

            encontrado = 0
            numero = 1

            print(f"\n{'N°':<5} | {'NOMBRE':<20} | {'CATEGORÍA':<15} | {'PRECIO':<10}")
            print("-" * 60)

            for prod in productos:
                if prod["nombre"].lower() == busqueda.lower():
                    print(f"{numero:<5} | {prod["nombre"]:<20} | {prod["categoria"]:<15} | ${prod["precio"]:<10}")
                    encontrado += 1
                numero += 1

            if encontrado == 0:
                print("No se encontraron productos con ese nombre.")

        input("\nPresioná Enter para volver al menú anterior...")

    
    elif opcion == 4:
        if not productos:
            print("\n" + "*" * 45)
            print(" [!] ALERTA: Base de datos vacía.")
            print(" No hay nada para eliminar en el sistema.")
            print("*" * 45)
        else:
            print("\nProductos registrados:")
            numero = 1
            for prod in productos:
                print(f"{numero:<5} | {prod["nombre"]:<20} | {prod["categoria"]:<15} | ${prod["precio"]:<10}")
                numero += 1

            posicion = input("\nIngrese el número del producto que querés eliminar: ").strip()
            while posicion == "" or not posicion.isdigit():
                print("Debes ingresar un número válido.")
                posicion = input("Ingrese el número del producto que querés eliminar: ").strip()

            posicion = int(posicion)

            if posicion < 1 or posicion > len(productos):
                print("[!] No existe producto con ese número.")
            else:
                eliminado = productos.pop(posicion - 1)
                print(f"\nProducto '{eliminado}' eliminado correctamente.")

        input("\nPresioná Enter para volver al menú anterior...")

    
    elif opcion == 5:
        print("\nGracias por usar el sistema de gestión. ¡Nos vemos, Vuelvas Pronto!")