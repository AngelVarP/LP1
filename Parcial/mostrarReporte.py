from tabulate import tabulate
from comandoVoz import voz

# Función para mostrar el reporte de alumnos con tabulate
def reporte():
    # Leer los datos del archivo lista.txt
    with open("lista.txt", "r") as file:
        lines = file.readlines()
    
    lines = lines[1:]

    # Mostrar el reporte con tabulate
    print("\nReporte de Alumnos:")
    voz("mostrando reporte de Alumnos")
    print(tabulate([line.strip().split(" | ") for line in lines], headers=["Código", "Apellido", "Nombre", "PC1", "PC2", "PC3", "PC4", "Promedio", "Estado"], tablefmt="grid"))