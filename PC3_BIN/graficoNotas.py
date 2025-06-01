import pickle
import matplotlib.pyplot as plt

ARCHIVO_ALUMNOS = "alumnos.bin"

def leerDatos():
    try:
        with open(ARCHIVO_ALUMNOS, "rb") as f:
            alumnos = pickle.load(f)
    except FileNotFoundError:
        print("No hay alumnos registrados.")
        return {}

    alumnos_dict = {}
    for alumno in alumnos:
        codigo = alumno["codigo"]
        nombre_completo = f"{alumno['nombre']} {alumno['apellido']}"
        notas = [alumno["pc1"], alumno["pc2"], alumno["pc3"], alumno["pc4"]]
        alumnos_dict[codigo] = (nombre_completo, notas)
    return alumnos_dict

def graficarNotas(nombre, notas):
    etiquetas = ['PC1', 'PC2', 'PC3', 'PC4']
    plt.figure(figsize=(8, 5))
    plt.bar(etiquetas, notas, color='dodgerblue')
    plt.title(f'Notas de {nombre}')
    plt.xlabel('Evaluaciones')
    plt.ylabel('Nota')
    plt.ylim(0, 20)
    for i, nota in enumerate(notas):
        plt.text(i, nota + 0.5, str(nota), ha='center')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

def ejecutarGrafico():
    alumnos = leerDatos()
    if not alumnos:
        return
    codigo_input = input("Ingresa el código del alumno: ").strip()
    if codigo_input in alumnos:
        nombre, notas = alumnos[codigo_input]
        graficarNotas(nombre, notas)
    else:
        print("Código no encontrado.")

