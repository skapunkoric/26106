"""""
contador = 1
while contador <= 10:
    print(contador)
    if contador==5:
 
 #contador +=1  (mas pro)
 #contador = contador + 1   ( for dummies)
"""

password = "python26106"
intentos = 0
max_intento = 3
acceso_permitido = False
while intentos < max_intento:
    passowrd_Ingresado = input("ingrese su contraseña o password: ")
    if passowrd_Ingresado == password:
        print("acceso permitido")
        acceso_permitido = True
        break

    intentos +=1 
    intentos_restantes = max_intento - intentos
    print(f"contraseña incorrecta. Te quedan {intentos_restantes} intentos")

    if not acceso_permitido:
        print ("acceso bloqueado")





