"""""
1) Solicite al cliente su nombre, apellido, edad y correo electrónico.
2) Compruebe que el nombre, el apellido y el correo no estén en blanco, y que la edad sea mayor de 18 años.
3) Muestre los datos por la terminal, en el orden que se ingresaron. 
Si alguno de los datos ingresados no cumple los requisitos, sólo mostrar el texto “ERROR!”.
"""

nombre = input("ingrese su nombre: ")
apellido =input("ingrese su apellido: ")
edad=int(input("ingrese su edad (debe ser numerico): "))
correo=input ("ingrese su correo electronico: ")

if edad and apellido and edad.is_integer():
    print(f"su nombre es:  {nombre} y su apellido es: {apellido} y su edad:  {edad}")

else: 
    print ("ERROR")



