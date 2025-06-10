import csv
import json

# Abrimos el archivo CSV
with open('inventario_productos.csv', mode='r', encoding='utf-8') as csv_file:
    lector = csv.DictReader(csv_file)
    filas = list(lector)  # Convertimos en una lista de diccionarios

# Guardamos como JSON
with open('datos.json', mode='w', encoding='utf-8') as json_file:
    json.dump(filas, json_file, indent=4, ensure_ascii=False)

print("Conversión completada.")
