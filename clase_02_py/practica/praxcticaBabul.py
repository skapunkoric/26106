"""""
# Solicitud de datos al usuario
nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
edad = input("Ingresa tu edad: ")
correo = input("Ingresa tu correo electrónico: ")

# Mostrar la tarjeta de presentación
print("\n" + "-" * 30)
print("  TARJETA DE PRESENTACIÓN")
print("-" * 30)
print(f"Nombre Completo: {nombre} {apellido}")
print(f"Edad:            {edad} años")
print(f"Email:           {correo}")
print("-" * 30)


# Solicitud de datos al usuario
nombre = input("Ingresa tu nombre: ")
#apellido = input("Ingresa tu apellido: ")
#edad = input("Ingresa tu edad: ")
#correo = input("Ingresa tu correo electrónico: ")

# Mostrar la tarjeta de presentación
print("\n" + "-" * 30)
print("  TARJETA DE PRESENTACIÓN")
print("-" * 30)
print(f"Nombre Completo: {nombre} ")
#print(f"Nombre Completo: {nombre} {apellido}")
#print(f"Edad:            {edad} años")
#print(f"Email:           {correo}")
print("-" * 30)

# Datos (puedes usar los input anteriores)
nombre = "Mili"
apellido = "Pérez"
edad = "25"
correo = "mili@example.com"

# Definimos el ancho de la tarjeta
ancho = 40
separador = "-" * ancho

print(separador)
print(f"| {'TARJETA DE PRESENTACIÓN':^{ancho-4}} |") # Centrado con ^
print(separador)
print(f"| Nombre: {nombre} {apellido:<{ancho-18}} |") # Alineado a la izquierda
print(f"| Edad:   {edad:<{ancho-18}} |")
print(f"| Email:  {correo:<{ancho-18}} |")
print(separador)
"""""
nombre = "Babul"
apellido = "Tolentino"
edad = "47"
correo = "babul@babul.com"

# Definimos un ancho total para la tarjeta
ancho_total = 40
# Definimos un ancho fijo para la columna de las etiquetas (Nombre, Edad, etc.)
ancho_etiqueta = 3

separador = "-" * ancho_total

print(separador)
print(f"| {'TARJETA DE PRESENTACIÓN':^{ancho_total-4}} |")
print(separador)

# Usamos :< para alinear a la izquierda con un ancho fijo
print(f"| { 'Nombre:':<{ancho_etiqueta}} {nombre} {apellido:<{ancho_total - ancho_etiqueta - 12}} |")
print(f"| { 'Edad:':<{ancho_etiqueta}} {edad + ' años':<{ancho_total - ancho_etiqueta - 4}} |")
print(f"| { 'Email:':<{ancho_etiqueta}} {correo:<{ancho_total - ancho_etiqueta - 5}} |")

print(separador)