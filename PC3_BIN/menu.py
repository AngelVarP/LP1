from agregarAlumno import agregarAlumno
from mostrarReporte import reporte
from buscarAlumno import buscarAlumn
from comandoVoz import voz
from eliminarAlumno import eliminarAlumno
from ordenarApellido import ordenarPorApellido
from graficoNotas import ejecutarGrafico
from validacionUsuario import agregarNuevoUsuario

def menu():
    while True:
        print("\nMenú de opciones:")
        print("1. Agregar alumno")
        print("2. Buscar alumno")
        print("3. Eliminar alumno")
        print("4. Mostrar reporte de alumnos")
        print("5. Mostrar reporte de alumnos por apellido")
        print("6. Mostrar gráfico de barras")
        print("7. Agregar nuevo usuario")
        print("8. Salir")
        
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            agregarAlumno()
        elif opcion == "2":
            buscarAlumn()
        elif opcion == "3":
            eliminarAlumno()
        elif opcion == "4":
            reporte()
        elif opcion == "5":    
            ordenarPorApellido()
        elif opcion == "6":
            ejecutarGrafico()
        elif opcion == "7":
            agregarNuevoUsuario()
        elif opcion == "8":
            print("\nPrograma finalizado...")
            voz("Programa finalizado")
            break
        else:
            print("Opción no válida, intenta nuevamente.")