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

Conceptos a practicar:
while, acumulador, contador, validaciones, break o condición centinela.
"""
import re
patron_estricto = r"^[0-9]+(\.[0-9]+)?$"
acumulaGastos = 0.0
contadorGastos= 0
print("📋 REGISTRO DE GASTOS tipo BILLETERA VIRTUAL")
print("-" * 40)

for i in range (100):

    gastoIngresado= input("Ingresá tus gastos (ó 0 para salir): ").strip()
    if re.match(patron_estricto,gastoIngresado):
        gastoReal= float(gastoIngresado)
        if gastoReal == 0:
         break
        acumulaGastos +=gastoReal
        contadorGastos += 1
        print(f"   ✅ Sumado: ${gastoReal:.2f}")

    else:
            print(f"error el gasto debe ser mayor a cerp")

print("\n" + "=" * 25)
print("     RESUMEN DE GASTOS")
print("=" * 25)

if contadorGastos>0:
     promedioDeGastos = acumulaGastos / contadorGastos
     print(f"Total Gastado: ${acumulaGastos:.2f}")
     print(f"Cantidad de Gastos cargados: {contadorGastos}")
     print(f"Promedio de Gastos cargados: ${promedioDeGastos:.2f}")
     print("-" * 25)
          
else:
    print(f"no cargaste nada, vuelve pronto")
    



      
    
    

        
    
        

    

