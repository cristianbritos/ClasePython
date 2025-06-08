class Cliente:
    def __init__(self, id, nom, ape, d, email):
        self.id_cliente = id
        self.nombre = nom
        self.apellido = ape
        self.dni = d
        self.email = email
    
    def nombre_completo(self):
        return f"{self.nombre}, {self.apellido}"

#------------Lista de Objetos---------------
Clientes = [
    Cliente(1,'Fatima', 'Britos', 49000, 'faty@gmail.com'),
    Cliente(2,'Maria', 'Britos', 51000, 'maria@gmail.com'),
    Cliente(3,'Nazarena', 'Britos', 42000, 'nany@gmail.com'),
]

for cliente in Clientes:
    print(cliente.nombre_completo())

#-----------Diccionario de Objetos---------------

Clientes_dict = {
    1: Cliente(1, 'Fatima', 'Britos', 49000, 'faty@gmail.com'),
    2: Cliente(2, 'Maria', 'Britos', 51000, 'maria@gmail.com'),
    3: Cliente(3, 'Nazarena', 'Britos', 42000, 'nany@gmail.com'),
}

cliente = Clientes_dict[1]
print(cliente.nombre_completo())

for value in range(1,3):
    print(Clientes_dict[value].nombre_completo())
