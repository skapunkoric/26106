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
import re
from tabulate import tabulate

def pedir_numero(mensaje):
    numero_validado = 0
    while numero_validado == 0:
        texto = input(mensaje).strip() 
        if re.match(r"^[1-9]\d*$", texto):
            numero_validado = int(texto)
        else:
            print("⚠️ Error: Por favor, ingresá un monto numérico entero y mayor a cero.")
            
    return numero_validado

def simulador_ahorro():
    ingreso_ahorro = pedir_numero("\n🎯 Ingresá tu meta total de ahorro: $")
    deposito_acumulado = 0
    nro_deposito = 1
    historial_depositos = []

    
    while deposito_acumulado < ingreso_ahorro:            
        deposito_actual = pedir_numero(f"\n💸 Ingresá el monto a depositar #{nro_deposito}: $")
        deposito_acumulado += deposito_actual
        
        
        historial_depositos.append([nro_deposito, f"${deposito_actual}", f"${deposito_acumulado}"])

        faltante = ingreso_ahorro - deposito_acumulado
        
        if faltante > 0:
            print(f"Llevás ahorrado ${deposito_acumulado} (Te faltan ${faltante})")

        
        nro_deposito += 1
    
    print(f"\nTotal ahorrado: ${deposito_acumulado} (Tu meta era de ${ingreso_ahorro})")
    
    headers = ["Nro. Depósito", "Monto Ingresado", "Total Acumulado"]
    print("\n" + tabulate(historial_depositos, headers=headers, tablefmt="grid"))

simulador_ahorro()