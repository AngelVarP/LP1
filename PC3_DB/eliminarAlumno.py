import sqlite3
from comandoVoz import voz

def eliminarAlumno():
    codigoBuscar = input("Ingrese el código del alumno a eliminar: ")

    conn = sqlite3.connect("gestion_alumnos.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM estudiantes WHERE codigo = ?", (codigoBuscar,))
    conn.commit()

    if cursor.rowcount > 0:
        print(f"Alumno con código {codigoBuscar} eliminado exitosamente.")
        voz(f"Alumno con código {codigoBuscar} eliminado exitosamente.")
    else:
        print("Alumno no encontrado.")
    conn.close()
