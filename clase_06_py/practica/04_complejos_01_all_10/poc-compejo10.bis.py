lista_de_puntajes = [1200, 900, 450, 300, 750, 1200, 100]
lista_puntajes_mayor_a_800 = []

maximo = max(lista_de_puntajes)
minimo = min(lista_de_puntajes)
promedio_puntajes = sum(lista_de_puntajes) / len(lista_de_puntajes)
cantidad_maxima = lista_de_puntajes.count(maximo)

for puntaje in lista_de_puntajes:
    if puntaje >= 800:
        lista_puntajes_mayor_a_800.append(puntaje)

cantidad_puntaje_800 = len(lista_puntajes_mayor_a_800)

# ── helpers visuales ──────────────────────────────────────
ANCHO = 52

def linea(car="─"): 
    print(car * ANCHO)

def fila(etiqueta, valor):
    print(f"  {etiqueta:<30} {valor}")

# ── reporte ───────────────────────────────────────────────
print()
linea("═")
print("🏆  REPORTE DE PUNTAJES".center(ANCHO))
linea("═")

fila("📋 Lista completa:",       str(lista_de_puntajes))
linea()
fila("🥇 Puntaje más alto:",     f"{maximo}  (aparece {cantidad_maxima}x)")
fila("🥉 Puntaje más bajo:",     f"{minimo}")
fila("📊 Promedio general:",     f"{promedio_puntajes:.2f}")
fila("🔥 Puntajes TOP (≥800):",  f"{cantidad_puntaje_800} encontrados")
linea("═")

print("  📌 Detalle TOP:".ljust(ANCHO))
for p in lista_puntajes_mayor_a_800:
    print(f"     {'█' * (p // 100)}  {p}")

linea("═")
print()