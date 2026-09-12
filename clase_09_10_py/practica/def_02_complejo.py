# ------------------------------------------------------------
# Ejercicio complejo 2: Registro de gastos
# ------------------------------------------------------------
"""
Consigna:
Crear un programa que registre gastos hasta que el usuario escriba 0.

Requisitos:
- Pedir importes de gastos uno por uno.
- Si el usuario ingresa 0, terminar la carga.
- Si ingresa un número negativo, mostrar un error y volver a pedir el dato.
- Acumular el total de gastos válidos.
- Contar cuántos gastos válidos se ingresaron.
- Al final, mostrar:
  - Total gastado.
  - Cantidad de gastos cargados.
  - Promedio de gasto, solo si se cargó al menos un gasto.

import re
from tabulate import tabulate
def registro_gastos():
    print("=== REGISTRO DE GASTOS CONTABLES ===")
    
    total_gastado = 0
    cantidad_gastos = 0
    
    while True:
        # 1. Pedimos el importe y limpiamos los espacios
        texto = input("💵 Ingresá el importe del gasto (0 para terminar): ").strip()
        
        # 2. El Patrón: Solo acepta números enteros (con o sin el signo menos)
        if re.match(r"^-?\d+$", texto):
            gasto = int(texto)
            
            # 3. Condición de corte (Si es 0, terminamos)
            if gasto == 0:
                break
                
            # 4. Condición de error (Si es negativo, avisamos y no sumamos)
            elif gasto < 0:
                print("⚠️ Error: El importe no puede ser un número negativo. Volvé a intentar.")
                
            # 5. Camino feliz (Si es positivo, acumulamos y contamos)
            else:
                total_gastado += gasto
                cantidad_gastos += 1
                
        else:
            print("⚠️ Error: Por favor, ingresá solo números enteros válidos.")

    # --- Resumen Final ---
    if cantidad_gastos > 0:
            
            promedio = total_gastado / cantidad_gastos
              
    lista_registro_promedio = [

            [f"{total_gastado}","{cantidad_gastos}"],f"{promedio:.2f}"
    ]
    headers = [ "💰 Total Gastado" ,  " 📋 Cantidad Gastado","⚖️ Promedio"]  
    print(tabulate(lista_registro_promedio, headers=headers,tablefmt="grid"))
    print("\n" + "="*40)
    print("📊 RESUMEN FINAL DE GASTOS")
    print("="*40)
    else:
        print("ℹ️ No se registraron gastos para procesar.")
    
   
    print(f"⚖️ Promedio por gasto: ${promedio:.2f}")
    print 
    
    
    print(f"💰 Total gastado: ${total_gastado}")
    print(f"📋 Cantidad de gastos cargados: {cantidad_gastos}")
    
    # 6. Promedio solo si se cargó al menos un gasto
   registro_gastos()
"""
import re
from tabulate import tabulate

def registro_gastos():
    print("=== REGISTRO DE GASTOS CONTABLES ===")
    
    total_gastado = 0
    cantidad_gastos = 0
    
    while True:
        # 1. Pedimos el importe y limpiamos los espacios
        texto = input("💵 Ingresá el importe del gasto (0 para terminar): ").strip()
        
        # 2. El Patrón: Solo acepta números enteros
        if re.match(r"^-?\d+$", texto):
            gasto = int(texto)
            
            # 3. Condición de corte
            if gasto == 0:
                break
                
            # 4. Condición de error
            elif gasto < 0:
                print("⚠️ Error: El importe no puede ser un número negativo. Volvé a intentar.")
                
            # 5. Camino feliz
            else:
                total_gastado += gasto
                cantidad_gastos += 1
                
        else:
            print("⚠️ Error: Por favor, ingresá solo números enteros válidos.")

    # --- Resumen Final ---
    print("\n" + "="*40)
    print("📊 RESUMEN FINAL DE GASTOS")
    print("="*40)

    if cantidad_gastos > 0:
        promedio = total_gastado / cantidad_gastos
          
        # 6. LA SOLUCIÓN: Una sola lista interna con los 3 datos separados por comas
        lista_registro_promedio = [
            [f"💰 {total_gastado}", f"📋 {cantidad_gastos}", f"⚖️ {promedio:.2f}"]
        ]
        
        headers = ["Total Gastado", "Cantidad Gastos", "Promedio"]  
        print(tabulate(lista_registro_promedio, headers=headers, tablefmt="grid"))
    else:
        print("ℹ️ No se registraron gastos para procesar.")

registro_gastos()