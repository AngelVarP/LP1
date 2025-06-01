import sqlite3
from tabulate import tabulate
from comandoVoz import voz

def buscarAlumno():
    codigoBuscar = input("Ingrese el código del alumno a buscar: ")

    conn = sqlite3.connect("gestion_alumnos.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM estudiantes WHERE codigo = ?", (codigoBuscar,))
    alumnoEncontrado = cursor.fetchone()

    if alumnoEncontrado:
        print("\nAlumno encontrado:")
        voz("Alumno encontrado")
        print(tabulate([alumnoEncontrado], headers=["Código", "Apellido", "Nombre", "PC1", "PC2", "PC3", "PC4", "Promedio", "Estado"], tablefmt="grid"))
    else:
        print("Alumno no encontrado.")
    conn.close()
