# open("nombre_archivo.txt", modo)

# r -> only read
# w -> only write
# a -> append , agregar al final (no borra contenido previo)
# r+ -> read and write combinados
"""
archivo = open("nombres.txt", "w") # si no existe lo crea

archivo.write("Maria\n")
archivo.write("Leo\n")
archivo.write("Mariano\n")
archivo.write("Babul\n")

archivo.close()

archivo = open("nombres.txt", "a") # agregar al final

archivo.write("Babul2\n")
archivo.write("Leo2\n")
archivo.write("Mariano2\n")
archivo.write("Babul3\n")

archivo.close()

archivo = open("nombres.txt", "r") # solo lee ver que pasa si no existe el archive
#contenido = archivo.read()
contenido = archivo.readlines() # tal cual
print(contenido) # con el for le saco espacios
for linea in contenido:
    print(linea.strip())
archivo.close()
# try - except
try:
    archivo = open("archivo_no_existe.txt", "r") 
    contenido = archivo.read()
    print(contenido)
    archivo.close()
except FileNotFoundError:
    print("verifica el nombre del archivo")    


entradas = [
    ("10" , "2"),
    ("10" , "0"),
    ("Hola" , "2")
]

for num_str, den_str in entradas:
    try:
        numerador = float(num_str)
        
        denominador = float(den_str)
        
        resultado = numerador / denominador
        
        print (f"Resultado: {resultado}")

    except ValueError:
        print(" Ingrese valores numericos ")    
    except ZeroDivisionError:
        print(" No se puede dividr por (0) cero")    

print("verifica el nombre del archivo")            
"""

