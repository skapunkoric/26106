import sqlite3
from tabulate import tabulate

DB_NAME = "productos_babul.db"
opcion = ""
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
    
    precio = input("Ingrese el valor del producto, sin centavos ")
    while precio == "" or not precio.isdigit():
        print("El precio debe ser un numero entero, sin centavos. ")
        precio = input("Ingrese el valor del producto, sin centavos ")
    
    return int(precio)

def pedir_texto(mensaje, mensaje_error):
    dato = input(mensaje)
    while dato =="":
        print(mensaje_error)
        dato = input(mensaje)
    return dato    

def hay_productos():
    conexion= conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT COUNT(*)FROM productos_babul")
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
    nombre = pedir_texto(
        "Ingrese el nombre del producto ",
        "El nombre no puede estar vacio"
        )
    
    categoria = pedir_texto(
        "Ingrese la categoria del producto ", 
        "La categoria no puede estar vacia"
        )
    
    precio = pedir_precio()

    descripcion = pedir_texto(
        "Ingrese la descripcion del producto ", 
        "La descripcion no puede estar vacia"
    )

    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("""
    INSERT INTO productos_babul (nombre, categoria, precio, descripcion)
    VALUES (?,?,?,?)""", (nombre, categoria, precio, descripcion))
    conexion.commit()
    conexion.close()
    print("Producto agregado correctamente")

               
def mostrar_productos():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT id, nombre, categoria, precio, descripcion  FROM productos_babul")
    productos = cursor.fetchall()
    conexion.close()
    if productos == []:
        print("No hay productos registrados")
    else:
        print(f"{'N°':<5} {'nombre':<20} {'categoria':<15} {'precio':<10}")
        for producto in productos:
            print(
                  f"{producto[0]:<5}) "
                  f"{producto[1]:<20}) "
                  f"{producto[2]:<15}) "
                  f"{producto[3]:<10}) "
                  f"{producto[4]:<10}) "
)

def buscar_producto():
    if not hay_productos():
            print("No hay prodcutos registrados para buscar")
    else:
        busqueda = input("Ingresa el nombre del producto a buscar ")
        
        
        while busqueda == "":
            print("La busqueda no puede estar vacia")
            busqueda = input("Ingresa el nombre del producto a buscar ")
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT id, nombre, categoria , precio, descripcion  FROM  productos_babul WHERE nombre = ?" , (busqueda,))
    productos = cursor.fetchall()
    conexion.close()
    if productos == []:
        print("No se encontraron productos con ese nombre")
        
    else:
        for producto in productos:
                print("producto", producto[0])
                print("Nombre: ", producto[1])
                print("Categoria: ", producto[2])
                print("Precio: $", producto[3])
                print("Descripcion: $", producto[4])
                print("----------------------")
                
def actualizar_producto():
    if not hay_productos():
        print ("no hay productos para actuzalizar")
    else:
        mostrar_productos()
    id_producto = input ("Ingresa el numero del producto que queres actualizar")
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT id  FROM  productos_babul WHERE  id = ?" , (id_producto,))
    producto = cursor.fetchone()
    
    if producto is None:
        print("no existe Producto con ese ID")
    else:
        nombre = pedir_texto("ingrese el nuevo nombre del producto", "el nombre no puede estar vacio")
        categoria = pedir_texto("ingrese la nuevo categoria del producto", "la categoria no puede estar vacio")
        precio = pedir_precio()
        descripcion = pedir_texto("ingrese la nueva descripcion del producto", " la  descripcion no puede estar vacia")
     
        cursor.execute(""" UPDATE productos_babul SET nombre =? , categoria = ? , precio = ? , descripcion = ? 
            WHERE id = ? """, (nombre, categoria, precio, descripcion, id_producto))
    conexion.commit()
    print("Producto actualizado correctamente")
    conexion.close()
    
def eliminar_producto():
        if not hay_productos():
            print("No hay productos registrados.")
        else:
            print("Productos registrados.")
            mostrar_productos()
            
        id_producto = input("Ingresa el número (ID) del producto que quieres eliminar: ")

        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute("SELECT id FROM productos_babul WHERE id = ?", (id_producto,))
        producto = cursor.fetchone()

        if producto is None:
            print("No existe un producto con ese número.")
            conexion.close()
        else:
            cursor.execute("DELETE FROM productos_babul WHERE id = ?", (id_producto,))
            conexion.commit()
            conexion.close()
            print("Producto eliminado correctamente.")

crear_tabla()

while opcion != 6:
    mostrar_menu()
    entrada = input("Elegí una opción (1-6): ").strip()
    if entrada.isdigit() and entrada != "" and 1 <= int(entrada) <= 7:
        opcion = int(entrada)
    else:
        print(" [!] ERROR: Opción inválida.")
        input("\nPresioná Enter para volver al menú...")
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
        print("\nGracias por usar el sistema de gestión. ¡Nos vemos, Vuelvas Pronto!")

    else:
        print("Opcion invalida. Elegi una opcion del 1 al 6")