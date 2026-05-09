"""""
# ao vivop 9/4/2026

resultado = 5 == 5
print(f"5==5: {resultado}")
print("5==5 :" , resultado)
print("5==5 :  + resultado")

resultado1 = 4 == 5
print(f"4==5: {resultado1}")

# resultado = 10 > 

numero = 5
if numero > 0:
    print(f"el numero {numero} es positivo")


numero1 = 5
if numero1 > 10:
    print(f"el numero {numero1} es positivo")    

numero2 = 5

if numero2 > 10:
    print(f"el numero {numero2} es positivo")           
else:
    print(f"el numero {numero2} no es positivo")           
    
es_ciudadano = True

if edad >= 18 and es_ciudadano:
    print(f"Con {edad} años y siendo ciudadano , PUEDES VOTAR")           
else:
    print(f"NO CUMPLLES CON LOS REQUISITOS , NO PUEDES VOTAR")   
"""

nombre= input("ingrese su nombre")        
apellido= input("ingrese su apellido")        
edad= int (input("ingrese su edad"))

if nombre == "" and apellido == "" and edad == "":
   print("no debe ser vacio los datos ingresados")

email = input("ingrese su email")
if '@' not in email:
   print("debes colocar un mail")