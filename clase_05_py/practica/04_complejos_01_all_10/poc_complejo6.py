# ------------------------------------------------------------
# Ejercicio complejo 6: Menú interactivo
# ------------------------------------------------------------
"""
Consigna:
Crear un menú que se repita hasta que el usuario elija salir.

Opciones:
1 - Saludar
2 - Mostrar los números del 1 al 5
3 - Mostrar una lista de cursos
4 - Salir

Requisitos:
- Usar while para mantener el menú activo.
- Si elige 1, mostrar un saludo.
- Si elige 2, usar otro while para mostrar los números del 1 al 5.
- Si elige 3, recorrer una lista de cursos con while.
- Si elige 4, mostrar "Programa finalizado" y terminar.
- Si elige otra opción, mostrar "Opción inválida".

Conceptos a practicar:
while, menú, condicionales, listas, bucles anidados simples.
"""
cursos=["Introduccion a Python","Java","IA Inteligencia Artificial"]
numero = 1
indice= 0
lista_Numerica =[]
while True:
    print("\n==== Opciones: ====")
    print("*"*30)
    print("1 - Saludar ")
    print("2 - Mostrar los números del 1 al 5") 
    print("3 - Mostrar una lista de cursos")
    print ("4 - Salir")
    print("*"*30)
    opcion = input("\nSelecione su opcion: ")
 
    if opcion.isdigit():
        opcion = int(opcion)
        match opcion:
            case  1:
                print ("\n>>>>>>...Hola Bienvenido/a ......")
                input(f"\nPresioná Enter para volver al menú...")

            case 2:
                while numero <=5:
                    lista_Numerica.append(numero)
                    numero+=1
                print("\n>>> Procesando números...")
                print(".........numeros del 1 al 5...........")
                print(f"La lista numerica es :{lista_Numerica}")
                input(f"\nPresioná Enter para volver al menú...")

            case 3:
                while indice>len(cursos):
                    indice +=1          
                print(f"Los cursos disponibles son:{cursos}")
                input(f"\nPresioná Enter para volver al menú...")

            case 4:
                print ("\n..PROGRAMA Finalizado ....")             
                break
            
            case _:
                print("\n[!] Opcion invalida. Elige una opción del 1 al 4.")
                input("\nPresioná Enter para volver al menú...")
    else:
        print("\n[!] Error: Por favor, ingresa solo números.")
        print (".........OPCION INVALIDA ....")
        input(f"\nPresioná Enter para volver al menú...")

