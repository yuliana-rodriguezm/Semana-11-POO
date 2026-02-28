# SISTEMA DE GESTIÓN DE COSMÉTICOS - INTERFAZ DE USUARIO

from servicios.inventario import Inventario

def menu():
    inventario = Inventario()

    while True:
        print("\n===== SISTEMA DE COSMÉTICOS =====")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar por nombre")
        print("5. Mostrar todos")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            inventario.agregar_producto()
        elif opcion == "2":
            inventario.eliminar_producto()
        elif opcion == "3":
            inventario.actualizar_producto()
        elif opcion == "4":
            inventario.buscar_por_nombre()
        elif opcion == "5":
            inventario.mostrar_todos()
        elif opcion == "6":
            print("👋 Saliendo del sistema...")
            break
        else:
            print("⚠️ Opción inválida.")


if __name__ == "__main__":
    menu()