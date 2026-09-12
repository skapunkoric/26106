import sqlite3

def crear_bb_dd():
    conexion= sqlite3.connect("instituto.db")
    cursor = conexion.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS alumnos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    edad INTEGER NOT NULL,
    curso TEXT NOT NULL)
                   """)

""" 
    def agregar_alumno():
    """
    #cursor.execute(""" INSERT INTO alumnos (nombre, edad, curso)
    #VALUES (?,?, ?)""", (nombre, edad, curso))"""
    #conexion.commit()
    #print("Alumno agregado con éxito.")
    """
    def mostrar_alumnos():
    
        cursor.execute("SELECT * FROM alumnos")
        alumnos = cursor.fetchall()
        print("\nLista de alumnos:")
        for alumno in alumnos:
        print(f"ID: {alumno[0]}, Nombre: {alumno[1]}, Edad: {alumno[2]},
        Curso: {alumno[3]}")
        def actualizar_curso(id_alumno, nuevo_curso):
"""
def registrar_alumno_seguro(nombre, edad, curso):
    conexion = sqlite3.connect("instituto.db")
    cursor = conexion.cursor()
    
    try: 
        conexion.execute("BEGIN TRANSACTION")
        cursor.execute("INSERT INTO alumnos (nombre, edad, curso) VALUES (?,?, ?)", (nombre, edad, curso))
        conexion.commit()
        print("Alumno agregado con éxito.")

    except sqlite3.Error as e:

        conexion.rollback()
        print(F"ERROR AL REGISTRAR AL Alumno NO OK.{e}")

    finally:
         conexion.close()

"""
Modifica el curso de un alumno específico
cursor.execute("UPDATE alumnos SET curso = ? WHERE id = ?",
(nuevo_curso, id_alumno))
conexion.commit()
print("Curso actualizado correctamente.")
def eliminar_alumno(id_alumno):
Elimina un alumno de la base de datos
cursor.execute("DELETE FROM alumnos WHERE id = ?", (id_alumno,))
conexion.commit()
print("Alumno eliminado correctamente.")
# Menú interactivo
while True:
print("\nGestión de Alumnos")
print("1. Agregar alumno")
print("2. Mostrar alumnos")
print("3. Actualizar curso de un alumno")
print("4. Eliminar alumno")
print("5. Salir")
"""