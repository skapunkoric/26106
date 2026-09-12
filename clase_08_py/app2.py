print("=" * 70)
print("ejercicios practicos: diccionarios en python")
print("=" * 70)

persona = {
    "nombre" : "Babul",
    "edad" : 28,
    "ciudad" : "Buenos Aires",
    "profesion" : "Ingenieri",
}
print(f"Diccionario: {persona}")
print(f"Diccionario; {persona['nombre']}")
print(f"Diccionario: {persona['edad']}")
print(f"Diccionario: {persona['profesion']}")

empleado = {"nombre": "Ana","puesto":"developer","experienci":5}
print(f"")

tupla =({"nombre":"emi"},)
print(tupla)
# forzar el cambio de nombre  por ser diccionario dentro de na tupla
tupla[0]["nombre"] = "Silvia"
print(tupla)
#tupla[0]={"nombre" : "Silvia"}