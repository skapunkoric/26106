"""
import sqlite3
from tabulate import tabulate

DB_NAME = "productos_babul.db"

def conectar():
    return sqlite3.connect(DB_NAME)

def crear_tabla():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS productos_babul(
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        nombre TEXT NOT NULL,
        categoria TEXT NOT NULL,
        precio INTEGER NOT NULL,
        descripcion TEXT NOT NULL,
        estado TEXT 
    )
    """)
    conexion.commit()
    conexion.close()

def pedir_precio():
    precio = input("Ingrese el valor del producto, sin centavos: ").strip()
    while precio == "" or not precio.isdigit():
        print("[!] El precio debe ser un numero entero, sin centavos.")
        precio = input("Ingrese el valor del producto, sin centavos: ").strip()
    return int(precio)

def pedir_texto(mensaje, mensaje_error):
    # Agregamos .strip() para que no hagan trampa metiendo espacios en blanco
    dato = input(mensaje).strip()
    while dato == "":
        print(f"[!] {mensaje_error}")
        dato = input(mensaje).strip()
    return dato    

def hay_productos():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT COUNT(*) FROM productos_babul")
    cantidad = cursor.fetchone()[0]
    conexion.close()
    return cantidad > 0

def mostrar_menu():
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

def crear_producto():
    print("\n--- ALTA DE PRODUCTO ---")
    nombre = pedir_texto("Ingrese el nombre del producto: ", "El nombre no puede estar vacio.")
    categoria = pedir_texto("Ingrese la categoria del producto: ", "La categoria no puede estar vacia.")
    precio = pedir_precio()
    descripcion = pedir_texto("Ingrese la descripcion del producto: ", "La descripcion no puede estar vacia.")

    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("""
    INSERT INTO productos_babul (nombre, categoria, precio, descripcion)
    VALUES (?,?,?,?)""", (nombre, categoria, precio, descripcion))
    conexion.commit()
    conexion.close()
    print("\n✅ ¡Producto agregado correctamente!")

def mostrar_productos():
    if not hay_productos():
        print("\n[!] No hay productos registrados en el sistema.")
        return # Corta la función acá si no hay nada

    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT id, nombre, categoria, precio, descripcion FROM productos_babul")
    productos = cursor.fetchall()
    conexion.close()
    
    # Magia de Tabulate en acción
    headers = ["ID", "NOMBRE", "CATEGORÍA", "PRECIO ($)", "DESCRIPCIÓN"]
    print("\n" + tabulate(productos, headers=headers, tablefmt="fancy_grid"))

def buscar_producto():
    if not hay_productos():
        print("\n[!] No hay productos registrados para buscar.")
        return

    busqueda = pedir_texto("\nIngresa el nombre del producto a buscar: ", "La busqueda no puede estar vacia.")
    
    conexion = conectar()
    cursor = conexion.cursor()
    # Usamos LIKE para que encuentre coincidencias parciales (no tiene que ser exacto)
    cursor.execute("SELECT id, nombre, categoria, precio, descripcion FROM productos_babul WHERE nombre LIKE ?", ('%' + busqueda + '%',))
    productos = cursor.fetchall()
    conexion.close()
    
    if not productos:
        print("\n[!] No se encontraron productos con ese nombre.")
    else:
        headers = ["ID", "NOMBRE", "CATEGORÍA", "PRECIO ($)", "DESCRIPCIÓN"]
        print("\n" + tabulate(productos, headers=headers, tablefmt="fancy_grid"))
                
def actualizar_producto():
    if not hay_productos():
        print("\n[!] No hay productos para actualizar.")
        return # Freno de mano
        
    mostrar_productos()
    id_producto = input("\nIngresa el numero del producto que queres actualizar: ").strip()
    
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT id FROM productos_babul WHERE id = ?", (id_producto,))
    producto = cursor.fetchone()
    
    if producto is None:
        print("\n[!] No existe un producto con ese ID.")
    else:
        print("\n--- Ingresando nuevos datos ---")
        nombre = pedir_texto("Ingrese el nuevo nombre del producto: ", "El nombre no puede estar vacio.")
        categoria = pedir_texto("Ingrese la nueva categoria del producto: ", "La categoria no puede estar vacia.")
        precio = pedir_precio()
        descripcion = pedir_texto("Ingrese la nueva descripcion del producto: ", "La descripcion no puede estar vacia.")
     
        cursor.execute(""" 
            UPDATE productos_babul 
            SET nombre = ?, categoria = ?, precio = ?, descripcion = ? 
            WHERE id = ? 
        """, (nombre, categoria, precio, descripcion, id_producto))
        conexion.commit()
        print("\n✅ Producto actualizado correctamente.")
        
    conexion.close()
    
def eliminar_producto():
    if not hay_productos():
        print("\n[!] No hay productos registrados para eliminar.")
        return # Freno de mano
        
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

# --- INICIO DEL FLUJO DEL PROGRAMA ---
crear_tabla()
opcion = 0 # Inicializamos la variable

while opcion != 6:
    mostrar_menu()
    entrada = input("Elegí una opción (1-6): ").strip()
    
    # Corregido: Ahora chequea hasta el 6
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
        print("\n¡Gracias por usar el sistema de gestión! Nos vemos, ¡Vuelvas Pronto!")


