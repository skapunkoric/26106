import sqlite3
from tabulate import tabulate

DB_NAME = "productos_babul.db"

# ==========================================
#        FUNCIONES DE UTILIDAD
# ==========================================

def pedir_texto(mensaje, mensaje_error):
    """Solicita un texto al usuario y valida que no esté vacío, limpiando espacios extra."""
    dato = input(mensaje).strip()
    while dato == "":
        print(f"[!] {mensaje_error}")
        dato = input(mensaje).strip()
    return dato

def pedir_entero(mensaje, mensaje_error):
    """Solicita un número (precio o cantidad) y asegura que sea un entero válido."""
    numero = input(mensaje).strip()
    while numero == "" or not numero.isdigit():
        print(f"[!] {mensaje_error}")
        numero = input(mensaje).strip()
    return int(numero)

def mostrar_menu():
    """Imprime el menú principal del sistema en la consola."""
    print("\n" + "=" * 35)
    print("   SISTEMA DE GESTIÓN DE STOCK by Babul")
    print("=" * 35)
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Actualizar producto")
    print("5. Eliminar producto")
    print("6. Salir")
    print("=" * 35)

# ==========================================
#        FUNCIONES DE BASE DE DATOS -
# ==========================================

def conectar():
    """Establece y retorna la conexión con la base de datos SQLite."""
    return sqlite3.connect(DB_NAME)

