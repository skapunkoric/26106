
nombre = input("ingrese nombre: ").strip().title()
apellido = input("ingrese su apellido: ").strip().title()
mensaje = f"{nombre} {apellido}"
email = input("Ingrese su email: ").strip()
edad_ingresada = input("ingrese se Edad:  ").strip()
edadValidada = 0
if edad_ingresada.isdigit() and int(edad_ingresada) > 0:
        edadValidada=int(edad_ingresada)
else:
    print("error de edad")

email_valido = "@" in email and email.count("@") == 1
if not email_valido:
    print("su mail es incorrecto contiene mas de 1 un arroba @")

if edadValidada>0:
    if edadValidada < 15:
        categoria= "Niño/ña"
        

    elif 15 <= edadValidada < 18:
        categoria = "Adolescente"

    else:
       categoria = "Adukto/a"
       

print(f"{mensaje} y es: {categoria}")
                





