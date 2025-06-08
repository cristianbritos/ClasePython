import json
from client import Cliente, agregar_cliente, list_clientes, save_clientes, load_clientes
from product import Producto, agregar_producto, list_productos, save_productos


ventas = []

class Venta:
    def __init__(self, id, fecha, cliente, productos):
        self.id_venta = id
        self.fecha = fecha
        self.cliente = cliente  # Instancia de Cliente
        self.productos = productos  # Lista de instancias de Producto

    def __str__(self):
        return f"Venta ID: {self.id_venta}, Fecha: {self.fecha}, Cliente: {self.cliente.nombre}, Productos: {[p.nombre for p in self.productos]}"

    def to_dict(self):
        return {
            "Venta ID": self.id_venta,
            "Fecha": self.fecha,
            "Cliente": self.cliente.to_dict(),
            "Prductos": self.productos_to_dict(),
        }

    def from_dict(data):
        cliente = Cliente.from_dict(data["Cliente"])
        productos = [Producto.from_dict(p) for p in data["Prductos"]]
        return Venta(data["Venta ID"], data["Fecha"], cliente, productos)

def add_venta(venta):
    venta.append(venta)

def list_ventas():
    if not ventas:
        print("No hay ventas registradas.")
    else:
        print("\nListado de Ventas:")
        for venta in ventas:
            print(venta)

def load_ventas():
    global ventas
    try:
        with open("ventas.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        ventas = [Venta.from_dict(item) for item in data]
    except FileNotFoundError:
        ventas = []

def save_ventas():
    with open("ventas.json", "w", encoding="utf-8") as f:
        json.dump([v.to_dict() for v in ventas], f, indent=4, ensure_ascii=False)

def agregar_venta():

