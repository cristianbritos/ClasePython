import json


class Persona:
    def __init__(self, nombre, dni):
        self.nombre = nombre
        self.dni = dni

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "dni": self.dni
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["nombre"], data["dni"])


class Alumno(Persona):
    def __init__(self, nombre, dni, matricula):
        super().__init__(nombre, dni)
        self.matricula = matricula

    def __str__(self):
        return f"Alumno: {self.nombre}, Matrícula: {self.matricula}"

    def to_dict(self):
        data = super().to_dict()
        data["matricula"] = self.matricula
        return data

    @classmethod
    def from_dict(cls, data):
        return cls(data["nombre"], data["dni"], data["matricula"])


class Profesor(Persona):
    def __init__(self, nombre, dni, legajo):
        super().__init__(nombre, dni)
        self.legajo = legajo

    def __str__(self):
        return f"Profesor: {self.nombre}, Legajo: {self.legajo}"

    def to_dict(self):
        data = super().to_dict()
        data["legajo"] = self.legajo
        return data

    @classmethod
    def from_dict(cls, data):
        return cls(data["nombre"], data["dni"], data["legajo"])


class Curso:
    def __init__(self, nombre, tipo, descripcion):
        self.nombre = nombre
        self.tipo = tipo
        self.descripcion = descripcion
        self.profesor = None
        self.alumnos = []
        self.notas = {}

    def asignar_profesor(self, profesor):
        self.profesor = profesor

    def inscribir_alumno(self, alumno):
        if alumno.matricula not in [a.matricula for a in self.alumnos]:
            self.alumnos.append(alumno)

    def cargar_nota(self, matricula, nota):
        self.notas[matricula] = nota

    def listar_notas(self):
        for alumno in self.alumnos:
            nota = self.notas.get(alumno.matricula, "Sin nota")
            print(f"{alumno} - Nota: {nota}")

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "tipo": self.tipo,
            "descripcion": self.descripcion,
            "profesor": self.profesor.to_dict() if self.profesor else None,
            "alumnos": [a.to_dict() for a in self.alumnos],
            "notas": self.notas
        }

    @classmethod
    def from_dict(cls, data):
        curso = cls(data["nombre"], data["tipo"], data["descripcion"])
        if data["profesor"]:
            curso.profesor = Profesor.from_dict(data["profesor"])
        curso.alumnos = [Alumno.from_dict(a) for a in data["alumnos"]]
        curso.notas = data["notas"]
        return curso


# Datos globales
alumnos = []
profesores = []
cursos = []


# Funciones de gestión
def registrar_alumno():
    nombre = input("Nombre del alumno: ")
    dni = input("DNI: ")
    matricula = input("Matrícula: ")
    alumno = Alumno(nombre, dni, matricula)
    alumnos.append(alumno)
    print("Alumno registrado.")


def registrar_profesor():
    nombre = input("Nombre del profesor: ")
    dni = input("DNI: ")
    legajo = input("Legajo: ")
    profesor = Profesor(nombre, dni, legajo)
    profesores.append(profesor)
    print("Profesor registrado.")


def crear_curso():
    nombre = input("Nombre del curso: ")
    tipo = input("Tipo: ")
    descripcion = input("Descripción: ")
    curso = Curso(nombre, tipo, descripcion)
    cursos.append(curso)
    print("Curso creado.")


def asignar_profesor_y_alumnos():
    if not cursos:
        print("No hay cursos.")
        return
    print("Cursos disponibles:")
    for i, curso in enumerate(cursos):
        print(f"{i}. {curso.nombre}")
    idx = int(input("Seleccione curso: "))
    curso = cursos[idx]

    if profesores:
        for i, prof in enumerate(profesores):
            print(f"{i}. {prof}")
        idx_p = int(input("Seleccione profesor: "))
        curso.asignar_profesor(profesores[idx_p])

    while True:
        print("Alumnos disponibles:")
        for i, a in enumerate(alumnos):
            print(f"{i}. {a}")
        entrada = input("Seleccione alumno o ENTER para salir: ")
        if entrada == "":
            break
        idx_a = int(entrada)
        curso.inscribir_alumno(alumnos[idx_a])


def cargar_nota_a_alumno():
    if not cursos:
        print("No hay cursos.")
        return
    for i, curso in enumerate(cursos):
        print(f"{i}. {curso.nombre}")
    idx = int(input("Seleccione curso: "))
    curso = cursos[idx]
    for i, alumno in enumerate(curso.alumnos):
        print(f"{i}. {alumno}")
    idx_a = int(input("Seleccione alumno: "))
    nota = float(input("Nota: "))
    curso.cargar_nota(curso.alumnos[idx_a].matricula, nota)
    print("Nota cargada.")


def listar_notas_curso():
    if not cursos:
        print("No hay cursos.")
        return
    for i, curso in enumerate(cursos):
        print(f"{i}. {curso.nombre}")
    idx = int(input("Seleccione curso: "))
    cursos[idx].listar_notas()


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
        print("\nSistema de Gestión Académica")
        print("1. Registrar alumno")
        print("2. Registrar profesor")
        print("3. Crear curso")
        print("4. Asignar profesor y alumnos a curso")
        print("5. Cargar nota")
        print("6. Listar notas")
        print("7. Guardar y salir")
        op = input("Seleccione una opción: ")

        match op:
            case "1":
                registrar_alumno()
            case "2":
                registrar_profesor()
            case "3":
                crear_curso()
            case "4":
                asignar_profesor_y_alumnos()
            case "5":
                cargar_nota_a_alumno()
            case "6":
                listar_notas_curso()
            case "7":
                guardar_datos()
                print("Datos guardados. Saliendo...")
                break
            case _:
                print("Opción inválida")


if __name__ == "__main__":
    menu()
