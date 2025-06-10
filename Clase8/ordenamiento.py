import csv

ruta = "inventario_productos.csv"
class Producto:
    def __init__(self, id, nombre, stock, precio):
        self.id = id
        self.nombre = nombre
        self.stock = stock
        self.precio = precio

    def __repr__(self):
        return f"{self.id} - {self.nombre} | Stock: {self.stock} | ${self.precio}"
def cargar_productos_csv(ruta):
    productos = []
    with open(ruta, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            producto = Producto(
                id=int(row['ID']),
                nombre=row['Nombre'],
                stock=int(row['Stock']),
                precio=int(row['Precio'])
            )
            productos.append(producto)
    return productos

def guardar_productos_csv(productos, ruta):
    with open(ruta, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['ID', 'Nombre', 'Stock', 'Precio'])
        for p in productos:
            writer.writerow([p.id, p.nombre, p.stock, p.precio])