def crear_tabla():
    """Crea la tabla 'productos_babul' si no existe en la base de datos."""
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS productos_babul(
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        nombre TEXT NOT NULL,
        categoria TEXT NOT NULL,
        precio INTEGER NOT NULL,
        cantidad INTEGER MOT NULL,
        descripcion TEXT NOT NULL,
        estado TEXT 
    )
    """)
    conexion.commit()
    conexion.close()

def hay_productos():
    """Verifica si existe al menos un producto registrado en la base de datos."""
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT COUNT(*) FROM productos_babul")
    cantidad = cursor.fetchone()[0]
    conexion.close()
    return cantidad > 0

def cargar_datos_prueba():
    """Inyecta 10 productos tecnológicos de prueba si la base de datos está vacía."""
    if hay_productos():
        return

    productos_falsos = [
        ("Monitor Gamer 24'", "Monitores", 185000, 15 , "Monitor LED 144Hz 1ms Full HD"),
        ("Teclado Mecánico", "Periféricos", 45000, 22,  "Teclado RGB con switches red"),
        ("Mouse Óptico Inalámbrico", "Periféricos", 28000, 49, "Mouse ergonómico 3200 DPI"),
        ("Placa de Video RTX 4060", "Componentes",  420000, 9, "NVIDIA 8GB GDDR6"),
        ("Memoria RAM 16GB", "Componentes", 55000, 45, "DDR4 3200MHz Kingston Fury"),
        ("Disco Sólido SSD 1TB", "Almacenamiento", 68000, 25, "Crucial NVMe M.2 de alta velocidad"),
        ("Fuente Certificada 750W", "Componentes", 89000, 12, "Fuente 80 Plus Bronze Gigabyte"),
        ("Gabinete ATX Mid Tower", "Componentes",  62000, 11, "Gabinete con 3 fanes RGB incluidos"),
        ("Auriculares con Mic", "Audio", 39000, 21,"Auriculares Over-Ear sonido 7.1"),
        ("Procesador Ryzen 5 5600X", "Componentes",  210000, 15, "AMD AM4 6 núcleos 12 hilos")
    ]

    conexion = conectar()
    cursor = conexion.cursor()
    cursor.executemany("""
    INSERT INTO productos_babul (nombre, categoria, precio, cantidad, descripcion)
    VALUES (?, ?, ?, ?, ?)
    """, productos_falsos)
    conexion.commit()
    conexion.close()
    print("\n📦 Se cargaron 10 productos de prueba automáticamente.")

# ==============================================================================================
#        LÓGICA DEL SISTEMA (CRUD) create crear , read leer , update actualizar y delete borrar
# ===============================================================================================

def crear_producto():
    """Pide los datos al usuario y da de alta un nuevo producto (CREATE)."""
    print("\n--- ALTA DE PRODUCTO ---")
    
    nombre = pedir_texto("Ingrese el nombre del producto: ", "El nombre no puede estar vacío.")
    categoria = pedir_texto("Ingrese la categoría del producto: ", "La categoría no puede estar vacía.")
    precio = pedir_entero("Ingrese el precio (sin centavos): ", "El precio debe ser un número entero.")
    cantidad = pedir_entero("Ingrese el la cantidad : ", "La cantidad debe ser un número entero.")
    descripcion = pedir_texto("Ingrese la descripción del producto: ", "La descripción no puede estar vacía.")

    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("""
    INSERT INTO productos_babul (nombre, categoria, precio, cantidad, descripcion)
    VALUES (?,?,?,?,?)""", (nombre, categoria, precio, cantidad, descripcion))
    conexion.commit()
    conexion.close()
    print("\n✅ ¡Producto agregado correctamente!")

def mostrar_productos():
    """Selecciona todos los productos y los muestra en una tabla formateada lee(READ)."""
    if not hay_productos():
        print("\n[!] No hay productos registrados en el sistema.")
        return 

    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT id, nombre, categoria, precio, cantidad,descripcion FROM productos_babul")
    productos = cursor.fetchall()
    conexion.close()
    
    headers = ["ID", "NOMBRE", "CATEGORÍA", "PRECIO ($)", "CANTIDAD", "DESCRIPCIÓN"]
    print("\n" + tabulate(productos, headers=headers, tablefmt="fancy_grid" \
    ""))

def buscar_producto():
    """Busca productos por coincidencia parcial en el nombre y los muestra (LECTURA)."""
    if not hay_productos():
        print("\n[!] No hay productos registrados para buscar.")
        return

    busqueda = pedir_texto("\nIngresa el nombre del producto a buscar: ", "La búsqueda no puede estar vacía.")
    
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT id, nombre, categoria, cantidad, precio, descripcion FROM productos_babul WHERE nombre LIKE ?", ('%' + busqueda + '%',))
    productos = cursor.fetchall()
    conexion.close()
    
    if not productos:
        print("\n[!] No se encontraron productos con ese nombre.")
    else:
        headers = ["ID", "NOMBRE", "CATEGORÍA", "PRECIO ($)", "CANTIDAD", "DESCRIPCIÓN"]
        print("\n" + tabulate(productos, headers=headers, tablefmt="fancy_grid"))
                
def actualizar_producto():
    """Permite modificar un producto existente mediante su ID, manteniendo datos si se deja vacío (UPDATE)."""
    if not hay_productos():
        print("\n[!] No hay productos para actualizar.")
        return
    
    mostrar_productos()
    id_producto = input("\nIngresa el número del producto que querés actualizar: ").strip()
    
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT nombre, categoria, precio, cantidad, descripcion FROM productos_babul WHERE id = ?", (id_producto,))
    producto = cursor.fetchone()
    
    if producto is None:
        print("\n[!] No existe un producto con ese ID.")
        conexion.close()
        return
    
    nombre_act, categoria_act, precio_act, cantidad_act, descripcion_act = producto
    
    print(f"\n--- Modificando Producto ID {id_producto} ---")
    print("(Presioná Enter sin escribir nada para mantener el valor actual)")
    
    nombre = input(f"Nombre [{nombre_act}]: ").strip()
    if nombre == "":
       nombre = nombre_act
        
    categoria = input(f"Categoría [{categoria_act}]: ").strip()
    if categoria == "": 
       categoria = categoria_act
    
    while True:
        precio_inp = input(f"Precio [{precio_act}]: ").strip()
        if precio_inp == "":
            precio = precio_act 
            break
        elif precio_inp.isdigit():
            precio = int(precio_inp)
            break
        else:
            print("[!] El precio debe ser un número entero válido.")
            
    while True:
        cantidad_inp = input(f"Stock [{cantidad_act}]: ").strip()
        if cantidad_inp == "":
            cantidad = cantidad_act 
            break
        elif cantidad_inp.isdigit():
            cantidad = int(cantidad_inp)
            break
        else:
            print("[!] La cantidad debe ser un número entero válido.")
    
    descripcion = input(f"Descripción [{descripcion_act}]: ").strip()
    if descripcion == "":
       descripcion = descripcion_act
     
    cursor.execute(""" 
            UPDATE productos_babul 
            SET nombre = ?, categoria = ?, precio = ?, cantidad= ?, descripcion = ? 
            WHERE id = ? 
        """, (nombre, categoria, precio, cantidad, descripcion, id_producto))
    conexion.commit()
    conexion.close()
    print("\n✅ Producto actualizado correctamente.")
    
def eliminar_producto():
    """Elimina un producto de la base de datos usando su ID (DELETE)."""
    if not hay_productos():
        print("\n[!] No hay productos registrados para eliminar.")
        return 
        
    mostrar_productos()
    id_producto = input("\nIngresa el número (ID) del producto que quieres eliminar: ").strip()

    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT id FROM productos_babul WHERE id = ?", (id_producto,))
    producto = cursor.fetchone()

    if producto is None:
        print("\n[!] No existe un producto con ese número.")
    else:
        cursor.execute("DELETE FROM productos_babul WHERE id = ?", (id_producto,))
        conexion.commit()
        print("\n✅ Producto eliminado correctamente.")
    conexion.close()

# ==========================================
#        FLUJO PRINCIPAL DEL PROGRAMA
# ==========================================

crear_tabla()
cargar_datos_prueba()
opcion = 0    

while opcion != 6:
    mostrar_menu()
    entrada = input("Elegí una opción (1-6): ").strip()
    
    if entrada.isdigit() and entrada != "" and 1 <= int(entrada) <= 6:
        opcion = int(entrada)
    else:
        print("\n[!] ERROR: Opción inválida.")
        input("Presioná Enter para volver al menú...")
        continue

    if opcion == 1:
        crear_producto()
    elif opcion == 2:
        mostrar_productos()
    elif opcion == 3:
        buscar_producto()
    elif opcion == 4:
        actualizar_producto()
    elif opcion == 5:
        eliminar_producto()
    elif opcion == 6:
        print("\n¡Gracias por usar el sistema de gestión B4BU1! Nos vemos,¡Vuelvas Pronto!")

    if opcion != 6:
        input("\nPresioná Enter para volver al menú...")