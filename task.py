# app.py - Gestor de Tareas Funcional
tareas = []

def agregar_tarea():
    titulo = input("Ingrese el título de la tarea: ").strip()
    if not titulo:
        print("Error: El título no puede estar vacío.\n")
    else:
        tareas.append({"titulo": titulo, "completada": False})
        print(f"Tarea '{titulo}' agregada con éxito.\n")

def menu():
    while True:
        print("=== GESTOR DE TAREAS ===")
        print("1. Agregar Tarea (HU01)")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            agregar_tarea()
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida.\n")

if __name__ == "__main__":
    menu()
