""""
productos = ["manzana","narajas","bananas","peras"]
i =0

while i< len(productos):
    
    print(f"con WHILE: producots disponibles: {productos[i]}")
    i +=1

for producto in productos:
    
    print(f" CON FOR productos disponibles: {producto}")

produc_find = False
prod_buscado = input("ingrese el producto a buscar: ").strip().lower()
for fruta in productos:
    if fruta == prod_buscado:
        print("el producto encontrado es:",prod_buscado)
        produc_find = True
        break
if not produc_find:    
    print("el producto BUSCADO no esta en la lista",prod_buscado)
    
#  otra forma
produc_find = False
prod_buscado = input("ingrese el producto a buscar: ").strip().lower()
for fruta in productos:
    if fruta == prod_buscado:
     produc_find = True        
     break
if produc_find:
    print("el producto encontrado es:",prod_buscado)
else:
    print("el producto BUSCADO no esta en la lista",prod_buscado)

palabra = "Babul"
for letra in palabra:
    print(f"{letra}")

print("lo ultimo que guardo letra es como valor es," letra)    

#Range(fin)
for i in range (5):
    print(i)
#range(inicio,fin)
for num in range(3,8):
    print(num)
#range(inicio,fin,paso)
for i in range(0,10,2):
    print(i)
for i in range(10,0,-1):
    print(i)

productos = ["manzana","narajas","bananas","peras"]
print(len(productos))
for i in range(len(productos)):
    print(f"indice: {i} / {productos[i]}")

numeros = [10,20,30]
print(f"lista original")
print(numeros)
for i in range(len(numeros)):
    numeros[i] = numeros[i] * 2

print(f"lista modificada multi por 2")
print(numeros)
numeros = [10,20,30]
print(f"lista original")
print(numeros)
for i in range(1,len(numeros)):
    numeros[i] = numeros[i] * 30

print(f"lista modificada multi por 2")
print(numeros)
"""
lista_Numeros = []
print("vamos a cargas la lista con 5 numeros")
contador = 0
while contador <5:
    numero=int(input("ingrese la lista de numeros: "))
    lista_Numeros=lista_Numeros+[numero]
    contador = contador + 1
print("numeros ingresados")
print(lista_Numeros)
for i in range (len(lista_Numeros)):
    lista_Numeros[i] = lista_Numeros[i] * 20
print(lista_Numeros)    