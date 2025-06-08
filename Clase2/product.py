import json

productos= []

class Producto:
    
    def __init__(self, id, nom, det, pre):
        self.id_producto = id
        self.nombre = nom 
        self.detalle = det 
        self.precio = pre
    

    def __str__(self):
        return f"{self.nombre} ({self.detalle}): ${self.precio}"

    def to_dict(self):
        return {
            "id_producto":self.id_producto,
            "nombre": self.nombre,
            "detalle": self.detalle,
            "precio": self.precio
        }


    @staticmethod
    def from_dict(data):
        return Producto(
            data["id_producto"],
            data["nombre"],
            data["detalle"],
            data["precio"]
        )


def add_producto(p):
    productos.append(p)


def list_productos():
    if not productos:
        print("\nNo hay productos Cargados..")
    else:
        print("\n Listado de Productos")
        for prod in productos:
            print(prod)


def save_productos():
    with open("productos.json", "w", encoding="utf-8") as f:
        json.dump([p.to_dict() for p in productos], f, indent=4, ensure_ascii=False)


def load_productos():
    global productos
    try:
        with open("productos.json","r", encoding="utf-8") as f:
           data = json.load(f) 
        productos = [Producto.from_dict(item) for item in data]
    except FileNotFoundError:
        productos = []

def id_max():
    return max((prod.id_productos for prod in productos), default=0)+1


def agregar_producto():
    print("\nAgregar Productos:")
    nom = input("Nombre:")
    det = input("Detalle:")
    try:
        pre = int(input("Precio:"))
    except ValueError:
        print("Precion Invalido")
        return
    producto = Producto(id_max(), nom, det, pre)
    add_producto(producto)
    print("Producto Agregado...")


