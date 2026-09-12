import sqlite3
from tabulate import tabulate # <--- Importamos la herramienta mágica

conexion = sqlite3.connect("talendo_productos.db")
cursor = conexion.cursor()

# --- CONSULTA 1: Todos los productos ---
cursor.execute("SELECT * FROM productos")
todos = cursor.fetchall()

print("\n" + "="*40)
print("       TODOS LOS PRODUCTOS")
print("="*40)
# tabulate se encarga de acomodar todo. 'headers' pone los títulos de las columnas
print(tabulate(todos, headers=["ID", "Nombre", "Precio"], tablefmt="grid"))


# --- CONSULTA 2: Filtrados > 50 ---
cursor.execute("SELECT * FROM productos WHERE precio > ?", (50,))
filtrados = cursor.fetchall()

print("\n" + "="*40)
print("   PRODUCTOS CON PRECIO MAYOR A 50")
print("="*40)
print(tabulate(filtrados, headers=["ID", "Nombre", "Precio"], tablefmt="grid"))


# --- CONSULTA 3: Ordenados por Nombre ---
cursor.execute("SELECT * FROM productos ORDER BY nombre")
todos_sin_goma = cursor.fetchall()

print("\n" + "="*40)
print("   PRODUCTOS ORDENADOS POR NOMBRE")
print("="*40)
print(tabulate(todos_sin_goma, headers=["ID", "Nombre", "Precio"], tablefmt="grid"))

conexion.close()