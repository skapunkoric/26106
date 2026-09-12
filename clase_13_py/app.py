import sqlite3
productos_iniciales= [

("Lapiz" , 25.50),
("Cuaderno" , 120.50),
("Mochila" , 890.99),
("Regla" , 15.00),
("Goma" , 8.50)
]

conexion = sqlite3.connect("talendo_productos.db")
cursor = conexion.cursor()
"""
cursor.execute('''
CREATE TABLE IF NOT EXISTS productos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,               
    nombre TEXT NOT NULL,
    precio REAL NOT NULL           
               )
''')
conexion.commit()
for nombre , precio in productos_iniciales:
    cursor.execute(
    "INSERT INTO productos (nombre,precio) VALUES (?, ?)",
    (nombre,precio)
)
conexion.commit()
#cursor.execute("DELETE FROM productos")
#conexion.commit()
"""
# Select
cursor.execute("SELECT * FROM productos")
todos= cursor.fetchall()
for producto in todos:
    print(f"{producto}")


cursor.execute("SELECT * FROM productos WHERE precio >?", (50,))
filtrados = cursor.fetchall()
print ("--------"*20)
for producto_50 in filtrados:
    print(f"{producto_50}")

# ORDER BY ASC  /DESC
cursor.execute("SELECT * FROM productos ORDER BY precio ASC")
order_by = cursor.fetchall()
print ("--------" * 10)
for producto_order in order_by:
    print(f"{producto_order}")    

cursor.execute("SELECT * FROM productos ORDER BY precio DESC")
order_by_desc = cursor.fetchall()
print ("--------" * 10)
for producto_order_desc in order_by_desc:
    print(f"{producto_order_desc}")

# Update
"""
nuevo_precio = 30.00
id_act = 1
cursor.execute("UPDATE productos SET precio = ? WHERE  id = ?", (nuevo_precio,id_act))
conexion.commit()
"""
# vendo el resultado
id_act = 1
cursor.execute("SELECT * FROM productos WHERE id = ?", (id_act,))
filtrados_por_30 = cursor.fetchone()
print ("--------" * 10)
for producto_30 in filtrados_por_30:
    print(f"{producto_30}")

# Update varios
"""
cursor.execute("UPDATE productos SET precio = precio * 1.10 WHERE  precio  ?", (50,))
conexion.commit()
"""
# verlo 
cursor.execute("SELECT * FROM productos ORDER BY precio ASC")
order_precio = cursor.fetchall()
print ("--------" * 10)
for order_by_50 in order_precio:
    print(f"{order_by_50}")

# DELETE
"""
nombre_borrar = "Goma"
cursor.execute("DELETE  FROM productos WHERE nombre = ?" , (nombre_borrar,))        
conexion.commit()
"""

cursor.execute("SELECT * FROM productos")
todos_sin_goma= cursor.fetchall()
print ("--------" * 10)
for product_not_goma in todos_sin_goma:
    print(f"{product_not_goma}")