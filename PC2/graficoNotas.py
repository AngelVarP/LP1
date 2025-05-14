import matplotlib.pyplot as plt

def leerDatos(ruta):
    alumnos = {}
    with open(ruta, "r", encoding="utf-8") as f:
        next(f)  # Saltar encabezado
        for linea in f:
            partes = [p.strip() for p in linea.strip().split("|")]
            if len(partes) >= 8:
                codigo = partes[0]
                nombre = f"{partes[2]} {partes[1]}"  # Nombre Apellido
                notas = list(map(float, partes[3:7]))
                alumnos[codigo] = (nombre, notas)
    return alumnos

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
    alumnos = leerDatos("lista.txt")
    codigo_input = input("Ingresa el código del alumno: ").strip()
    if codigo_input in alumnos:
        nombre, notas = alumnos[codigo_input]
        graficarNotas(nombre, notas)
    else:
        print("Código no encontrado.")
