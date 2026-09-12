productos = []

opcion = ""


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
        
    return dato



def pedir_precio():
    precio = input("Ingrese el valor del producto, sin centavos ")
        
    while precio == "" or not precio.isdigit():
        print("El precio debe ser un numero entero, sin centavos. ")
        precio = input("Ingrese el valor del producto, sin centavos ")
        
    return int(precio)



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
    
    datos_extra = ("Disponible","Sin Descuento")
        
    producto = {
        "nombre": nombre,
        "categoria":categoria,
        "precio":precio,
        "extra" : datos_extra
    } 
    productos.append(producto)
    
    print("Producto agregado correctamente")
    
    
    

def mostrar_productos():
    if productos == []:
        print("No hay prodcutos registrados")
    else:
        
        numero = 1
        print(f"{'N°':<5} {'nombre':<20} {'categoria':<15} {'precio':<10}")
        for producto in productos:
            print(f"{numero:<5} {producto["nombre"]:<20} {producto["categoria"]:<15} {producto["precio"]:<10}")
            numero = numero + 1




def buscar_producto():
    if productos == []:
            print("No hay prodcutos registrados para buscar")
    else:
        
        busqueda = input("Ingresa el nombre del producto a buscar ")
        
        
        while busqueda == "":
            print("La busqueda no puede estar vacia")
            busqueda = input("Ingresa el nombre del producto a buscar ")
        
        encontrado = 0
        numero = 1
        
        for producto in productos:
            
            if producto["nombre"] == busqueda:
                print("producto", numero)
                print("Nombre: ", producto["nombre"])
                print("Categoria: ", producto["categoria"])
                print("Precio: $", producto["precio"])
                print("----------------------")
                encontrado = encontrado + 1
                
        if encontrado == 0:
            print("No se encontraron productos con ese nombre")
            
            
            
            
            
def eliminar_producto():
    if productos == []:
            print("No hay prodcutos registrados")
    else:
        print("Productos registrado")
        numero = 1
        
        for producto in productos:
            print(f"{numero} - {producto["nombre"]} - {producto["categoria"]} - ${producto["precio"]}")
            numero = numero + 1
        
        posicion = input("Ingresa el numero del producto que queres eliminar ")
        
        while posicion == "" or not posicion.isdigit():
            print("Debes ingresar un numero valido")
            posicion = input("Ingresa el numero del producto que queres eliminar ")
            
        posicion = int(posicion)
        
        if posicion < 1 or posicion > len(productos):
            print("No existe un producto con ese numero")
        else:
            
            productos.pop(posicion - 1)
            
            print("Prodcuto eliminado correctamente")
    

while opcion != "5":

    mostrar_menu()

    opcion = input("Elegi una opcion: ")

    if opcion == "1":
        crear_producto()

    elif opcion == "2":
        mostrar_productos()

    elif opcion == "3":
        buscar_producto()

    elif opcion == "4":
        eliminar_producto()

    elif opcion == "5":
        print("Gracias por usar el sistema")

    else:
        print("Opcion invalida. Elegi una opcion del 1 al 5")

































# while opcion != "5":
    
#     mostrar_menu()
    
#     opcion = input("Elegi una opcion: ")
    
#     if opcion == "1":
#         crear_producto()
#         # nombre = input("Ingrese el nombre del producto ")
        
#         # while nombre == "":
#         #     print("El nombre no puede estar vacio")
#         #     nombre = input("Ingrese el nombre del producto ")
        
#         # categoria = input("Ingrese la categoria del producto ")
        
#         # while categoria == "":
#         #     print("La categoria no puede estar vacia")
#         #     categoria = input("Ingrese la categoria del producto ")
            
#         # precio = input("Ingrese el valor del producto, sin centavos ")
        
#         # while precio == "" or not precio.isdigit():
#         #     print("El precio debe ser un numero entero, sin centavos. ")
#         #     precio = input("Ingrese el valor del producto, sin centavos ")
        
#         # precio = int(precio)
        
#         # producto = [nombre, categoria, precio]
        
#         # Tupla
#         # datos_extra = ("Disponible","Sin Descuento")
        
