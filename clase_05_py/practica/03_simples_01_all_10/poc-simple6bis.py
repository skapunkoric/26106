"""
Consigna:
Dada la lista frutas = ["manzana", "banana", "cereza", "durazno"], mostrar cada fruta usando while.

Requisitos:
- Usar una variable indice que empiece en 0.
- Usar len(frutas) en la condición del while.
- Mostrar cada elemento accediendo con frutas[indice].
"""

lista_frutas = ["manzana", "banana", "cereza", "durazno"]

indice = 0

while indice < len(lista_frutas):
    
    print(f"==[elemento: {indice}] | fruta:[{lista_frutas[indice]}]")   
    indice +=1

print("=-------lista de frutas=-----")
print(f"{lista_frutas}")