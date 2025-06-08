import json

clientes = []

class Cliente:
    def __init__(self, id, ape, nom, dni):
        self.id_cliente = id 
        self.apellido = ape 
        self.nombre = nom 
        self.dni = dni 

    def __str__(self):
        return f"{self.apellido}, {self.nombre} (DNI: {self.dni})"


    def to_dict(self):
        return {
            "id_cliente": self.id_cliente,
            "apellido": self.apellido,
            "nombre": self.nombre,
            "dni": self.dni
        }


    @staticmethod
    def from_dict(data):
        return Cliente(
            data["id_cliente"],
            data["apellido"],
            data["nombre"],
            data["dni"]
        )


def add_cliente(cliente):
    clientes.append(cliente)


def list_clientes():
    if not clientes:
        print("No hay clientes cargados.")
    else:
        print("\nListado de Clientes:")
        for cliente in clientes:
            print(cliente)


def save_clientes():
    with open("clientes.json", "w", encoding="utf-8") as f:
        json.dump([c.to_dict() for c in clientes], f, indent=4, ensure_ascii=False)


def load_clientes():
    global clientes
    try:
        with open("clientes.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        clientes = [Cliente.from_dict(item) for item in data]
    except FileNotFoundError:
        clientes = []


def get_next_id():
    return max((c.id_cliente for c in clientes), default=0) + 1


def agregar_cliente():
    print("\n--- Nuevo Cliente ---")
    ape = input("Apellido: ")
    nom = input("Nombre: ")
    try:
        dni = int(input("DNI: "))
    except ValueError:
        print("DNI inválido.")
        return

    cliente = Cliente(get_next_id(), ape, nom, dni)
    add_cliente(cliente)
    print("Cliente agregado.")