#         # producto = {
#         #     "nombre": nombre,
#         #     "categoria":categoria,
#         #     "precio":precio,
#         #     "extra" : datos_extra
#         # }
        
#         # # productos = productos + [producto]
        
#         # productos.append(producto)
        
#         # print("Producto agregado correctamente")
        
        
#     elif opcion == "2":
#         mostrar_productos()
#         # if productos == []:
#         #     print("No hay prodcutos registrados")
#         # else:
           
#         #    numero = 1
#         #    print(f"{'N°':<5} {'nombre':<20} {'categoria':<15} {'precio':<10}")
#         #    for producto in productos:
#         #         # print("producto", numero)
#         #         # print("Nombre: ", producto[0])
#         #         # print("Categoria: ", producto[1])
#         #         # print("Precio: $", producto[2])
#         #         # print("----------------------")
                
#         #         print(f"{numero:<5} {producto["nombre"]:<20} {producto["categoria"]:<15} {producto["precio"]:<10}")
#         #         numero = numero + 1
                
#     elif opcion == "3":
#         busscar_producto()
#         # if productos == []:
#         #     print("No hay prodcutos registrados para buscar")
#         # else:
            
#         #     busqueda = input("Ingresa el nombre del producto a buscar ")
            
            
#         #     while busqueda == "":
#         #         print("La busqueda no puede estar vacia")
#         #         busqueda = input("Ingresa el nombre del producto a buscar ")
            
#         #     encontrado = 0
#         #     numero = 1
            
#         #     for producto in productos:
                
#         #         if producto["nombre"] == busqueda:
#         #             print("producto", numero)
#         #             print("Nombre: ", producto["nombre"])
#         #             print("Categoria: ", producto["categoria"])
#         #             print("Precio: $", producto["precio"])
#         #             print("----------------------")
#         #             encontrado = encontrado + 1
                    
#         #     if encontrado == 0:
#         #         print("No se encontraron productos con ese nombre")
                
#     elif opcion == "4":
#         eliminar_producto()
#         # if productos == []:
#         #     print("No hay prodcutos registrados")
#         # else:
#         #     print("Productos registrado")
#         #     numero = 1
            
#         #     for producto in productos:
#         #         print(f"{numero} - {producto["nombre"]} - {producto["categoria"]} - ${producto["precio"]}")
#         #         numero = numero + 1
            
#         #     posicion = input("Ingresa el numero del producto que queres eliminar ")
            
#         #     while posicion == "" or not posicion.isdigit():
#         #         print("Debes ingresar un numero valido")
#         #         posicion = input("Ingresa el numero del producto que queres eliminar ")
                
#         #     posicion = int(posicion)
            
#         #     if posicion < 1 or posicion > len(productos):
#         #         print("No existe un producto con ese numero")
#         #     else:
#         #         # nueva_lista = []
#         #         # numero = 1
                
#         #         # for producto in productos:
#         #         #     if numero != posicion:
#         #         #         nueva_lista = nueva_lista + [producto]  
#         #         #     numero = numero + 1
                
#         #         # productos = nueva_lista
#         #         # Pop()
#         #         productos.pop(posicion - 1)
                
#         #         # Remove
#         #         # producto_eliminar = productos[producto - 1]
                
#         #         # productos.remove(producto_eliminar)
#         #         print("Prodcuto eliminado correctamente")
                
# # ----------------------------------------------------------------------------------------
#                 # nombre_eliminar = input("Ingrese el nombre del producto para eliminar")
                
#                 # encontrado = False
                
#                 # for producto in productos:
#                 #     if producto[0] == nombre_eliminar:
                        
#                 #         productos.remove(producto)
#                 #         encontrado = True
#                 #         print("Producto Eliminado")
#                 #         break
                
#                 # if not encontrado:
#                 #     print("No se encontro producto para eliminar")
                
            
#     elif opcion == "5":
#         print("Gracias por usar el sistema")
    
#     else:
#         print("Opcion invalida. Elegi una opcion del 1 al 5")
        
        
        
# tupla = ({"nombre":("Emi",)},)

# print(tupla[0]["nombre"])

# tupla[0]["nombre"] = "Silvia"

# print(tupla)
