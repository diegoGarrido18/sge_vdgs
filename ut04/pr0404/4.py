
# Diccionario inicial
asignaturas = {
    "Matemáticas": ["Ana", "Carlos", "Luis", "María", "Jorge"],
    "Física": ["Elena", "Luis", "Juan", "Sofía"],
    "Programación": ["Ana", "Carlos", "Sofía", "Jorge", "Pedro"],
    "Historia": ["María", "Juan", "Elena", "Ana"],
    "Inglés": ["Carlos", "Sofía", "Jorge", "María"],
}

def listar_estudiantes():
    asignatura = input("Introduce la asignatura: ")
    if asignatura in asignaturas:
        print(f"Estudiantes matriculados en {asignatura}: {', '.join(asignaturas[asignatura])}")
    else:
        print("Esa asignatura no existe.")

def matricular_estudiante():
    asignatura = input("Introduce la asignatura: ")
    if asignatura in asignaturas:
        estudiante = input("Introduce el nombre del estudiante: ")
        if estudiante not in asignaturas[asignatura]:
            asignaturas[asignatura].append(estudiante)
            print(f"{estudiante} ha sido matriculado en {asignatura}.")
        else:
            print(f"{estudiante} ya está matriculado en {asignatura}.")
    else:
        print("Esa asignatura no existe.")

def dar_baja_estudiante():
    asignatura = input("Introduce la asignatura: ")
    if asignatura in asignaturas:
        estudiante = input("Introduce el nombre del estudiante: ")
        if estudiante in asignaturas[asignatura]:
            asignaturas[asignatura].remove(estudiante)
            print(f"{estudiante} ha sido dado de baja en {asignatura}.")
        else:
            print(f"{estudiante} no está matriculado en {asignatura}.")
    else:
        print("Esa asignatura no existe.")

def menu():
    while True:
        print("\n--- Menú ---")
        print("1. Listar estudiantes matriculados en una asignatura")
        print("2. Matricular un estudiante en una asignatura")
        print("3. Dar de baja un estudiante de una asignatura")
        print("4. Salir")
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            listar_estudiantes()
        elif opcion == "2":
            matricular_estudiante()
        elif opcion == "3":
            dar_baja_estudiante()
        elif opcion == "4":
            print("Saliendo... hasta luego.")
            break
        else:
            print("Opción no válida.")

# Ejecutamos el menú
menu()