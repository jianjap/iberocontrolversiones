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

# Se agrega la funcionalidad de marcar tareas
def marcar_completada():
    """HU03: Marcar Tarea como Completada"""
    if not tareas:
        print("No hay tareas registradas para modificar.\n")
        return
    
    try:
        indice = int(input("Ingrese el número de la tarea a marcar como completada: ")) - 1
        if 0 <= indice < len(tareas):
            if tareas[indice]["completada"]:
                print(f"La tarea '{tareas[indice]['titulo']}' ya se encuentra completada.\n")
            else:
                tareas[indice]["completada"] = True
                print(f"Tarea '{tareas[indice]['titulo']}' marcada como completada [X] con éxito.\n")
        else:
            print("Error: El número de tarea ingresado no existe.\n")
    except ValueError:
        print("Error: Por favor, ingrese un número entero válido.\n")

# Se agrega la funcionalidad de eliminar tareas
def eliminar_tarea():
    """HU04: Eliminar Tarea"""
    if not tareas:
        print("No hay tareas registradas para eliminar.\n")
        return
        
    try:
        indice = int(input("Ingrese el número de la tarea que desea eliminar: ")) - 1
        if 0 <= indice < len(tareas):
            tarea_eliminada = tareas.pop(indice)
            print(f"Tarea '{tarea_eliminada['titulo']}' eliminada correctamente.\n")
        else:
            print("Error: El número de tarea ingresado no existe.\n")
    except ValueError:
        print("Error: Por favor, ingrese un número entero válido.\n")        

# Se agrega la funiconalidad de filtrar tareas
def filtrar_tarea():
    """HU05: Filtrar por Estado"""
    if not tareas:
        print("No hay tareas registradas para filtrar.\n")
        return
        
    print("--- OPCIONES DE FILTRADO ---")
    print("1. Ver solo tareas Pendientes")
    print("2. Ver solo tareas Completadas")
    opcion_filtro = input("Seleccione una opción: ").strip()
    
    if opcion_filtro == "1":
        pendientes = [t for t in tareas if not t["completada"]]
        if not pendientes:
            print("No existen tareas pendientes en este momento.\n")
        else:
            print("\n--- TAREAS PENDIENTES ---")
            for i, tarea in enumerate(pendientes, 1):
                print(f"{i}. [ ] {tarea['titulo']}")
            print()
            
    elif opcion_filtro == "2":
        completadas = [t for t in tareas if t["completada"]]
        if not completadas:
            print("No existen tareas completadas en este momento.\n")
        else:
            print("\n--- TAREAS COMPLETADAS ---")
            for i, tarea in enumerate(completadas, 1):
                print(f"{i}. [X] {tarea['titulo']}")
            print()
    else:
        print("Opción de filtrado inválida.\n")

# Definir menu de tareas
def menu():
    while True:
        print("=== GESTOR DE TAREAS ===")
        print("1. Agregar Tarea (HU01)")
        print("2. Listar Tarea (HU02)")
        print("3. Marcar Tarea (HU03)")
        print("4. Eliminar Tarea (HU04)")
        print("5. Filtrar Tarea (HU05)")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            agregar_tarea()
        if opcion == "2":
            listar_tareas()
        if opcion == "3":
            marcar_completada()
        if opcion == "4":
            eliminar_tarea()
        if opcion == "5":
            filtrar_tarea()
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida.\n")

if __name__ == "__main__":
    menu()
