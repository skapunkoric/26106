"""
productos = []
opcion = 0  # Lo inicializamos como número entero

while opcion != 5:  # El bucle sale cuando opcion sea el entero 5
    print("\n--- MENÚ DE GESTIÓN ---")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")

    entrada = input("Elegí una opción (1-5): ").strip()

    # Validación de la opción del menú
    if entrada.isdigit() and entrada != "":
        opcion = int(entrada)
    else:
        print("Opción inválida. Elegí un número del 1 al 5.")
        continue  # Vuelve al inicio del while sin evaluar lo de abajo

    # --- OPCIÓN 1: AGREGAR ---
    if opcion == 1:
        nombre = input("Ingrese el nombre del producto: ").strip()
        while nombre == "":
            print("El nombre no puede estar vacío.")
            nombre = input("Ingrese el nombre del producto: ").strip()

        categoria = input("Ingrese la categoría del producto: ").strip()
        while categoria == "":
            print("La categoría no puede estar vacía.")
            categoria = input("Ingrese la categoría del producto: ").strip()

        precio_input = input("Ingrese el precio del producto, sin centavos: ").strip()
        while not precio_input.isdigit() or precio_input == "":
            print("El precio debe ser un número entero, sin centavos.")
            precio_input = input("Ingrese el precio del producto, sin centavos: ").strip()

        precio = int(precio_input)
        producto = [nombre, categoria, precio]
        productos.append(producto)
        print("¡Producto agregado correctamente!")

    # --- OPCIÓN 2: MOSTRAR ---
    elif opcion == 2:
        if not productos:  # Forma limpia de ver si la lista general está vacía
            print("No hay productos registrados.")
        else:
            numero = 1
            print(f"\n{'N°':<5} | {'NOMBRE':<20} | {'CATEGORÍA':<15} | {'PRECIO':<10}")
            print("-" * 60)
            for prod in productos:
                print(f"{numero:<5} | {prod[0]:<20} | {prod[1]:<15} | ${prod[2]:<10}")
                numero += 1

    # --- OPCIÓN 3: BUSCAR ---
    elif opcion == 3:
        if not productos:
            print("No hay productos registrados.")
        else:
            busqueda = input("Ingresá el nombre del producto a buscar: ").strip()
            while busqueda == "":
                print("La búsqueda no puede estar vacía.")
                busqueda = input("Ingresá el nombre del producto a buscar: ").strip()

            encontrado = 0
            numero = 1

            print(f"\n{'N°':<5} | {'NOMBRE':<20} | {'CATEGORÍA':<15} | {'PRECIO':<10}")
            print("-" * 60)

            for prod in productos:
                if prod[0].lower() == busqueda.lower():  # .lower() ayuda a que no importe mayúsculas/minúsculas
                    print(f"{numero:<5} | {prod[0]:<20} | {prod[1]:<15} | ${prod[2]:<10}")
                    encontrado += 1
                numero += 1

            if encontrado == 0:
                print("No se encontraron productos con ese nombre.")

    # --- OPCIÓN 4: ELIMINAR ---
    elif opcion == 4:
        if not productos:
            print("No hay productos registrados.")
        else:
            print("\nProductos registrados:")
            numero = 1  # Inicializamos para que no tire error
            for prod in productos:
                print(f"{numero} - {prod[0]} - {prod[1]} - ${prod[2]}")
                numero += 1

            posicion = input("Ingrese el número del producto que querés eliminar: ").strip()
            while posicion == "" or not posicion.isdigit():
                print("Debes ingresar un número válido.")
                posicion = input("Ingrese el número del producto que querés eliminar: ").strip()

            posicion = int(posicion)

            if posicion < 1 or posicion > len(productos):
                print("No existe producto con ese número.")
            else:
                eliminado = productos.pop(posicion - 1)
                print(f"Producto '{eliminado[0]}' eliminado correctamente.")

    # --- OPCIÓN 5: SALIR ---
    elif opcion == 5:
        print("Gracias por usar el sistema de gestión.")

productos = []
opcion = 0

while opcion != 5:
    print("\n" + "=" * 35)
    print("   SISTEMA DE GESTIÓN DE STOCK")
    print("=" * 35)
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")
    print("=" * 35)

    entrada = input("Elegí una opción (1-5): ").strip()

    if entrada.isdigit() and entrada != "":
        opcion = int(entrada)
    else:
        print("\n[!] Opción inválida. Elegí un número del 1 al 5.")
        input("\nPresioná Enter para volver al menú...")
        continue

        # --- OPCIÓN 1: AGREGAR ---
    if opcion == 1:
        nombre = input("\nIngrese el nombre del producto: ").strip()
        while nombre == "":
            print("El nombre no puede estar vacío.")
            nombre = input("Ingrese el nombre del producto: ").strip()

        categoria = input("Ingrese la categoría del producto: ").strip()
        while categoria == "":
            print("La categoría no puede estar vacía.")
            categoria = input("Ingrese la categoría del producto: ").strip()

        precio_input = input("Ingrese el precio del producto (sin centavos): ").strip()
        while not precio_input.isdigit() or precio_input == "":
            print("El precio debe ser un número entero, sin centavos.")
            precio_input = input("Ingrese el precio del producto (sin centavos): ").strip()

        precio = int(precio_input)
        producto = [nombre, categoria, precio]
        productos.append(producto)

        print("\n¡Producto agregado correctamente!")

        # Vista adicional en columnas del producto recién creado
        print(f"\n{'N°':<5} | {'NOMBRE':<20} | {'CATEGORÍA':<15} | {'PRECIO':<10}")
        print("-" * 60)
        print(f"{len(productos):<5} | {nombre:<20} | {categoria:<15} | ${precio:<10}")

        input("\nPresioná Enter para volver al menú anterior...")

    # --- OPCIÓN 2: MOSTRAR ---
    elif opcion == 2:
        if not productos:
            print("\n[!] No hay productos registrados.")
        else:
            numero = 1
            print(f"\n{'N°':<5} | {'NOMBRE':<20} | {'CATEGORÍA':<15} | {'PRECIO':<10}")
            print("-" * 60)
            for prod in productos:
                print(f"{numero:<5} | {prod[0]:<20} | {prod[1]:<15} | ${prod[2]:<10}")
                numero += 1

        input("\nPresioná Enter para volver al menú anterior...")

    # --- OPCIÓN 3: BUSCAR ---
    elif opcion == 3:
        if not productos:
            print("\n[!] No hay productos registrados.")
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
                if prod[0].lower() == busqueda.lower():
                    print(f"{numero:<5} | {prod[0]:<20} | {prod[1]:<15} | ${prod[2]:<10}")
                    encontrado += 1
                numero += 1

            if encontrado == 0:
                print("No se encontraron productos con ese nombre.")

        

    # --- OPCIÓN 4: ELIMINAR ---
    elif opcion == 4:
        if not productos:
            print("\n[!] No hay productos registrados.")
        else:
            print("\nProductos registrados:")
            numero = 1
            for prod in productos:
                print(f"{numero} - {prod[0]} - {prod[1]} - ${prod[2]}")
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
                print(f"\nProducto '{eliminado[0]}' eliminado correctamente.")

        input("\nPresioná Enter para volver al menú anterior...")

    # --- OPCIÓN 5: SALIR ---
    elif opcion == 5:
        print("\nGracias por usar el sistema de gestión. ¡Nos vemos, gombre!")
"""""

