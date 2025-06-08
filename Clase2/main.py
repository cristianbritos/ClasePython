from client import Cliente, agregar_cliente, list_clientes, save_clientes, load_clientes
from product import Producto, agregar_producto, list_productos, save_productos, load_productos


def menu_cliente():
    while True:
        print("\n---Menú de Clientes ---")
        print("1. Agregar Cliente")
        print("2. Listar Clientes")
        print("3. Guardar Clientes")
        print("4. Salir")
        opcion = input("Seleccione una opción (1-4): ")

        if opcion == "1":
            agregar_cliente()
        elif opcion == "2":
            list_clientes()
        elif opcion == "3":
            save_clientes()
            print("Clientes guardados.")
        elif opcion == "4":
            print("Saliendo... ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")


def menu_producto():
    while True:
        print("\n---Menú de Productos ---")
        print("1. Agregar Producto")
        print("2. Listar Productos")
        print("3. Guardar Productos")
        print("4. Salir")
        opcion = input("Seleccione una opción (1-4): ")

        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            list_productos()
        elif opcion == "3":
            save_productos()
            print("Productos guardados.")
        elif opcion == "4":
            print("Saliendo... ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")


def menu_venta():
    while True:
        print("\n---Menú de Ventas ---")
        print("1. Agregar Venta")
        print("2. Listar Ventas")
        print("3. Guardar Ventas")
        print("4. Salir")
        opcion = input("Seleccione una opción (1-4): ")

        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            list_productos()
        elif opcion == "3":
            save_productos()
            print("Productos guardados.")
        elif opcion == "4":
            print("Saliendo... ¡Hasta luego!")
            break
        else:
            print("Opción no valida. Intente de nuevo.")
        


def menu_principal():
    while True:
        print("\n---Menú Principal ---")
        print("1. Menú de Clientes")
        print("2. Menú de Productos")
        print("3. Menú de Ventas")
        print("4. Salir")
        opcion = input("Seleccione una opción (1-4): ")

        if opcion == "1":
            menu_cliente()
        elif opcion == "2":
            menu_producto()
        elif opcion == "3":
            menu_venta()
        elif opcion == "4":
            print("Saliendo... ¡Saliendo Hasta Luego!")
            break
        else:
            print("Opción no valida. Intente de nuevo.")
            

# Inicio del programa
load_clientes()
load_productos()
menu_principal()
save_clientes()
save_productos()
