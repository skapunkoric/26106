
    
def pedir_texto(mensaje , mensaje_error):
    dato = input(mensaje)
    
    while dato == "":
        print(mensaje_error)
        dato = input(mensaje)
        
    return dato