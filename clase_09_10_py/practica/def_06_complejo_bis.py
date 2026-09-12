# ------------------------------------------------------------
# Ejercicio 6: Menú interactivo (Versión DRY + Minimalista)
# ------------------------------------------------------------

cursos = ["Introduccion a Python", "Java", "IA Inteligencia Artificial"]


def saludo():
    print("\n👋 ¡Hola! Bienvenido/a al sistema.")


def menu():
    print("\n" + "=" * 20)
    print("      MENÚ")
    print("=" * 20)
    print("1 - Saludar")
    print("2 - Números 1 al 5")
    print("3 - Lista de cursos")
    print("4 - Salir")
    print("=" * 20)


def mostra_numeros():
    lista_numerica = []
    for i in range(1, 6):
        lista_numerica.append(i)
    print("\n>>> Procesando números...")
    print(f"Lista generada: {lista_numerica}")


def lista_cursos():
    print(f"\n📚 Cursos disponibles: {cursos}")


def finally_program():
    print("\n🔌 PROGRAMA FINALIZADO. ¡Adiós!")


def error():
    print("\n[!] Opción inválida. Elegí del 1 al 4.")


def error_dos():
    print("\n[!] Error: Ingresá solo números.")


# El Chef Controlador
def validacion_menu():
    while True:
        menu()
        opcion = input("\nSeleccione su opción: ").strip()

        if opcion.isdigit():
            opcion = int(opcion)
            match opcion:
                case 1:
                    saludo()
                case 2:
                    mostra_numeros()
                case 3:
                    lista_cursos()
                case 4:
                    finally_program()
                    break  # El break nos saca del while y ESQUIVA la pausa de abajo
                case _:
                    error()
        else:
            error_dos()

        # === LA MAGIA DRY ===
        # Este único input ataja a TODAS las opciones (1, 2, 3 y los errores)
        # antes de que el while vuelva a arrancar arriba.
        input("\n>> Presioná Enter para continuar...")


# ==========================================
# FLUJO PRINCIPAL
# ==========================================
validacion_menu()