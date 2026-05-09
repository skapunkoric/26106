"""""
texto = "Hola"

texto[0] = "J"

print({texto})

texto = "Python"

if "P" in texto and texto.endswith("on"):

    print("Condición cumplida.")

else:

    print("Condición no cumplida.")

nombre = "Ana"

saludo = f"Hola, {nombre}!"

print(saludo)

# Observá el siguiente código. ¿Qué mensaje se imprime si el ingreso mensual es 60000 y la edad es 25?

ingreso = 80000

edad = 25

if ingreso < 50000:

    print("Ingresos bajos.")

elif edad < 30:

    print("Joven con buenos ingresos.")

else:

    print("Adulto con buenos ingresos.")
"""
#Observá el siguiente código. ¿Qué pasará si el usuario ingresa un valor no numérico?


edad = int(input("Ingresá tu edad: "))

if edad < 18:

    print("Sos menor de edad.")

else:

    print("Sos mayor de edad.")


