# ------------------------------------------------------------
# Ejercicio complejo 3: Análisis de temperaturas
# ------------------------------------------------------------
"""""
Consigna:
Dada la lista temperaturas = [22, 25, 19, 30, 28, 18, 24], analizar los datos usando while.

Requisitos:
- Recorrer la lista con un índice. +
- Calcular la suma total de temperaturas. +
- Calcular el promedio.+
- Encontrar la temperatura más alta.+
- Encontrar la temperatura más baja.+
- Contar cuántas temperaturas fueron mayores o iguales a 25.+
- Mostrar un resumen final.+

Conceptos a practicar:
listas, índices, while, acumuladores, comparación de máximos y mínimos.
"""
#maxima = float('-inf') # El número más pequeño que existe
#minima = float('inf')  # El número más grande que existe
temperaturas = [22, 25, 19, 30, 28, 18, 24]
indice = 0
sumaTemperatura = 0
contadorTemperatura = 0
temperaturaMasAlta = temperaturas[0]
temperaturaMasBaja = temperaturas[0]
print() 
print("-" * 70)
print( " RESUMEN FINAL DE TEMPERATURAS " )
print("-" * 70)
print("lista de temperaturas con su corrrespondiente indice en la lista")
 
while indice<len(temperaturas):
    temperatura =  temperaturas[indice]
    print(f"indice: {indice} / temperatura: {temperaturas[indice]}°C") 
    sumaTemperatura += temperatura
    cantidadDeTemperaturas=len(temperaturas)
    indice += 1 
    if temperatura>=25:
        contadorTemperatura+= 1
    if  temperatura>temperaturaMasAlta:
          temperaturaMasAlta=temperatura
          
    if  temperatura<temperaturaMasBaja:
          temperaturaMasBaja=temperatura    
    
promedioDeTemperaturas = sumaTemperatura / cantidadDeTemperaturas    
print("-" * 70)
print(f"total suma de temperaturas: {sumaTemperatura}°C")
print(f"total promedio de temperaturas: {promedioDeTemperaturas:.2F}°C")
print(f"total cantidad de temperaturas MAYOR A 25°C: {contadorTemperatura}")
print(f"total temperatura mas alta : {temperaturaMasAlta}°C")
print(f"total temperatura mas baja : {temperaturaMasBaja}°C")
print("-" * 70)
        
"""
con ayuda de gemini
temperaturas = [22, 25, 19, 30, 28, 18, 24] # Proba dejarla vacía [] para testear

# 1. EL ESCUDO: Solo entramos si hay datos
if len(temperaturas) > 0:
    indice = 0
    sumaTemperatura = 0
    contadorTemperatura = 0
    
    # Inicialización segura (porque sabemos que al menos hay un elemento)
    temperaturaMasAlta = temperaturas[0]
    temperaturaMasBaja = temperaturas[0]
    
    print("-" * 30)
    print("PROCESANDO DATOS...")
    
    while indice < len(temperaturas):
        temperatura = temperaturas[indice]
        sumaTemperatura += temperatura
        
        # Lógica de máximos y mínimos
        if temperatura > temperaturaMasAlta:
            temperaturaMasAlta = temperatura
        if temperatura < temperaturaMasBaja:
            temperaturaMasBaja = temperatura
            
        # Conteo de temperaturas altas
        if temperatura >= 25:
            contadorTemperatura += 1
            
        indice += 1
    
    # Cálculos finales (afuera del while, adentro del if)
    promedio = sumaTemperatura / len(temperaturas)
    
    print(f"Máxima: {temperaturaMasAlta}°C")
    print(f"Mínima: {temperaturaMasBaja}°C")
    print(f"Promedio: {promedio:.2f}°C")
    print(f"Días calurosos: {contadorTemperatura}")

else:
    # 2. EL PLAN B: Qué pasa si la lista está vacía
    print("Error: No se encontraron registros de temperatura para procesar.")
"""      

