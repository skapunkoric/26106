# ------------------------------------------------------------
# Ejercicio complejo 9: Simulador de ahorro
# ------------------------------------------------------------
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

Conceptos a practicar:
while, acumulador, contador, validación, condición de corte.
"""
deposito_Acumulado = 0
objetivo_alcanzado = False
deposito_de_Dinero = 0
contador_de_Depositos = 0
mensajeInvalido = " | ESTADO: ❌ Ingreso no valido" 
ahorro_ingresado = 0
print("="*50)
print ("=== OBJETIVO DE AHORRO ===")
print("="*50)
print("")

while True:
    if ahorro_ingresado == 0:
        ingreso_futuro_ahorro = input("Ingresa la Cantidad de DINERO que Deseas Ahorrar: $")
        if ingreso_futuro_ahorro.isdigit() and int(ingreso_futuro_ahorro) >0: 
           ahorro_ingresado = int(ingreso_futuro_ahorro)
        
        else:
            print(mensajeInvalido) 
        
        continue 
    
    dinero_a_Ingresar = input("Ingresa la cantidad de Dinero a Depositar: $") 
    
    if not dinero_a_Ingresar.isdigit():
        print(mensajeInvalido)  
        continue
    
    deposito_de_Dinero = int(dinero_a_Ingresar)
    deposito_Acumulado += deposito_de_Dinero
    resultado_de_Ahorro = (ahorro_ingresado - deposito_Acumulado)
    contador_de_Depositos += 1
    
    if  deposito_Acumulado >= ahorro_ingresado:
        objetivo_alcanzado = True
        print("Objetivo alcanzado" "✅") 
        break
     
    else:
        print(f"Te faltan: ${resultado_de_Ahorro}")
        print("-"*40)
        print(f"Ingresaste: {contador_de_Depositos} cant de Deposito/s Valido/os✅")
        print("\nVolve a ingresar DINERO para tus deposito/os y cunplir tu Objetivo de Ahorro")   

