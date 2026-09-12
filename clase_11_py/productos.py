import random
import datetime

def crear_producto(nombre,precio):
    codigo = random.randomint(1000, 9999)
    fecha_compra = datetime.datetime.now()

    producto = {

"codigo" : codigo,
"nombre" : nombre,
"precio" : precio,
"fecha_compra" : fecha_compra

    }
