"""
def calcular_cuadrado(numero):
    resultado = numero **2
    
    return resultado

cuadrado__de_5 = calcular_cuadrado(5)
print(cuadrado__de_5)

def calcular_precio_total(precio_unitario,cantidad,descuento=0):
    subtotal = precio_unitario * cantidad
    descuento_aplicado = subtotal * (descuento/ 100)
    total = subtotal - descuento_aplicado
    return total

precio_sin_descuento = calcular_precio_total(500,3)
print(precio_sin_descuento)

precio_con_descuento = calcular_precio_total(500,3,25)
print(precio_con_descuento)

def calcular_area_y_perimetro(base,altura):
    area = base * altura
    perimetro = 2 *(base + altura)
    return area , perimetro


print(calcular_area_y_perimetro(8,5))
areaG, perimetroG = calcular_area_y_perimetro(8,5)
print(areaG)
print(perimetroG)

resultado = calcular_area_y_perimetro(8,5)
print(resultado[0] ,resultado[1])


def estadisticas(numeros):
    minimo = min(numeros)
    maximo = max(numeros)
    promedio = sum (numeros)/ len(numeros)

    return minimo, maximo, promedio

notas = [7,9,5,8,6,10,4]
minimo,maximo,promedio = estadisticas(notas)

print(f"Notas:{notas}")
print(f"Minimas:{minimo}")
print(f"Maximas {maximo}")
print(f"Promedio: {promedio}")


def calcular_precio_final(precio,impuesto):
    
    return precio + (precio * impuesto / 100)

# datos de la compra
precio_unitario = 500
cantidad = 3

# compra sin dwescuento
total_sin_descuento = calcular_precio_total(precio_unitario, cantidad)

total_con_descuento_25 = calcular_precio_total(precio_unitario,cantidad, 25)

# aplicaar iva 21%
precio_con_iva = calcular_precio_final(total_con_descuento_25,21)
print(f"precio con iva, {precio_con_iva}")
#aplicar PB de 2%
precio_con_PB = calcular_precio_total(total_con_descuento_25,2)
print(f"precio con iva, {precio_con_PB}")
"""
def calcular_imc(peso, altura):
    """
    calcula el indice de Masaa Corporal (IMC)
    
    formula : imv = peso (kg) / altura2 (m)
    parametros:
    peso (float): peso de la persona en kilogramos,
    altura (float): altura de la persona en metros
    retorna:
    float: el valor redondeado a 2 decimales.
    """
    imc = peso / (altura ** 2)
    return round(imc,2)
    
    
imc = calcular_imc(70,1.75)
print(imc)
    ## help (calcular_imc)
    



    