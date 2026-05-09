#poc

nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
edad = input("Ingresa tu edad: ")
correo = input("Ingresa tu correo electrónico: ")

# Definimos un ancho total para la tarjeta
ancho_total = 40

# Definimos un ancho fijo para la columna de las etiquetas (Nombre, Edad, etc.)
ancho_etiqueta = 3

separador = "-" * ancho_total

print(separador)
print(f"| {'TARJETA DE PRESENTACIÓN':^{ancho_total-4}} |")
print(separador)

# Usamos :< para alinear a la izquierda con un ancho fijo
print(f"| { 'Nombre:':<{ancho_etiqueta}} {nombre} {apellido:<{ancho_total - ancho_etiqueta }} |")
print(f"| { 'Edad:':<{ancho_etiqueta}} {edad + ' años':<{ancho_total - ancho_etiqueta }} |")
print(f"| { 'Email:':<{ancho_etiqueta}} {correo:<{ancho_total - ancho_etiqueta }} |")

print(separador)
