
producto = []
opcion = ""

while opcion != "5":
    print("1. Agregar producto")
    print("2. Mostrar productos")    
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")

    opcion = input("input elegi una opcion: ")
    
    if opcion =="1":

        nombre = input("ingrese el nombre del producto: ")
        
        while nombre == "":
            print("el nombre no puede estar vacio")
            nombre = input("ingrese el nombre del producto: ")

        categoria = input("ingrese el nombre del producto: ")   
        
        while categoria == "":
            print("la categoria no puede estar vacia")
            categoria = input("ingrese la categoria del producto: ")
         
        precio = input("ingrese el precio del producto, sin centavos: ") 
        precio.isdigit()
        while precio == "" or not precio.isdigit():
            print("el precio debe ser un numero entero, sin centavos")
            precio = input("ingrese el precio del producto, sin centavos: ") 
        
        precio = int(precio)
        producto = [nombre,categoria,precio]    
        productos = productos + [producto]
        print("producto agregado correctamente")

    elif opcion == "2":
        if producto  == []:
            print("no hay productos registrados")
        else:
             numero = 1

             for producto in productos:
                
                print("productos",numero)
                print("nombre ", producto[0]) 
                print("categoria ", producto[1])
                print("precios  ",    producto[2])    
                numero += 1
    
    elif opcion == "3":
        if producto  == []:
           print("no hay productos registrados")
        else:
            busqueda = input("ingresa el nombre del producto a buscar")
            
            while busqueda == "":
                print("la busqueda no puede estar vacia")
                busqueda = input("ingresa el nombre del producto a buscar")
            
            encontrado = 0
            numero = 1
             
            for producto in productos:
                if producto[0] == busqueda:

                    print("productos",numero)
                    print("nombre ", producto[0]) 
                    print("categoria ", producto[1])
                    print("precio $ ",    producto[2])
                    print("-------------------------- ")
                    encontrado += 1 

                    if encontrado == 0:
                        print("no se encontraron productos con ese nombre")

    elif opcion == "4":                    
        if producto  == []:
            print("no hay productos registrados")

        else:
            print("productos registrados")

            for producto in productos:
                print(f"{numero}-{producto[0]}-{producto[1]}¬${producto[2]} ")
                numero +=1
            
            posicion = input("ingrese el numero del producto que queres eliminar")
            while posicion =="" or not posicion.isdigit():
                 print("debes ingresar  el numero del producto que queres eliminar")
                 posicion = input("ingrese el numero del prodycto que queres eliminar")
            
            posicion = int(posicion)
            
            if posicion <1 or posicion > len(productos):
                print("no existe producto con ese numero")

            else:
                nueva_lista = []   
                numero = 1
              
                for producto in productos: 
                    if numero != posicion:
                      nueva_lista = nueva_lista + [productos]

                    numero += 1

                productos = nueva_lista
                
                print(" producto eliminado correctamente")

    elif opcion == "5":
        print("gracias por usar el sistema")


    else:
      print("opcion invalida. elegi la opcion 1-5")    



