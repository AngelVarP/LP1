import sqlite3
from tabulate import tabulate
from comandoVoz import voz

# Función para ordenar los alumnos por apellido desde la base de datos
def ordenarPorApellido():
    conn = sqlite3.connect("gestion_alumnos.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM estudiantes")
    alumnos = cursor.fetchall()
    conn.close()

    if alumnos:
        # Ordenar por apellido (está en la segunda columna)
        alumnos_sorted = sorted(alumnos, key=lambda x: x[1])

        print("\nReporte de Alumnos (Ordenado por Apellido):")
        voz("mostrando reporte de Alumnos (Ordenado por Apellido):")
        print(tabulate(alumnos_sorted, headers=["Código", "Apellido", "Nombre", "PC1", "PC2", "PC3", "PC4", "Promedio", "Estado"], tablefmt="grid"))
    else:
        print("No hay alumnos registrados.")
