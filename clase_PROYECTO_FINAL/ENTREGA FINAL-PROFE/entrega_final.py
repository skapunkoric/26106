import sqlite3

DB_NAME = "inventario.db"


def conectar_db():
    return sqlite3.connect(DB_NAME)


def crear_tabla():
    conexion = conectar_db()
    cursor = conexion.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            descripcion TEXT,
            cantidad INTEGER NOT NULL,
            precio REAL NOT NULL,
            categoria TEXT
        )
    """)

    conexion.commit()
    conexion.close()


def mostrar_menu():
    print("\nSistema de gestión de inventario")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto por ID")
    print("4. Actualizar cantidad")
    print("5. Eliminar producto")
    print("6. Reporte de bajo stock")
    print("7. Salir")


def pedir_texto(mensaje, mensaje_error):
    dato = input(mensaje).strip()

    while dato == "":
        print(mensaje_error)
        dato = input(mensaje).strip()

    return dato


def pedir_entero(mensaje, mensaje_error):
    dato = input(mensaje).strip()

    while dato == "" or not dato.isdigit():
        print(mensaje_error)
        dato = input(mensaje).strip()

    return int(dato)


def pedir_precio():
    precio = input("Ingrese el precio del producto: ").strip()

    while precio == "":
        print("El precio no puede estar vacío.")
        precio = input("Ingrese el precio del producto: ").strip()

    while not precio.replace(".", "", 1).isdigit():
        print("El precio debe ser un número válido. Por ejemplo: 1500 o 1500.50")
        precio = input("Ingrese el precio del producto: ").strip()

    return float(precio)


def agregar_producto():
    nombre = pedir_texto(
        "Ingrese el nombre del producto: ",
        "El nombre no puede estar vacío."
    )

    descripcion = pedir_texto(
        "Ingrese una descripción del producto: ",
        "La descripción no puede estar vacía."
    )

    cantidad = pedir_entero(
        "Ingrese la cantidad disponible: ",
        "La cantidad debe ser un número entero."
    )

    precio = pedir_precio()

    categoria = pedir_texto(
        "Ingrese la categoría del producto: ",
        "La categoría no puede estar vacía."
    )

    conexion = conectar_db()
    cursor = conexion.cursor()

    cursor.execute("""
        INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria)
        VALUES (?, ?, ?, ?, ?)
    """, (nombre, descripcion, cantidad, precio, categoria))

    conexion.commit()
    conexion.close()

    print("Producto agregado correctamente.")


def mostrar_productos():
    conexion = conectar_db()
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()

    conexion.close()

    if productos == []:
        print("No hay productos registrados.")
    else:
        print("\nProductos registrados:")
        print(f"{'ID':<5} {'Nombre':<20} {'Descripción':<25} {'Cantidad':<10} {'Precio':<10} {'Categoría':<15}")
        print("-" * 90)

        for producto in productos:
            print(f"{producto[0]:<5} {producto[1]:<20} {producto[2]:<25} {producto[3]:<10} ${producto[4]:<9.2f} {producto[5]:<15}")


def buscar_producto_por_id():
    id_producto = pedir_entero(
        "Ingrese el ID del producto a buscar: ",
        "El ID debe ser un número entero."
    )

    conexion = conectar_db()
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM productos WHERE id = ?", (id_producto,))
    producto = cursor.fetchone()

    conexion.close()

    if producto is None:
        print("No se encontró un producto con ese ID.")
    else:
        print("\nProducto encontrado:")
        print("ID:", producto[0])
        print("Nombre:", producto[1])
        print("Descripción:", producto[2])
        print("Cantidad:", producto[3])
        print("Precio: $", producto[4])
        print("Categoría:", producto[5])


def actualizar_cantidad():
    id_producto = pedir_entero(
        "Ingrese el ID del producto a actualizar: ",
        "El ID debe ser un número entero."
    )

    nueva_cantidad = pedir_entero(
        "Ingrese la nueva cantidad disponible: ",
        "La cantidad debe ser un número entero."
    )

    conexion = conectar_db()
    cursor = conexion.cursor()

    cursor.execute(
        "UPDATE productos SET cantidad = ? WHERE id = ?",
        (nueva_cantidad, id_producto)
    )

    conexion.commit()

    if cursor.rowcount == 0:
        print("No se encontró un producto con ese ID.")
    else:
        print("Cantidad actualizada correctamente.")

    conexion.close()


def eliminar_producto():
    id_producto = pedir_entero(
        "Ingrese el ID del producto a eliminar: ",
        "El ID debe ser un número entero."
    )

    conexion = conectar_db()
    cursor = conexion.cursor()

    cursor.execute("DELETE FROM productos WHERE id = ?", (id_producto,))

    conexion.commit()

    if cursor.rowcount == 0:
        print("No se encontró un producto con ese ID.")
    else:
        print("Producto eliminado correctamente.")

    conexion.close()


def reporte_bajo_stock():
    limite = pedir_entero(
        "Ingrese el límite de stock: ",
        "El límite debe ser un número entero."
    )

    conexion = conectar_db()
    cursor = conexion.cursor()

    cursor.execute(
        "SELECT * FROM productos WHERE cantidad <= ?",
        (limite,)
    )

    productos = cursor.fetchall()

    conexion.close()

    if productos == []:
        print("No hay productos con bajo stock.")
    else:
        print("\nReporte de bajo stock:")
        print(f"{'ID':<5} {'Nombre':<20} {'Cantidad':<10} {'Categoría':<15}")
        print("-" * 55)

        for producto in productos:
            print(f"{producto[0]:<5} {producto[1]:<20} {producto[3]:<10} {producto[5]:<15}")


def iniciar_programa():
    crear_tabla()

    opcion = ""

    while opcion != "7":
        mostrar_menu()
        opcion = input("Elegí una opción: ").strip()

        if opcion == "1":
            agregar_producto()

        elif opcion == "2":
            mostrar_productos()

        elif opcion == "3":
            buscar_producto_por_id()

        elif opcion == "4":
            actualizar_cantidad()

        elif opcion == "5":
            eliminar_producto()

        elif opcion == "6":
            reporte_bajo_stock()

        elif opcion == "7":
            print("Gracias por usar el sistema.")

        else:
            print("Opción inválida. Elegí una opción del 1 al 7.")


iniciar_programa()