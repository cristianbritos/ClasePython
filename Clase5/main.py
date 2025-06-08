import control 
from control import (
    Profesor, Alumno,
    listar_personas, add_persona,
    cargar_lista, agregar_persona,
    guardar_lista, Profesores, Alumnos,
)


def menu_principal():
    while True:
        print("\nMenu Principal")
        print("--------------")
        print("1. Profesores")
        print("2. Alumnos")
        print("3. Cursos")
        print("4. Salir")
        op = input("Seleccione una opcion: ")

        match op:
            case "1":
                menu_profesores()
            case "2":
                menu_alumnos()
            case "3":
                print("Modulo de cursos en desarrollo...")
            case "4":
                print("Saliendo del programa...")
                break
            case _:
                print("Opcion invalida, intente nuevamente.")


def menu_profesores():
    while True:
        print("\nMenu Profesores")
        print("---------------")
        print("1. Agregar Profesor")
        print("2. Listar Profesores")
        print("3. Guardar Profesores")
        print("4. Volver al menu principal")
        op = input("Seleccione una opcion: ")

        match op:
            case "1":
                agregar_persona("profesor")
            case "2":
                listar_personas(control.Profesores, "profesor")
            case "3":
                guardar_lista("Profesores.json",control.Profesores)
                print("Profesores guardados exitosamente en JSON.")
            case "4":
                break
            case _:
                print("Opcion invalida, intente nuevamente.")


def menu_alumnos():
    while True:
        print("\nMenu Alumnos")
        print("-------------")
        print("1. Agregar Alumno")
        print("2. Listar Alumnos")
        print("3. Guardar Alumnos")
        print("4. Volver al menu principal")
        op = input("Seleccione una opcion: ")

        match op:
            case "1":
                agregar_persona("alumno")
            case "2":
                listar_personas(control.Alumnos, "Alumno")
            case "3":
                guardar_lista("Alumnos.json", control.Alumnos)
                print("Alumnos guardados exitosamente en JSON.")
            case "4":
                break
            case _:
                print("Opcion invalida, intente nuevamente.")


if __name__ == "__main__":
    menu_principal()
