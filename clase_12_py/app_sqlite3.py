import sqlite3

conexion = sqlite3.connect("talento.db")

cursor = conexion.cursor()

cursor.execute ("""
        CREATE TABLE IF NOT EXISTS clientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                apellido TEXT NOT NULL,
                correo TEXT NOT NULL
    )
"""                
)
cursor.execute(""" 
               INSERT INTO clientes(nombre , apellido , correo )
                VALUES (?,?,?)""",
                ("Babul", "Tolenpillo", "ana@email.com"),
                           
)
conexion.commit()
conexion.close()


