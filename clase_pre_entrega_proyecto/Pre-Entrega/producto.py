from herramientas import pedir_precio, pedir_texto

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
    
