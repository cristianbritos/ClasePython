## Sistema de inventario de productos ##
#Leer un archivo CSV con los productos.(ya esta hecho)
#Buscar productos por nombre o ID.(ya esta hecho)
#Ordenar los productos por precio o por stock.(ya esta hecho)
#Comparar algoritmos de ordenamiento por eficiencia.(no se si lo haremos o no pero podemos ir viendo)
#hay que pulirlo y dejarlo bonito, pero ya tenemos la base
from busqueda import busqueda_lineal, busqueda_binaria, bubble_sort, quick_sort
from ordenamiento import guardar_productos_csv, cargar_productos_csv, Producto

import time


def mostrar_menu():
    """Muestra el menú principal del programa."""
    # Separa las opciones del menú
    print("\n" + "="*60)
    print("===== INVENTARIO DE PRODUCTOS =====")
    # Separa las opciones del menú
    print("="*60)
    print("Seleccione una opción:")
    print("1. Búsqueda Lineal por nombre")
    print("2. Búsqueda Binaria por nombre")
    print("3. Ordenamiento por precio (Bubble Sort)")
    print("4. Ordenamiento por stock (Quick Sort)")
    print("5. Salir")
    # Separa las opciones del menú
    print("-" * 60)

def main():
    """Función principal del programa."""
    ruta = "inventario_productos.csv"
    productos = cargar_productos_csv(ruta)

    while True:
        mostrar_menu()
        
        opcion = input("Selecciona una opción: ").upper().strip()
        
        if opcion == '1':
            print("\n" + "="*50)
            nombre = input("Nombre del producto a buscar: ")
            inicio = time.perf_counter()
            resultado = busqueda_lineal(productos, nombre)
            fin = time.perf_counter()
            print("Resultado:", resultado if resultado else "No encontrado")
            print(f"Tiempo de búsqueda: {fin - inicio:.6f} segundos")
            print("="*50)
            
        elif opcion == '2':
            print("\n" + "="*50)
            nombre = input("Nombre del producto a buscar: ")
            inicio = time.perf_counter()
            resultado = busqueda_binaria(productos, nombre)
            fin = time.perf_counter()
            print("Resultado:", resultado if resultado else "No encontrado")
            print(f"Tiempo de búsqueda: {fin - inicio:.6f} segundos")
            print("="*50)
            
        elif opcion == '3':
            print("\n" + "="*50)
            print("Ordenando productos por precio...")
            inicio = time.perf_counter()
            bubble_sort(productos)
            fin = time.perf_counter()
            print(f"Productos ordenados. Tiempo: {fin - inicio:.6f} segundos")
            guardar_productos_csv(productos, "ordenado_precio.csv")
            print("Archivo generado: ordenado_precio.csv")
            print("="*50)

        elif opcion == '4':
            print("\n" + "="*50)
            print("Ordenando productos por stock...")
            inicio = time.perf_counter()
            productos_ordenados = quick_sort(productos)
            fin = time.perf_counter()
            print(f"Productos ordenados. Tiempo: {fin - inicio:.6f} segundos")
            guardar_productos_csv(productos_ordenados, "ordenado_stock.csv")
            print("Archivo generado: ordenado_stock.csv")
            print("="*50)
            
        elif opcion == '5':
            print("\n¡Gracias por usar el programa! Hasta luego.")
            break
            
        else:
            print("\nOpción inválida.")
        
        # Pausa antes de mostrar el menú nuevamente
        if opcion in ['1', '2', '3', '4']:
            input("\nPresione Enter para continuar...")

if __name__ == "__main__":
    main()