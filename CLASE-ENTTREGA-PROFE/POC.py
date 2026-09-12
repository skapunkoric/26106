import sqlite3

DB_NAME = "productos.db"
opcion = ""


def conectar():
    return sqlite3.connect(DB_NAME)


def crear_tabla():
    conexion = conectar()
    cursor = conexion.cursor()  # <-- Corregido: faltaban los ()
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS productos
                   (
                       id
                       INTEGER
                       PRIMARY
                       KEY
                       AUTOINCREMENT
                       NOT
                       NULL,
                       nombre
                       TEXT
                       NOT
                       NULL,
                       categoria
                       TEXT
                       NOT
                       NULL,
                       precio
                       INTEGER
                       NOT
                       NULL,
                       descripcion
                       TEXT
                       NOT
                       NULL,
                       estado
                       TEXT
                       NOT
                       NULL
                   )
                   """)
    conexion.commit()
    conexion.close()  # <-- Corregido: decía clore()


def mostrar_menu():
    print("\n=== Sistema de gestión de productos ===")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Actualizar producto")
    print("5. Eliminar producto")
    print("6. Salir")


def pedir_texto(mensaje, mensaje_error):
    dato = input(mensaje).strip()
    while dato == "":
        print(mensaje_error)
        dato = input(mensaje).strip()
    return dato


def pedir_precio():
    precio = input("Ingrese el valor del producto, sin centavos: ")
    while precio == "" or not precio.isdigit():
        print("El precio debe ser un número entero, sin centavos.")
        precio = input("Ingrese el valor del producto, sin centavos: ")
    return int(precio)


def hay_productos():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT COUNT(*) FROM productos")
    cantidad = cursor.fetchone()[0]
    conexion.close()
    return cantidad > 0


def crear_producto():
    nombre = pedir_texto("Ingrese el nombre del producto: ", "El nombre no puede estar vacío.")
    categoria = pedir_texto("Ingrese la categoría del producto: ", "La categoría no puede estar vacía.")
    precio = pedir_precio()
    descripcion = pedir_texto("Ingrese la descripción del producto: ", "La descripción no puede estar vacía.")

    # Valores por defecto para cumplir con la estructura de tu tabla
    estado_defecto = "Disponible"

    conexion = conectar()
    cursor = conexion.cursor()
    # Corregido: Agregados los campos, correspondencia de 'estado' y las 5 incógnitas (?,?,?,?,?)
    cursor.execute("""
                   INSERT INTO productos (nombre, categoria, precio, descripcion, estado)
                   VALUES (?, ?, ?, ?, ?) """, (nombre, categoria, precio, descripcion, estado_defecto))
    conexion.commit()
    conexion.close()

    print("Producto agregado correctamente.")


def mostrar_productos():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT id, nombre, categoria, precio, descripcion FROM productos")
    productos = cursor.fetchall()
    conexion.close()

    if not productos:
        print("No hay productos registrados.")
    else:
        print("\n" + "-" * 60)
        print(f"{'N°':<5} {'Nombre':<20} {'Categoría':<15} {'Precio':<10}")
        print("-" * 60)
        for producto in productos:
            print(f"{producto[0]:<5} {producto[1]:<20} {producto[2]:<15} ${producto[3]:<10}")
        print("-" * 60)


def buscar_producto():
    if not hay_productos():
        print("No hay productos registrados para buscar.")
        return

    busqueda = pedir_texto("Ingresa el nombre del producto a buscar: ", "La búsqueda no puede estar vacía.")

    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT id, nombre, categoria, precio, descripcion FROM productos WHERE nombre LIKE ?",
                   (f"%{busqueda}%",))
    productos = cursor.fetchall()
    conexion.close()

    if not productos:
        print("No se encontraron productos con ese nombre.")
    else:
        for producto in productos:
            print("\n----------------------")
            print(f"ID Producto: {producto[0]}")
            print(f"Nombre:      {producto[1]}")
            print(f"Categoría:   {producto[2]}")
            print(f"Precio:      ${producto[3]}")
            print(f"Descripción: {producto[4]}")
            print("----------------------")


def actualizar_producto():
    if not hay_productos():
        print("No hay productos para actualizar.")
        return

    mostrar_productos()
    id_producto = input("Ingresa el número (ID) del producto que quieres actualizar: ")

    conexion = conectar()
    cursor = conexion.cursor()
    # Corregido: Se quitó la coma inválida y se cambió a filtrar por 'id = ?'
    cursor.execute("SELECT id FROM productos WHERE id = ?", (id_producto,))
    producto = cursor.fetchone()

    if producto is None:
        print("No existe un producto con ese ID.")
        conexion.close()
    else:
        nombre = pedir_texto("Ingrese el nuevo nombre del producto: ", "El nombre no puede estar vacío.")
        categoria = pedir_texto("Ingrese la nueva categoría del producto: ", "La categoría no puede estar vacía.")
        precio = pedir_precio()
        descripcion = pedir_texto("Ingrese la nueva descripción del producto: ", "La descripción no puede estar vacía.")

        cursor.execute("""
                       UPDATE productos
                       SET nombre      = ?,
                           categoria   = ?,
                           precio      = ?,
                           descripcion = ?
                       WHERE id = ? """, (nombre, categoria, precio, descripcion, id_producto))
        conexion.commit()
        conexion.close()
        print("Producto actualizado correctamente.")


def eliminar_producto():
    if not hay_productos():
        print("No hay productos registrados.")
        return

    mostrar_productos()
    id_producto = input("Ingresa el número (ID) del producto que quieres eliminar: ")

    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT id FROM productos WHERE id = ?", (id_producto,))
    producto = cursor.fetchone()

    if producto is None:
        print("No existe un producto con ese número.")
        conexion.close()
    else:
        # Corregido: Sintaxis de DELETE FROM estándar y la tupla con coma final
        cursor.execute("DELETE FROM productos WHERE id = ?", (id_producto,))
        conexion.commit()
        conexion.close()
        print("Producto eliminado correctamente.")


# Inicializamos la tabla base
crear_tabla()

while opcion != "6":
    mostrar_menu()
    opcion = input("Elegí una opción: ")

    if opcion == "1":
        crear_producto()
    elif opcion == "2":
        mostrar_productos()
    elif opcion == "3":
        buscar_producto()
    elif opcion == "4":  # Corregido: Opción 4 según tu menú es Actualizar
        actualizar_producto()
    elif opcion == "5":  # Corregido: Opción 5 según tu menú es Eliminar
        eliminar_producto()
    elif opcion == "6":
        print("Gracias por usar el sistema.")
    else:
        print("Opción inválida. Elegí una opción del 1 al 6.")