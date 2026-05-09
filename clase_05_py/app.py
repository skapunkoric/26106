# while bucle
"""""
contador = 1
while contador <= 5:
   print(f"Este es el intento número {contador}.")
   contador += 1
nombre = ""

while nombre == "":
   nombre = input("Ingresá tu nombre: ").strip()
   if nombre == "":
       print("El nombre no puede estar vacío. Intentá de nuevo.")

print(f"¡Hola, {nombre}! Gracias por ingresar tu nombre.")

numero = 0

while numero <= 5:
    print(f"este es le intento {numero}")

    numero = numero + 1



salir = input("Ingresá 'salir' para terminar el programa ").strip().lower()
while salir != "salir":
     print("Debe colocar 'salir")
     salir = input("debe ingresar 'salir' para terminar el programa ").strip().lower()

salir = input("Ingresá 'salir' para terminar el programa ").strip().lower()
while salir != "salir":
     print("Debe colocar 'salir")
     salir = input("debe ingresar 'salir' para terminar el programa ").strip().lower()

while True:
     respuesta = input("Ingresá 'salir' para terminar el programa ").strip().lower()

     if respuesta == 'salir':
        break
     else:
         print("debes colocar 'salir: ")
    
    print("finaliza el programa")     


# listas[]
lista_numeros = [10,20,30,40,40]
lista_nombres = ["ana","juan","maria","alfredo"]
mixta = [1,"dos",3.14,True,[1,2,3]]
vacia = []

print(mixta[2])
print(mixta[4] [1])
print(lista_nombres[-4])

print(len(lista_numeros))
indice = 0

while indice < len(lista_numeros):
    print(f"indice: {indice} / elemento {lista_numeros[indice]}")
    indice +=1      


lista_numeros = [10,20,30,40,40]

indice = int(input("indice; "))

if  indice < len(lista_numeros):
    print(f"indice: {indice} ; elemento {lista_numeros[indice]}")
    indice += 1
else:
    print("no hay elementos en este " + indice)  

"""
numeros_entrada = [10,-1,,40,40]
numero = numero_entrada[indice]


indice = int(input("indice; "))

if  indice < len(lista_numeros):
    print(f"indice: {indice} ; elemento {lista_numeros[indice]}")
    indice += 1
else:
    print("no hay elementos en este " + indice)            
          

