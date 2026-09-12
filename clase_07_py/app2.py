"""""
# tuplas
lista = [10, 20, 30]
tupla = (10, 20, 30)

#print(tupla)
#print(lista)

tupla1 = 30,60,90
#print(tupla1)

tupla_unica =(100,)
print(tupla_unica)
print(tupla[0])
print(tupla[1])
print(tupla[2])
lista = list[tupla]
lista[0] = 12
tupla_nueva = tuple(lista)

lista = [10, 20, 30]
tupla = (10, 20, 30)

# diccionarios
# 'clave : valor'
persona = { 
    "nombre" : "Emiliano",
    "edad" : 35,
    "ciudad" : "Santa Fe",
    "Profesion" : "Educational Developer",
    }

print(persona)
persona ["nombre"] = "luis"
#print(persona["email"])
print(persona.get('nombre','no disponible'))
print(persona.get('email','sin email'))
persona["email"] = 'babul@babul.com'
persona.setdefault('telefono', '555-1234')
print(persona)
persona.pop('email')
print(persona)
del persona ['telefono']
print(persona)

#clave for
for pers in persona:
    print(pers)

#valores for
for pers in persona.values():
    print(pers)

# clave , valor
for clave, valor  in persona.items():
    print(pers)
    print(f"{clave}: {valor}")
"""""


persona = { 
    "nombre" : "Emiliano",
    "edad" : 35,
    "ciudad" : "Santa Fe",
    "Profesion" : "Educational Developer",
    "profesor" : True,
    "peliz_favoritas" : ["peli1","peli2"]
    }

nuevos_datos = {'email':'babul@example.con','telefono':'555-1234'}
persona.update(nuevos_datos)

print(persona)