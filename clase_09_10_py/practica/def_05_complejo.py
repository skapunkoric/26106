# ------------------------------------------------------------
# Ejercicio complejo 5: Limpieza de lista con continue
# ------------------------------------------------------------
"""
Consigna:
Dada la lista datos = ["Ana", "", "Luis", "   ", "María", "Pedro", ""], crear una nueva lista solo con nombres válidos.

Requisitos:
- Recorrer la lista con while.+
- Usar strip() para limpiar espacios.+
- Si el dato queda vacío, ignorarlo usando continue.+
- Agregar los nombres válidos a una lista nueva llamada nombres_validos.+
- Mostrar la lista final.+
"""

def funcion1_limpia_nombre_vacios(dato):
    """
    recibe por parametro una lista de datos 
    recorre con un for de otra funcion
    y usa strip() para limpiar espacios.
    """
    dato_limpio = dato.strip()
    
    if dato_limpio != "":
        return dato_limpio
    else:
        return None

def funcion2_recorre_lista(lista_dato):

#recorre con un for una lista de datos y la recorre la lista 
    nombres_validos= []    
    for dato in lista_dato:
        resultado_lista =funcion1_limpia_nombre_vacios(dato)

        if resultado_lista is not None:
            nombres_validos.append(resultado_lista)
    return nombres_validos
         
def funcion3_mostrar_reporte_final(lista_datos,datos_nueva_lista):
    """muestra la lista en forma de funcion parametrizada"""
    print("*" * 60)
    print(f"Los datos ORIGINALES son: \n{lista_datos}")
    print("*" * 60)
    print(f"Los nuevos datos SIN ESPACIOS VACÍOS: \n{datos_nueva_lista}")
    print("*" * 60)
    print("\n" + "=" * 40)
    print(f"{'Índice':<10} | {'Nombre Válido':<20}")
    print("-" * 40)

    for i, nombre in enumerate(datos_nueva_lista):
        print(f"{i:<10} | {nombre:<20}")
    print("=" * 40)
    
lista_datos = ["Ana", "", "Luis", "   ", "María", "Pedro", ""]

lista_final = funcion2_recorre_lista(lista_datos)

funcion3_mostrar_reporte_final(lista_datos, lista_final)
