ventas = []

ventas.append(1000)
ventas.append(1500)
ventas.append(100)
ventas.append(15300)
ventas.append(15200)
ventas.append(150)
ventas.append(150)

print(ventas)
print(max(ventas))
print(min(ventas))
print(f"promedio de las ventas {sum(ventas)/len(ventas):.2f}")
#venta_cliente = input("ingrese monto de la vida")
#ventas.append(venta_cliente)
#print(ventas)
#ventas.append[120,30,20]
ventas.extend({120,30,50})
print(ventas)
ventas.insert(2,"Emi")
print(ventas)

inventario = ["pan","leche","queso","yogur","peras","pan","pan"]

print(inventario.count("pan"))

if "pan" in inventario:
    inventario.remove("pan")

print(inventario)
print(inventario.pop(1))
print(inventario)



