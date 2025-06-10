import json
import csv 
from rutinas import busqueda_binaria, busqueda_lineal, bubble_sort, quick_sort, guardar_lista, cargar_lista, Producto 

Productos = []

def Menu():
    Productos = cargar_lista("datos.json")
    print("Menu Principal")
    print("--------------")
    while True:
        print("1) Busqueda Binaria Simple")
        print("2) Busqueda Binaria con Recursividad")
        print("3) Salir")

        op = input("Ingrese una opcion: ")

        if op == "1":
            print("\n" + "="*50)
            nombre = input("Nombre del producto a buscar: ")
            inicio = time.perf_counter()
            resultado = busqueda_lineal(productos, nombre)
            fin = time.perf_counter()
            print("Resultado:", resultado if resultado else "No encontrado")
            print(f"Tiempo de búsqueda: {fin - inicio:.6f} segundos")
            print("="*50)
        elif op == "2":
            print("Busqueda Lineal")
            #Llamar a la funcion de busqueda binaria con recursividad
        elif op == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opcion no valida, intente nuevamente.")

if __name__ == "__main__":
    Menu()
