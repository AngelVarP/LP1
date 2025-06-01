import sqlite3
import matplotlib.pyplot as plt

# Función para leer los datos de los alumnos desde la base de datos
def leerDatos():
    conn = sqlite3.connect("gestion_alumnos.db")
    cursor = conn.cursor()
    cursor.execute("SELECT codigo, apellido, nombre, pc1, pc2, pc3, pc4 FROM estudiantes")
    alumnos = cursor.fetchall()
    conn.close()

    # Organizar los datos
    alumnos_dict = {}
    for alumno in alumnos:
        codigo, apellido, nombre, pc1, pc2, pc3, pc4 = alumno
        notas = [pc1, pc2, pc3, pc4]
        alumnos_dict[codigo] = (f"{nombre} {apellido}", notas)
    return alumnos_dict

# Función para graficar las notas de un alumno
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

# Función para ejecutar el gráfico
def ejecutarGrafico():
    alumnos = leerDatos()
    codigo_input = input("Ingresa el código del alumno: ").strip()
    if codigo_input in alumnos:
        nombre, notas = alumnos[codigo_input]
        graficarNotas(nombre, notas)
    else:
        print("Código no encontrado.")


