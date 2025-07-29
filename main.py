ESTADO_COMPLETADA="✔️ "
ESTADO_PENDIENTE="❌"

tareas = []

#Ver tareas
def mostrar_tareas():
    if not tareas:
        print("No hay tareas pendientes.")
        return
    
    print("Tareas pendientes:")
    for i, tarea in enumerate(tareas):
        estado = ESTADO_COMPLETADA if tarea["completada"] else ESTADO_PENDIENTE
        print(f"{i + 1}. {tarea['nombre']} [{estado}]")
    print("----------------------------\n")

#Añadir tarea
def añadir_tarea():
    nombre = input("Introduce el nombre de la tarea: ")
    if nombre.strip():
        tareas.append({"nombre": nombre, "completada": False})
        print(f"Tarea '{nombre}' añadida con éxito.\n")
    else:
        print("El nombre de la tarea no puede estar vacío.\n")

#Marcar tarea como completada
def marcar_tarea_completada():
    mostrar_tareas()
    if not tareas:
        return
    
    try:
        indice = int(input("Introduce el número de la tarea a marcar como completada: "))
        if 1 <= indice <= len(tareas):
            tarea_seleccionada = tareas[indice - 1]
            if tarea_seleccionada["completada"]:
                print(f"La tarea '{tarea_seleccionada['nombre']}' ya estaba completada.\n")
            else:
                tarea_seleccionada["completada"] = True
                print(f"Tarea '{tarea_seleccionada['nombre']}' marcada como completada.\n")
        else:
            print("Número de tarea inválido.\n")
    except ValueError:
        print("Por favor, introduce un número válido.\n")

#Eliminar tarea
def eliminar_tarea():
    mostrar_tareas()
    if not tareas:
        return
    
    try:
        indice = int(input("Introduce el número de la tarea a eliminar: "))
        if 1 <= indice <= len(tareas):
            tarea_eliminada = tareas.pop(indice - 1)
            print(f"Tarea '{tarea_eliminada['nombre']}' eliminada con éxito.\n")
        else:
            print("Número de tarea inválido.\n")
    except ValueError:
        print("Por favor, introduce un número válido.\n")

# Eliminar todas las tareas completadas
def eliminar_completadas():
    global tareas
    # Contamos cuántas tareas hay antes de eliminar
    num_tareas_antes = len(tareas)
    # Creamos una nueva lista solo con las tareas pendientes
    tareas = [tarea for tarea in tareas if not tarea["completada"]]
    if len(tareas) < num_tareas_antes:
        print("Todas las tareas completadas han sido eliminadas.\n")
    else:
        print("No había tareas completadas para eliminar.\n")

#Salir
def salir():
    print("¡Hasta luego!")
    exit()

# Bucle principal del programa
def main():
    print("¡Bienvenido a tu lista de tareas!")
    while True:
        print("\n¿Qué te gustaría hacer?")
        print("1. Ver tareas")
        print("2. Añadir tarea")
        print("3. Marcar tarea como completada")
        print("4. Eliminar tarea específica")
        print("5. Eliminar todas las tareas completadas")
        print("6. Salir")

        opcion = input("Elige una opción (1-6): ")
        if opcion == '1':
            mostrar_tareas()
        elif opcion == '2':
            añadir_tarea()
        elif opcion == '3':
            marcar_tarea_completada()
        elif opcion == '4':
            eliminar_tarea()
        elif opcion == '5':
            eliminar_completadas()
        elif opcion == '6':
        if opcion == '6':
            opciones[opcion]()
        else:
            print("Opción no válida. Por favor, elige un número del 1 al 6.\n")

if __name__ == "__main__":
    main()
