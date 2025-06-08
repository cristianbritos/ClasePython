import json
class Cliente:
    def __init__(self, id, nom, ape, d, email):
        self.id_cliente = id
        self.nombre = nom
        self.apellido = ape
        self.dni = d
        self.email = email
    
    def nombre_completo(self):
        return f"{self.nombre}, {self.apellido}"
    
    def to_dict(self):
        return {
            "id_cliente": self.id_cliente,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "dni": self.dni,
            "email": self.email
        }

    @staticmethod
    def from_dict(data):
        return Cliente(
            data["id_cliente"],
            data["nombre"],
            data["apellido"],
            data["dni"],
            data["email"],
        )

clientes = [
    Cliente(1, "Juan", "Pérez", "juan@email.com", "123456789"),
    Cliente(2, "Ana", "Gómez", "ana@email.com", "987654321"),
    Cliente(3, "Luis", "Martínez", "luis@email.com", "456123789")
]

# Convertimos a lista de diccionarios
clientes_data = [cliente.to_dict() for cliente in clientes]

# Guardamos en archivo
with open("clientes.json", "w", encoding="utf-8") as f:
    json.dump(clientes_data, f, indent=4, ensure_ascii=False)


# Leemos el archivo
with open("clientes.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Reconstruimos los objetos Cliente
clientes_recuperados = [Cliente.from_dict(item) for item in data]

# Mostramos nombres completos
for cliente in clientes_recuperados:
    print(cliente.nombre_completo())

