def pedir_precio():
    precio = input("Ingrese el valor del producto, sin centavos ")
        
    while precio == "" or not precio.isdigit():
        print("El precio debe ser un numero entero, sin centavos. ")
        precio = input("Ingrese el valor del producto, sin centavos ")
        
    return int(precio)