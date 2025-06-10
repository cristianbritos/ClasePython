import json


class Producto:
    def __init__(self, id, nombre, stock, precio):
        self.id = id
        self.nombre = nombre
        self.stock = stock
        self.precio = precio

    def __str__(self):
        return f"{self.id} - {self.nombre} | Stock: {self.stock} | ${self.precio}"

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "stock": self.stock,
            "precio": self.precio
        }
    @staticmethod
    def from_dict(data):
        return Producto(
            ID=data["ID"],
            nombre=data["Nombre"],
            stock=data["Stock"],
            precio=data["Precio"]
        )
    


# Funciones para Guardar y Cargar Datos JSON
def guardar_lista(nombre_archivo, lista):
    with open(nombre_archivo, "w", encoding="utf-8") as f:
        json.dump([p.to_dict() for p in lista], f, indent=4, ensure_ascii=False)


def cargar_lista(nombre_archivo):
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as f:
            data = json.load(f)
            print(f"Datos cargados desde {nombre_archivo}.")
        return [Producto.from_dict(item) for item in data]
    except FileNotFoundError:
        print(f"{nombre_archivo} no encontrado. Lista vacía inicializada.")
        return []

# Fin de Funciones 

# Búsqueda lineal por nombre
def busqueda_lineal(productos, nombre_buscado):
    for producto in productos:
        if producto.nombre == nombre_buscado:
            return producto
    return None

# Búsqueda binaria (requiere lista ordenada por nombre)
def busqueda_binaria(productos, nombre_buscado):
    productos.sort(key=lambda x: x.nombre)  # Asegura ordenamiento
    izq = 0
    der = len(productos) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if productos[medio].nombre == nombre_buscado:
            return productos[medio]
        elif productos[medio].nombre < nombre_buscado:
            izq = medio + 1
        else:
            der = medio - 1
    return None

# Bubble Sort por precio
def bubble_sort(productos):
    n = len(productos)
    for i in range(n):
        for j in range(0, n-i-1):
            if productos[j].precio > productos[j+1].precio:
                productos[j], productos[j+1] = productos[j+1], productos[j]

# Quick Sort por stock
def quick_sort(productos):
    if len(productos) <= 1:
        return productos
    pivote = productos[0]
    menores = [p for p in productos[1:] if p.stock <= pivote.stock]
    mayores = [p for p in productos[1:] if p.stock > pivote.stock]
    return quick_sort(menores) + [pivote] + quick_sort(mayores)
