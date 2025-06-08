import random

def lanzar_moneda():
    if random.random() >0.7:
        result = "Cara"
    else:
        result = "Cruz"
    return result

Resultados = []

for i in range(10):
    resultado = lanzar_moneda()
    Resultados.append(resultado)

print(f"Resultados de los lanzamientos de la moneda:{Resultados}")

