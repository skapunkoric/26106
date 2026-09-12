

def mostrar_menu():
    print("Sistema de gestion de productos")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")
    
def pedir_texto(mensaje , mensaje_error):
    dato = input(mensaje)
    
    while dato == "":
        print(mensaje_error)
        dato = input(mensaje)
        print("======================================================")
    return dato

def pedir_precio():
    precio = input("Ingrese el valor del producto, sin centavos ")
        
    while precio == "" or not precio.isdigit():
        print("El precio debe ser un numero entero, sin centavos. ")
        precio = input("Ingrese el valor del producto, sin centavos ")
        print("======================================================")
    return int(precio)
