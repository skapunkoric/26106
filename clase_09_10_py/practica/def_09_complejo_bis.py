import re
from tabulate import tabulate
from colorama import init, Fore, Style

# Inicializamos los colores
init(autoreset=True)


def pedir_numero(mensaje):
    numero_validado = 0
    # Nuestro while limpio (sin True) para atrapar el número
    while numero_validado == 0:
        texto = input(mensaje).strip()  # ¡Acá sumamos los paréntesis!
        if re.match(r"^[1-9]\d*$", texto):
            numero_validado = int(texto)
        else:
            print(Fore.RED + "⚠️ Error: Por favor, ingresá un monto numérico entero y mayor a cero.")

    return numero_validado


def simulador_ahorro():
    print(Fore.CYAN + "=" * 50)
    print(Fore.CYAN + "=== OBJETIVO DE AHORRO ===")
    print(Fore.CYAN + "=" * 50)

    # 1. Pedimos la meta
    meta = pedir_numero("\n🎯 Ingresá tu meta total de ahorro: $")

    # 2. Preparamos nuestras variables (AFUERA del bucle)
    acumulado = 0
    nro_deposito = 1
    historial_depositos = []  # Acá vamos a guardar los cajones para "tabulate"

    # 3. El Bucle Arquitectónico (Puro y duro, sin while True)
    while acumulado < meta:
        # Usamos la función pidiendo el depósito
        deposito = pedir_numero(f"\n💸 Ingresá el monto de tu depósito #{nro_deposito}: $")

        # Sumamos la plata
        acumulado += deposito

        # Armamos el cajoncito para nuestra tabla final: [Nro, Deposito, Total Acumulado]
        historial_depositos.append([nro_deposito, f"${deposito}", f"${acumulado}"])

        # Le avisamos al usuario cómo viene
        faltante = meta - acumulado
        if faltante > 0:
            print(Fore.YELLOW + f"💰 Llevás ahorrado: ${acumulado} (Te faltan ${faltante} para la meta)")

        nro_deposito += 1

    # ==========================================
    # ZONA DE ÉXITO Y REPORTES
    # ==========================================
    print(Fore.GREEN + "\n" + "=" * 50)
    print(Fore.GREEN + f"🎉 ¡OBJETIVO ALCANZADO! ✅")
    print(Fore.GREEN + f"Total ahorrado: ${acumulado} (Tu meta era de ${meta})")
    print(Fore.GREEN + "=" * 50 + "\n")

    # Imprimimos el ticket final con tabulate
    headers = [Fore.MAGENTA + "Nro. Depósito", Fore.MAGENTA + "Monto Ingresado",
               Fore.MAGENTA + "Total Acumulado" + Style.RESET_ALL]
    print(tabulate(historial_depositos, headers=headers, tablefmt="grid"))


# Encendemos el motor principal
simulador_ahorro()