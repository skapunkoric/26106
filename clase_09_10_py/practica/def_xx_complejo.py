import re
from tabulate import tabulate

patron_estricto = r"^[0-9]+(\.[0-9]+)?$"
acumulaGastos = 0.0
contadorGastos= 0

def ingreso_(msg):
    while True:
        gastoIngresado = input("Ingresá tus gastos (ó 0 para salir): ").strip()
            if re.match(gastoIngresado):
                gastoReal = float(gastoIngresado)
            elif gastoIngresado == 0:
                break
            else:
             print(f"error el gasto debe ser mayor a cerp")

    acumulaGastos += gastoReal
    contadorGastos += 1

    print(f"   ✅ Sumado: ${gastoReal:.2f}")
    print("\n" + "=" * 25)
    print("     RESUMEN DE GASTOS")
    print("=" * 25)
    if contadorGastos > 0:
    promedioDeGastos = acumulaGastos / contadorGastos
    print(f"Total Gastado: ${acumulaGastos:.2f}")
    print(f"Cantidad de Gastos cargados: {contadorGastos}")
    print(f"Promedio de Gastos cargados: ${promedioDeGastos:.2f}")
else:
    print(f"no cargaste nada, vuelve pronto")

print("📋 REGISTRO DE GASTOS tipo BILLETERA VIRTUAL")
print("-" * 40)
headers = ["Producto", "Cantidad", "Estado"]
    print(tabulate(datos_tabla, headers=headers, tablefmt="grid"))