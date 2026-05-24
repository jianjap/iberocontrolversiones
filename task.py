# task.py - Gestor de Tareas Funcional
tareas = []

def agregar_tarea():
    titulo = input("Ingrese el título de la tarea: ").strip()
    if not titulo:
        print("Error: El título no puede estar vacío.\n")
    else:
        tareas.append({"titulo": titulo, "completada": False})
        print(f"Tarea '{titulo}' agregada con éxito.\n")

# (Se añaden estas líneas al código existente en task.py)
def listar_tareas():
    if not tareas:
        print("No hay tareas registradas.\n")
    else:
        print("\n--- LISTA DE TAREAS ---")
        for i, tarea in enumerate(tareas, 1):
            estado = "[X]" if tarea["completada"] else "[ ]"
            print(f"{i}. {estado} {tarea['titulo']}")
        print()

# Modificar el menú para incluir la opción de listar tareas:
# Si el usuario presiona "2", invocar listar_tareas()
def menu():
    while True:
        print("=== GESTOR DE TAREAS ===")
        print("1. Agregar Tarea (HU01)")
        print("2. Listar Tarea (HU01)")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            agregar_tarea()
        if opcion == "2":
            listar_tareas()
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida.\n")

if __name__ == "__main__":
    menu()
