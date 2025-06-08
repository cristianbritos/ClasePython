import json

Profesores = []
Alumnos = []


class Persona:
    def __init__(self, id, nombre, dni):
        self.id = id
        self.nombre = nombre
        self.dni = dni

    def __str__(self):
        return f"{self.__class__.__name__}: {self.nombre}, ID: {self.id}, DNI: {self.dni}"

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "dni": self.dni
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["id"], data["nombre"], data["dni"])


class Profesor(Persona):
    def __init__(self, legajo, nombre, dni):
        super().__init__(legajo, nombre, dni)
        self.legajo = legajo

    def __str__(self):
        return f"Profesor: {self.nombre}, Legajo: {self.legajo}, DNI: {self.dni}"

    def to_dict(self):
        return {
            "legajo": self.legajo,
            "nombre": self.nombre,
            "dni": self.dni
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["legajo"], data["nombre"], data["dni"])


class Alumno(Persona):
    def __init__(self, matricula, nombre, dni):
        super().__init__(matricula, nombre, dni)
        self.matricula = matricula

    def __str__(self):
        return f"Alumno: {self.nombre}, Matrícula: {self.matricula}, DNI: {self.dni}"

    def to_dict(self):
        return {
            "matricula": self.matricula,
            "nombre": self.nombre,
            "dni": self.dni
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["matricula"], data["nombre"], data["dni"])


def add_persona(lista, persona):
    lista.append(persona)


def listar_personas(lista, titulo):
    print("\n" + titulo)
    print("-" * len(titulo))
    if not lista:
        print("No hay registros disponibles.")
    else:
        for item in lista:
            print(item)


def agregar_persona(tipo):
    nombre = input("Apellido y Nombre: ")
    try:
        dni = int(input("DNI: "))
    except ValueError:
        print("DNI debe ser un número entero.")
        return

    if tipo == "profesor":
        legajo = input("Legajo: ")
        persona = Profesor(legajo, nombre, dni)
        add_persona(Profesores, persona)
    elif tipo == "alumno":
        matricula = input("Matrícula: ")
        persona = Alumno(matricula, nombre, dni)
        add_persona(Alumnos, persona)

    print(f"{tipo.capitalize()} agregado exitosamente.")


def guardar_lista(nombre_archivo, lista):
    with open(nombre_archivo, "w", encoding="utf-8") as f:
        json.dump([p.to_dict() for p in lista], f, indent=4, ensure_ascii=False)


def cargar_lista(nombre_archivo, clase):
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as f:
            data = json.load(f)
            print(f"Datos cargados desde {nombre_archivo}.")
        return [clase.from_dict(item) for item in data]
    except FileNotFoundError:
        print(f"{nombre_archivo} no encontrado. Lista vacía inicializada.")
        return []


class Curso:
    def __init__(self, nombre, detalle, tipo, profesor, alumno):
        self.nombre = nombre
        self.detalle = detalle
        self.tipo = tipo
        self.profesor = profesor
        self.alumno = alumno

    def __str__(self):
        return f"Curso: {self.nombre}, Detalle: {self.detalle}, Tipo: {self.tipo}"


print("INICIANDO PROGRAMA...")
Profesores = cargar_lista("Profesores.json", Profesor)
Alumnos = cargar_lista("Alumnos.json", Alumno)
