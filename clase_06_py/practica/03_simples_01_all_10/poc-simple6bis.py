"""
Consigna:
Dada la lista frutas = ["manzana", "banana", "cereza", "durazno"], mostrar cada fruta usando while.

Requisitos:
- Usar una variable indice que empiece en 0.
- Usar len(frutas) en la condición del while.
- Mostrar cada elemento accediendo con frutas[indice].
"""
lista_frutas = ["manzana", "banana", "cereza", "durazno", "frutilla", "arándano"]

print("=" * 45)
print(f"| {'ID':<5} | {'PRODUCTO':<15} | {'CARACTERES':<12} |")
print("=" * 45)

# Usamos enumerate sólo para generar un ID estético (01, 02, 03...)
for i, fruta in enumerate(lista_frutas, start=1):
    # Capitalizamos la primera letra para que quede pro si viene en minúscula
    fruta_clean = fruta.capitalize()

    # Contamos el largo del string para simular un dato extra
    largo = len(fruta)

    # Formateo Pro:
    # :02d -> Pone el número con dos dígitos (01, 02...)
    # :<15 -> Alinea a la izquierda en 15 espacios
    # :^12 -> Centra el número en 12 espacios
    print(f"| {i:02d}  | {fruta_clean:<15} | {largo:^12} |")

print("=" * 45)
print(f"Total de variedades registradas: {len(lista_frutas)}")
print("=" * 45)
