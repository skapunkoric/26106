#import nombre_modulo
# nombre_modulo.funcion()
# random

import random
import math

"""
dado = random.randint(1,6)
print(dado)
frutas = ["manzanas","bananas","peras","naranjas"]
fruta_elegida = random.choice(frutas)
print(fruta_elegida)

numeros = [1,2,3,4,5]

random.shuffle(numeros)
print(numeros)

raiz = math.sqrt()

print(raiz)

radio = 5
area = math.pi * math.pow(radio,2)
print(area)

decimal = 3,7
#print (f"arriba", math.ceil(decimal))
#print (f"abajo", math.floor(decimal))

import datetine as dt
fecha_actual= dt.datetime.now()
print(fecha_actual)

from random import randint
numero_aleatorio = randint(1,10)
"""
#colorama
from colorama import Fore, Back, init
init()
print(Fore.GREEN + "Texto en verde")
print(Back.RED + "Fondo rojo" + Back.RESET)
print(Fore.BLUE + Back.YELLOW + "Texto azul en fondo amarillo")
