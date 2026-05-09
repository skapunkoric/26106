"""""
edad = 15
if edad < 13:
    print("es menor")
elif edad >= 13 and edad < 18:
    print("es adolescente")
else:
    print("es Adulto")    

notas = 10
if notas ==  0:
    print()
elif notas < 5:
    print()
elif notas > 5:
    print()
"""""
#fruta = "Manzana" 

fruta = input("ingrese su fruta")
match fruta:
        case "Manzana":  
            print("Roja o Verde")
        case "Pera":  
            print("Es Amarilla")
        case "Naranja":  
            print("Es Naranja")    
        case _:
            print("DESCONOCIDO / unknow")    

            




