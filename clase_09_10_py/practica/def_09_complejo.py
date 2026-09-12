"""
Consigna:
Crear un programa que simule un objetivo de ahorro.

Requisitos:
- Pedir al usuario un objetivo de ahorro, por ejemplo 50000.
- Luego pedir depósitos uno por uno.
- No aceptar depósitos negativos ni vacíos.
- Acumular los depósitos válidos.
- Mostrar después de cada depósito cuánto falta para llegar al objetivo.
- Cuando el ahorro acumulado llegue o supere el objetivo, mostrar "Objetivo alcanzado".
- Mostrar cuántos depósitos válidos se realizaron.
"""

import re

deposito_acumulado = 0
contador_depositos = 0
mensaje_invalido = " | ESTADO: ❌ Ingreso no valido" 

print("="*50)
print ("=== OBJETIVO DE AHORRO ===")
print("="*50)
print("")
 
ingreso_futuro_ahorro = input("Ingresa la Cantidad de DINERO que Deseas Ahorrar: $")
if re.match(r"^[1-9][0-9]*$",ingreso_futuro_ahorro): 
    ahorro_ingresado = int(ingreso_futuro_ahorro)
    
    for dinero_a_ingresar in range (1000):    
        dinero_a_ingresar = input("Ingresa la cantidad de Dinero a Depositar: $") 
        
        if not re.match(r"^[1-9][0-9]*$",dinero_a_ingresar):
            print(mensaje_invalido)
            continue
            
        deposito_acumulado += int(dinero_a_ingresar)
        contador_depositos += 1
         

        if  deposito_acumulado >= ahorro_ingresado:
            print("Objetivo alcanzado" "✅")
            break
        
        
        resultado_ahorro = (ahorro_ingresado - deposito_acumulado)        

        if deposito_acumulado < ahorro_ingresado:
            print(f"Te faltan: ${resultado_ahorro}")
            print("-"*40)
            print(f"Ingresaste: {contador_depositos} cant de Deposito/s Valido/os✅")
            print("\nVolve a ingresar DINERO para tus deposito/os y cunplir tu Objetivo de Ahorro")  
    
    