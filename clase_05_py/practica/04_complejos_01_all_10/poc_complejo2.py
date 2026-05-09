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
acumulaGastos = 0.00
contadorGastos= 0

while True:
    gastoIngresado= input("Ingresá tus gastos (ó 0 para salir): ").strip().replace(",",".")
    if gastoIngresado.replace(".", "",1).isdigit():
        gastoReal= float(gastoIngresado)
        if gastoReal == 0:
         break
        elif  gastoReal>0:
            acumulaGastos +=gastoReal
            contadorGastos += 1     
            promedioDeGastos = acumulaGastos/contadorGastos
            #print(f"Total Cargado: ${acumulaGastos:.2f}")
            

                            
        else:
            print(f"error el gasto debe ser mayor a cerp")

    else:
        print(f"no es numero valido")       
print(f"---RESUMEN DE GASTOS-----")        
if contadorGastos>0:
     
     print(f"Total Gastado: ${acumulaGastos:.2f}")
     print(f"Cantidad de Gastos cargados: {contadorGastos}")
     print(f"Promedio de Gastos cargados: ${promedioDeGastos:.2f}")      
          
else:
    print(f"no cargaste nada, vuelve pronto")
    



      
    
    

        
    
        

    

