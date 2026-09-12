import sqlite3

conexion = sqlite3.connect("producto_bd.db")
cursor = conexion.cursor()
#creacion table (PARA TABLA FLOAT = REAL)
cursor.execute("""
CREATE TABLE IF NOT EXISTS producto_bd (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    categoria TEXT NOT NULL,
    precio INTEGER NOT NULL
)               
""")

conexion.commit()

def guardar_producto_bd(nombre, categoria, precio):
    cursor.execute("""
INSERT INTO producto_bd(nombre, categoria, precio)
VALUES (?, ?, ?)
""", (nombre, categoria, precio))                   

    conexion.commit()    

