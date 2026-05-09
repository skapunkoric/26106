lista_frutas = ["manzana", "banana", "cereza", "durazno"]
indice = 0

while indice < len(lista_frutas):
    print("")            
    print(f"==[elemento: {indice}] | fruta:[{lista_frutas[indice]}]")   
    indice +=1

print("=-------lista de frutas=-----")
print(f"{lista_frutas}")

#nivel pro
lista_frutas = ["manzana", "banana", "cereza", "durazno"]
reporte_de_Frutas_acumulado = ""
indice = 0

while indice < len(lista_frutas):
    
    frutas_por_renglon =f"==[elemento: {indice}] | fruta:[{lista_frutas[indice]}]"   
    indice +=1
    reporte_de_Frutas_acumulado += frutas_por_renglon + "\n"

    
print(reporte_de_Frutas_acumulado)
print("=-------lista de frutas=-----")
print(f"{lista_frutas}")