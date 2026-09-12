# ------------------------------------------------------------
# Ejercicio complejo 3: Análisis de temperaturas
# ------------------------------------------------------------
"""
Consigna:
Dada la lista temperaturas = [22, 25, 19, 30, 28, 18, 24], analizar los datos usando while.

Requisitos:
- Recorrer la lista con un índice.
- Calcular la suma total de temperaturas.
- Calcular el promedio.
- Encontrar la temperatura más alta.
- Encontrar la temperatura más baja.
- Contar cuántas temperaturas fueron mayores o iguales a 25.
- Mostrar un resumen final.
"""
temperaturas = [22, 25, 19, 30, 28, 18, 24]

def calcular_estadisticas(temperaturas):
    """funcion que calcula promedio/suma/temp alta / temp baja / y temp mayor a 25"""
    suma = sum(temperaturas)
    maxima = max(temperaturas)
    minima = min(temperaturas)
    promedio = float (suma / len(temperaturas))
    contador_temperatura = 0
    for temperatura in temperaturas:
    
        if temperatura >= 25:
            contador_temperatura += 1
    return (suma, maxima, minima, promedio, contador_temperatura)


def mostrar_reporte(temperaturas,suma, maxima, minima, promedio, contador_temperatura):
        
        """funcion que muestra promedio/suma/temp alta / temp baja / y temp mayor a 25"""
        print("\n" + "=" * 30)
        print(f"{'Índice_Temp':<10} | {'Dato_Temp':<20}")
        print("-" * 30)
        for i, temp in enumerate(temperaturas):
            print(f"{i:<10} | {temp:<20}")
            print("=" * 30)
        print(f"total suma de temperaturas: {suma}°C")
        print(f"total promedio de temperaturas: {promedio:.2F}°C")
        print(f"total cantidad de temperaturas MAYOR A 25°C: {contador_temperatura}")
        print(f"total temperatura mas alta : {maxima}°C")
        print(f"total temperatura mas baja : {minima}°C")
        print("-" * 50)

suma_total, max_temp, min_temp, prom, calurosos = calcular_estadisticas(temperaturas)
mostrar_reporte(temperaturas, suma_total, max_temp, min_temp, prom, calurosos)

