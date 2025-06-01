import sqlite3
from tabulate import tabulate
from comandoVoz import voz

# Función para mostrar el reporte de alumnos desde la base de datos
def reporte():
    conn = sqlite3.connect("gestion_alumnos.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM estudiantes")
    alumnos = cursor.fetchall()
    conn.close()

    if alumnos:
        print("\nReporte de Alumnos:")
        voz("mostrando reporte de Alumnos")
        print(tabulate(alumnos, headers=["Código", "Apellido", "Nombre", "PC1", "PC2", "PC3", "PC4", "Promedio", "Estado"], tablefmt="grid"))
    else:
        print("No hay alumnos registrados.")