productos = []
opcion = 0

while opcion != 5:
    print("\n" + "=" * 35)
    print("   SISTEMA DE GESTIÓN DE STOCK")
    print("=" * 35)
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")
    print("=" * 35)

    entrada = input("Elegí una opción (1-5): ").strip()

    if entrada.isdigit() and entrada != "":
        opcion = int(entrada)
    else:
        print("\n" + "!" * 45)
        print(" [!] ERROR: Opción inválida.")
        print(" Debe ingresar un número entero del 1 al 5.")
        print("!" * 45)
        input("\nPresioná Enter para volver al menú...")
        continue

        # --- OPCIÓN 1: AGREGAR ---
    if opcion == 1:
        nombre = input("\nIngrese el nombre del producto: ").strip()
        while nombre == "":
            print("El nombre no puede estar vacío.")
            nombre = input("Ingrese el nombre del producto: ").strip()

        categoria = input("Ingrese la categoría del producto: ").strip()
        while categoria == "":
            print("La categoría no puede estar vacía.")
            categoria = input("Ingrese la categoría del producto: ").strip()

        precio_input = input("Ingrese el precio del producto (sin centavos): ").strip()
        while not precio_input.isdigit() or precio_input == "":
            print("El precio debe ser un número entero, sin centavos.")
            precio_input = input("Ingrese el precio del producto (sin centavos): ").strip()

        precio = int(precio_input)
        producto = [nombre, categoria, precio]
        productos.append(producto)

        print("\n¡Producto agregado correctamente!")

        # Vista adicional en columnas del producto recién creado
        print(f"\n{'N°':<5} | {'NOMBRE':<20} | {'CATEGORÍA':<15} | {'PRECIO':<10}")
        print("-" * 60)
        print(f"{len(productos):<5} | {nombre:<20} | {categoria:<15} | ${precio:<10}")

        input("\nPresioná Enter para volver al menú anterior...")

    # --- OPCIÓN 2: MOSTRAR ---
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
                print(f"{numero:<5} | {prod[0]:<20} | {prod[1]:<15} | ${prod[2]:<10}")
                numero += 1

        input("\nPresioná Enter para volver al menú anterior...")

    # --- OPCIÓN 3: BUSCAR ---
    elif opcion == 3:
        if not productos:
            print("\n" + "*" * 45)
            print(" [!] ALERTA: Base de datos vacía.")
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
                if prod[0].lower() == busqueda.lower():
                    print(f"{numero:<5} | {prod[0]:<20} | {prod[1]:<15} | ${prod[2]:<10}")
                    encontrado += 1
                numero += 1

            if encontrado == 0:
                print("No se encontraron productos con ese nombre.")

        input("\nPresioná Enter para volver al menú anterior...")

    # --- OPCIÓN 4: ELIMINAR ---
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
                print(f"{numero} - {prod[0]} - {prod[1]} - ${prod[2]}")
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
                print(f"\nProducto '{eliminado[0]}' eliminado correctamente.")

        input("\nPresioná Enter para volver al menú anterior...")

    # --- OPCIÓN 5: SALIR ---
    elif opcion == 5:
        print("\nGracias por usar el sistema de gestión. ¡Nos vemos, gombre!")