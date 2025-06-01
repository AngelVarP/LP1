import pickle
from comandoVoz import voz

ARCHIVO_ALUMNOS = "alumnos.bin"
ARCHIVO_TXT = "alumnos.txt"

def cargar_alumnos():
    try:
        with open(ARCHIVO_ALUMNOS, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return []

def guardar_alumnos(alumnos):
    with open(ARCHIVO_ALUMNOS, "wb") as f:
        pickle.dump(alumnos, f)

def guardar_txt(alumnos, ruta_txt=ARCHIVO_TXT):
    with open(ruta_txt, "w", encoding="utf-8") as f:
        f.write("Código | Apellido | Nombre | PC1 | PC2 | PC3 | PC4 | Promedio | Estado\n")
        f.write("-" * 80 + "\n")
        for a in alumnos:
            linea = (f"{a['codigo']} | {a['apellido']} | {a['nombre']} | "
                     f"{a['pc1']} | {a['pc2']} | {a['pc3']} | {a['pc4']} | "
                     f"{a['promedio']:.2f} | {a['estado']}\n")
            f.write(linea)

def validarNota(nota):
    while True:
        try:
            valorNota = float(input(f"Ingrese la {nota} (0-20): "))
            if 0 <= valorNota <= 20:
                return valorNota
            else:
                print("La nota debe estar entre 0 y 20. Inténtalo de nuevo.")
        except ValueError:
            print("Entrada inválida. Debe ingresar un número entre 0 y 20.")

def modulo11(codigo):
    t = 1
    aux = int(codigo)
    suma = 0
    while t <= 6:
        digito = aux % 10
        peso = 8 - t
        suma += peso * digito
        aux = aux // 10
        t += 1

    mod11 = suma % 11
    equivalencias = ["0", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    return codigo + equivalencias[mod11]

def verificarExistencia(codigo, alumnos):
    for alumno in alumnos:
        if alumno["codigo"] == codigo:
            return True
    return False

def agregarAlumno():
    alumnos = cargar_alumnos()

    while True:
        codigo = input("Ingrese el código del alumno (6 dígitos): ")
        if len(codigo) != 6 or not codigo.isdigit():
            print("El código debe ser de 6 dígitos numéricos.")
            continue

        newCodigo = modulo11(codigo)

        if verificarExistencia(newCodigo, alumnos):
            print(f"El código {newCodigo} ya existe.")
            continue

        apellido = input("Apellido del alumno: ")
        nombre = input("Nombre del alumno: ")

        pc1 = validarNota("Nota PC1")
        pc2 = validarNota("Nota PC2")
        pc3 = validarNota("Nota PC3")
        pc4 = validarNota("Nota PC4")

        notas = [pc1, pc2, pc3, pc4]
        notas.remove(min(notas))  # Quitar la nota más baja
        promedio = sum(notas) / 3
        estado = "Aprobado" if promedio >= 10 else "Desaprobado"

        nuevo_alumno = {
            "codigo": newCodigo,
            "apellido": apellido,
            "nombre": nombre,
            "pc1": pc1,
            "pc2": pc2,
            "pc3": pc3,
            "pc4": pc4,
            "promedio": promedio,
            "estado": estado
        }

        alumnos.append(nuevo_alumno)
        guardar_alumnos(alumnos)    # Guarda binario
        guardar_txt(alumnos)        # Guarda archivo texto legible

        print(f"Alumno {nombre} {apellido} agregado con éxito. Código: {newCodigo}")
        voz(f"Alumno {nombre} {apellido} agregado con éxito. Código: {newCodigo}")
        break



