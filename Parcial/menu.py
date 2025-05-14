from agregarUsuario import agregarUsuario
from agregarAlumno import agregarAlumno
from mostrarReporte import reporte
from buscarAlumno import buscarAlumno
from comandoVoz import voz
from eliminarAlumno import eliminarAlumno
from ordenarApellido import ordenarPorApellido

# Menu de opciones, una vez validado el ingreso de usuario
def menu():
    while True:
        print("\nMenú de opciones:")
        print("1. Agregar alumno")
        print("2. Buscar alumno")
        print("3. Eliminar alumno")
        print("4. Mostrar reporte de alumno")
        print("5. Mostrar reporte de alumnos por apellido")
        print("6. Agregar usuario")
        print("7. Salir")
        
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            agregarAlumno()
        elif opcion == "2":
            buscarAlumno()
        elif opcion == "3":
            eliminarAlumno()
        elif opcion == "4":
            reporte()
        elif opcion == "5":    
            ordenarPorApellido()
        elif opcion == "6":
            agregarUsuario()
        elif opcion == "7":
            print("\nPrograma finalizado...")
            voz("Programa finalizado")
            break
        else:
            print("Opción no válida, intenta nuevamente.")