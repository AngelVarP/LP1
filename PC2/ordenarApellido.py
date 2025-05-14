from tabulate import tabulate
from comandoVoz import voz

def ordenarPorApellido():
    # Leer los datos del archivo lista.txt
    with open("lista.txt", "r") as file:
        lines = file.readlines()

    # Eliminar la primera línea (encabezado) antes de ordenar
    encabezado = lines[0]
    lines = lines[1:]

    # Ordenar los alumnos por apellido (está en la segunda columna)
    lines_sorted = sorted(lines, key=lambda x: x.split(" | ")[1])

    # Mostrar el reporte con tabulate
    voz("mostrando reporte de Alumnos (Ordenado por Apellido):")
    print("\nReporte de Alumnos (Ordenado por Apellido):")
    print(tabulate([encabezado.strip().split(" | ")] + [line.strip().split(" | ") for line in lines_sorted], headers=["Código", "Apellido", "Nombre", "PC1", "PC2", "PC3", "PC4", "Promedio", "Estado"], tablefmt="grid"))
    