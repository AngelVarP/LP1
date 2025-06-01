import pickle
from comandoVoz import voz

ARCHIVO_ALUMNOS = "alumnos.bin"
ARCHIVO_TXT = "alumnos.txt"

def guardar_txt(alumnos, ruta_txt=ARCHIVO_TXT):
    with open(ruta_txt, "w", encoding="utf-8") as f:
        f.write("Código | Apellido | Nombre | PC1 | PC2 | PC3 | PC4 | Promedio | Estado\n")
        f.write("-" * 80 + "\n")
        for a in alumnos:
            linea = (f"{a['codigo']} | {a['apellido']} | {a['nombre']} | "
                     f"{a['pc1']} | {a['pc2']} | {a['pc3']} | {a['pc4']} | "
                     f"{a['promedio']:.2f} | {a['estado']}\n")
            f.write(linea)

def eliminarAlumno():
    codigoBuscar = input("Ingrese el código del alumno a eliminar: ")

    try:
        with open(ARCHIVO_ALUMNOS, "rb") as f:
            alumnos = pickle.load(f)
    except FileNotFoundError:
        print("No hay alumnos registrados.")
        return

    alumnos_nuevos = [a for a in alumnos if a["codigo"] != codigoBuscar]

    if len(alumnos_nuevos) == len(alumnos):
        print("Alumno no encontrado.")
        voz("Alumno no encontrado.")
        return

    # Guardar los cambios
    with open(ARCHIVO_ALUMNOS, "wb") as f:
        pickle.dump(alumnos_nuevos, f)

    guardar_txt(alumnos_nuevos)

    print(f"Alumno con código {codigoBuscar} eliminado exitosamente.")
    voz(f"Alumno con código {codigoBuscar} eliminado exitosamente.")


