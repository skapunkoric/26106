
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
import sys  # Lo usamos para simular un bucle infinito limpio

print("=" * 50)
print(f"{'=== OBJETIVO DE AHORRO ===':^50}")
print("=" * 50)

# 1. Pedimos la meta de ahorro (Validación simple sin 're')
ingreso_meta = input("Ingresa la cantidad de DINERO que deseas ahorrar: $")
if not ingreso_meta.isdigit() or int(ingreso_meta) <= 0:
    print("❌ Monto de objetivo inválido. Fin del programa.")
    sys.exit()  # Frenamos si mete cualquiera

meta_ahorro = int(ingreso_meta)
deposito_acumulado = 0
contador_depositos = 0

print("\n" + "-" * 50)
print(f"{'REGISTRO DE DEPÓSITOS':^50}")
print("-" * 50)

# La única forma pro de usar un for acá es usar un rango tan grande que sea imposible de alcanzar (infinito práctico)
# y manejar el flujo nosotros con break.
for _ in range(99999999):

    print(f"\n[Depósito N° {contador_depositos + 1:02d}]")
    monto_ingresado = input("-> Cantidad a depositar: $")

    # Validación del depósito
    if not monto_ingresado.isdigit() or int(monto_ingresado) <= 0:
        print("  ❌ ESTADO: Ingreso no válido. Intenta de nuevo.")
        continue

    monto = int(monto_ingresado)
    deposito_acumulado += monto
    contador_depositos += 1

    # Calculamos cuánto falta
    faltante = meta_ahorro - deposito_acumulado

    # REPORTE DE ESTADO EN REGISTRO
    print(f"  💰 Acumulado: ${deposito_acumulado:<10} | 📅 Total Depósitos: {contador_depositos:02d}")

    # Control del Objetivo
    if deposito_acumulado >= meta_ahorro:
        print("\n" + "=" * 50)
        print(" 🎉 ¡OBJETIVO ALCANZADO CON ÉXITO! ✅")
        print(f" Total Ahorrado: ${deposito_acumulado} (Meta: ${meta_ahorro})")
        print(f" Lo lograste en {contador_depositos} depósitos válidos.")
        print("=" * 50)
        break
    else:
        print(f"  📉 Te faltan : ${faltante}")
        print("-" * 50)