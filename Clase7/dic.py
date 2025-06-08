import json


class Producto:
    def __init__(self, cod, nom, desc, prec):
        self.codigo = cod
        self.nombre = nom
        self.descripcion = desc
        self.precio = prec

    def __str__(self):
        return f"Código: {self.codigo}, Nombre: {self.nombre}, Descripción: {self.descripcion}, Precio: {self.precio}"

    def to_dict(self):
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "descripcion": self.descripcion,
            "precio": self.precio
        }

    def from_dict(cls, data):
        return cls(data["codigo"], data["nombre"], data["descripcion"], data["precio"])


class Venta:
    def __init__(self, cod, cli, prod):
        self.codigo = cod
        self.cliente = cli
        self.detalle = {}
        self.precTot = 0

    def __str__(self):
        return f"Código: {self.codigo}, Cliente: {self.cliente}, Producto: {self.producto}, Cantidad: {self.cantidad}, Precio: {self.precio}"

def add_productos(p):
    productos.append(p)

def add_ventas(v):
    ventas.append(v)

def registrar_producto():
    print("\nRegistrar Producto")
    nom = input("Ingrese el nombre del producto: ")
    det = input("Ingrese la descripción del producto: ")
    try:
        prec = int(input("Ingrese el precio del producto: "))
    except ValueError:
        print("El precio debe ser un número entero.")
        return
    p = Producto(len(productos) + 1, nom, det, prec)
    add_productos(p)

def registrar_ventas():
    print("\nRegistrar Ventas")
    cod = input("Ingrese el código de la venta: ")
    cli = input("Ingrese Cliente:")
    while True:
        print("\nProductos disponibles:")
        for id,item in Productos:
            print(f"{id}) {item.codigo}: {item.nombre} - {item.precio}")
        prod = input("Ingrese el código del producto o 0 para terminar: ")
        cant = input("Ingrese la cantidad: ")
        prec = int(input("Ingrese el precio: "))
        det ["id"] = id 
        det ["producto"] = prod 
        det ["cantidad"] = cant 
        det ["precio"] = prec
    

def guardar_datos():
    with open("datos.json", "w", encoding="utf-8") as f:
        data = {
            "alumnos": [a.to_dict() for a in alumnos],
            "profesores": [p.to_dict() for p in profesores],
            "cursos": [c.to_dict() for c in cursos]
        }
        json.dump(data, f, indent=4)


def cargar_datos():
    global alumnos, profesores, cursos
    try:
        with open("datos.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            alumnos = [Alumno.from_dict(a) for a in data["alumnos"]]
            profesores = [Profesor.from_dict(p) for p in data["profesores"]]
            cursos = [Curso.from_dict(c) for c in data["cursos"]]
    except FileNotFoundError:
        pass


def menu():
    cargar_datos()
    while True:
        print("\nSistema de Ventas")
        print("1. Registrar Producto")
        print("2. Registrar Ventas")
        print("3. Listar Productos")
        print("4. Listar Ventas")
        print("5. Guardar y salir")
        op = input("Seleccione una opción: ")

        match op:
            case "1":
                registrar_producto()
            case "2":
                registrar_ventas()
            case "3":
                listar_productos()
            case "4":
                listar_ventas()
            case "5":
                guardar_datos()
                print("Datos guardados. Saliendo...")
                break
            case _:
                print("Opción inválida")


if __name__ == "__main__":
    menu()
