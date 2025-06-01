import pickle
from tabulate import tabulate
from comandoVoz import voz

ARCHIVO_ALUMNOS = "alumnos.bin"

def buscarAlumno():
    codigoBuscar = input("Ingrese el código del alumno a buscar: ")
    
    try:
        with open(ARCHIVO_ALUMNOS, "rb") as f:
            alumnos = pickle.load(f)
    except FileNotFoundError:
        print("No hay alumnos registrados.")
        return

    alumnoEncontrado = None
    for alumno in alumnos:
        if alumno["codigo"] == codigoBuscar:
            alumnoEncontrado = alumno
            break

    if alumnoEncontrado:
        print("\nAlumno encontrado:")
        voz("Alumno encontrado")
        print(tabulate([[
            alumnoEncontrado["codigo"],
            alumnoEncontrado["apellido"],
            alumnoEncontrado["nombre"],
            alumnoEncontrado["pc1"],
            alumnoEncontrado["pc2"],
            alumnoEncontrado["pc3"],
            alumnoEncontrado["pc4"],
            f"{alumnoEncontrado['promedio']:.2f}",
            alumnoEncontrado["estado"]
        ]], headers=["Código", "Apellido", "Nombre", "PC1", "PC2", "PC3", "PC4", "Promedio", "Estado"], tablefmt="grid"))
    else:
        print("Alumno no encontrado.")


