"""""
def saludar():
    print("hola")

saludar()


def saludar_dos(nombre):
    print("Hola", nombre)

    
saludar_dos('Babul')
saludar_dos('Caro')
saludar_dos('Tolen')

usuario = input("ingresar nombre: ")

def saludar_tres(usuario):
    print("Hola", usuario)

saludar_tres(usuario)    

def saludar_cuatro(nombre,ape):
    print("Hola", nombre,ape)
nombre = input("ingresar nombre: ")
apellido = input("ingresar apellido: ")
saludar_cuatro(nombre,apellido)    


def saludar_cinco(nombre,mensaje="Hola"):
    print(mensaje,nombre)
usuario = input("ingresar nombre: ")

saludar_cinco(usuario,"Hola Soy")    

def registrar_usuario(nombre,edad,ciudad):
    print(f"Nombre: {nombre}, Edad: {edad}, Ciudad: {ciudad}")

registrar_usuario(edad=30,nombre="Carlos",ciudad="Madrid")

def nostrar_variable_local():
    mensaje = "soy una variable local"
    print(mensaje)

#mostrar_variable_local()

#print(mensaje)

nombre_global = "Maca"

#def nostrar_variable_global():
    #print(f"nombre de la vaiable global :{nombre_global}")

def nodificar_variable_goblal():
    global nombre_global
    print(nombre_global)
    nombre_goblal = "Emi"
    print(nombre_global)

modificar_variable_goblal()

verduras = ["lechuha","rucula"]
def agregar_producto(lista,nuevo_producto):
    lista.append(nuevo_producto)

producto_nuevo = "zapallo"
agregar_producto(verduras,producto_nuevo)

print(verduras)
"""
verduras = ["lechuha","rucula"]
def agregar_producto1(lista,nuevo_producto):
    lista.append(nuevo_producto)
    print(lista)

producto_nuevo = "zapallo"

agregar_producto1(verduras.copy(),producto_nuevo)
print(verduras)
