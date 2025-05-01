from agregarAlumno import agregarAlumno
from mostrarReporte import reporte
from buscarAlumno import buscarAlumno
from comandoVoz import voz
from eliminarAlumno import eliminarAlumno

def menu():
    while True:
        print("\nMenú de opciones:")
        print("1. Agregar alumno")
        print("2. Buscar alumno")
        print("3. Eliminar alumno")
        print("4. Ordenar por apellidos")
        print("5. Mostrar reporte de alumnos")
        print("6. Salir")
        
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            agregarAlumno()
        elif opcion == "2":
            buscarAlumno()
        elif opcion == "3":
            eliminarAlumno()
        elif opcion == "4":
            pass
        elif opcion == "5":
            reporte()
        elif opcion == "6":
            print("\nPrograma finalizado...")
            voz("Programa finalizado")
            break
        else:
            print("Opción no válida, intenta nuevamente.")