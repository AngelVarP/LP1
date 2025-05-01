from tabulate import tabulate
from comandoVoz import voz

# Función para buscar un alumno por su código
def buscarAlumno():
    codigoBuscar = input("Ingrese el código del alumno a buscar: ")

    # Leer los datos del archivo lista.txt
    with open("lista.txt", "r") as file:
        lines = file.readlines()

    # Buscar el alumno por el código
    alumnoEncontrado = None
    for line in lines:
        if line.startswith(codigoBuscar):  # Si el código coincide
            alumnoEncontrado = line.strip().split(" | ")
            break
    
    if alumnoEncontrado:
        print("\nAlumno encontrado:")
        voz("Alumno encontrado")
        print(tabulate([alumnoEncontrado], headers=["Código", "Apellido", "Nombre", "PC1", "PC2", "PC3", "PC4", "Promedio", "Estado"], tablefmt="grid"))
    else:
        print("Alumno no encontrado.")