Productos = []
Ventas = []

class Producto: 
    def __init__(self, cod, nom, prec):
        self.codigo = cod
        self.nombre = nom
        self.precio = prec
    
    def __str__(self):
        return f"Código: {self.codigo}, Nombre: {self.nombre}, Precio: {self.precio}"

class Venta:
    def __init__(self, cod, cli, prods):
        self.codigo = cod
        self.cliente = cli
        self.producto = prods
        self.precioTotal = 0

    def __str__(self):
        return f"Código de venta: {self.codigo}, Cliente: {self.cliente}, Total: {self.precioTotal}"

def ListarVentas():
    print("Ventas registradas:")
    print("-------------------")


def AgregarVenta():
    global Productos
    print("\nRegistrar Venta")
    cod = 0
    cli = input("Ingrese el nombre del cliente: ")
    det = {}
    while True:
        id=0
        for item in Productos:
            id=id+1
            print(f"{id}) {item.codigo}: {item.nombre} - {item.precio}")
        id = int(input("Seleccione el producto por su ID o 0 Para Terminar: "))
        if id == 0:
            break
        cant = int(input("Ingrese la cantidad: "))
        prec = float(input("Ingrese el precio: "))
        det = {id:[cant,prec]}
    v = Venta(cod, cli, det)
    Ventas.append(v)
    print("Venta registrada exitosamente.")

def AgregarProducto():
    cod = input("Ingrese el código del producto: ")
    nom = input("Ingrese el nombre del producto: ")
    prec = float(input("Ingrese el precio del producto: "))
    
    nuevo_producto = Producto(cod, nom, prec)
    Productos.append(nuevo_producto)
    print("Producto agregado exitosamente.")

def ListarProductos():
    if not Productos:
        print("No hay productos registrados.")
    else:
        print("Productos registrados:")
        for producto in Productos:
            print(producto)

def Menu():
    while True:
        print("Menu Principal")
        print("--------------")
        print("1. Agregar Producto")
        print("2. Listar Productos")
        print("3. Agregar Venta")
        print("4. Listar Ventas")
        print("5. Salir")

        op = input("Seleccione una opción (1-5): ")

        if op == "1":
            AgregarProducto()
        elif op == "2":
            ListarProductos()
        elif op == "3":
            AgregarVenta()
        elif op == "4":
            print("Función para listar ventas aún no implementada.")
        elif op == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    Menu()
