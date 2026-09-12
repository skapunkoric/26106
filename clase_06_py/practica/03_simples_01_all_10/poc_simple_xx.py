"""""
lista_frutas = ["manzana", "banana", "cereza", "durazno"]

print("=" * 35)
print(f"| {'ID':<4} | {'FRUTA':<15} |")
print("=" * 35)

# Usamos enumerate con start=1 para el ID de mostrador
for i, fruta in enumerate(lista_frutas, start=1):
    # :02d -> ID con dos dígitos (01, 02...)
    # :<15 -> Deja 15 espacios fijos para el nombre de la fruta
    print(f"| {i:02d} | {fruta.capitalize():<15} |")

print("=" * 35)
print(f"Total variedades: {len(lista_frutas)}")
print("=" * 35)
"""

lista_frutas = ["manzana", "banana", "cereza", "durazno"]

print("=" * 35)
print(f"| {'POS':<4} | {'FRUTA':<15} |")
print("=" * 35)

# Camina por los índices: 0, 1, 2, 3
for i in range(len(lista_frutas)):
    fruta = lista_frutas[i]  # Buscamos la fruta por su posición

    print(f"| {i:<4} | {fruta.capitalize():<15} |")

print("=" * 35)