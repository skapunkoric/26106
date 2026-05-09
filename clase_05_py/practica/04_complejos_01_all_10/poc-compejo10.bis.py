

lista_de_Puntajes = [450, 900, 1200, 300, 750, 1200, 100]
puntaje_Maximo = lista_de_Puntajes[0]
puntaje_Minimo = lista_de_Puntajes[0]
contador_de_puntaje_maximo =0
suma_de_Puntajes =0
promedio_de_Puntajes = 0.0
contador_de_Mayor_a_800 = 0
lista_de_Puntajes_Mayor_a_800 = []
indice = 0

while indice < len(lista_de_Puntajes):
    lista_de_puntaje = lista_de_Puntajes[indice]
 
    if lista_de_puntaje>puntaje_Maximo:
        puntaje_Maximo = lista_de_puntaje
        contador_de_puntaje_maximo += 1
        
 
    if lista_de_puntaje<puntaje_Minimo:
        puntaje_Minimo = lista_de_puntaje

    if lista_de_puntaje>= 800:
        contador_de_Mayor_a_800 += 1
        lista_de_Puntajes_Mayor_a_800.append(lista_de_puntaje)
 
 
    suma_de_Puntajes += lista_de_puntaje
    promedio_de_Puntajes = suma_de_Puntajes / len(lista_de_Puntajes)

    indice += 1

print({puntaje_Maximo}) 
print({puntaje_Minimo}) 
print(promedio_de_Puntajes)
print({contador_de_Mayor_a_800})
print(lista_de_Puntajes_Mayor_a_800) 
print({contador_de_puntaje_maximo})