import pickle
from tabulate import tabulate
from comandoVoz import voz

ARCHIVO_ALUMNOS = "alumnos.bin"

def reporte():
    try:
        with open(ARCHIVO_ALUMNOS, "rb") as f:
            alumnos = pickle.load(f)
    except FileNotFoundError:
        print("No hay alumnos registrados.")
        return

    if alumnos:
        print("\nReporte de Alumnos:")
        voz("mostrando reporte de Alumnos")
        # Preparar datos para tabulate como lista de listas
        datos = []
        for a in alumnos:
            datos.append([
                a["codigo"],
                a["apellido"],
                a["nombre"],
                a["pc1"],
                a["pc2"],
                a["pc3"],
                a["pc4"],
                f"{a['promedio']:.2f}",
                a["estado"]
            ])
        print(tabulate(datos, headers=["Código", "Apellido", "Nombre", "PC1", "PC2", "PC3", "PC4", "Promedio", "Estado"], tablefmt="grid"))
    else:
        print("No hay alumnos registrados.")

