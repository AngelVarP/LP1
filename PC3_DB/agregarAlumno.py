import sqlite3
from comandoVoz import voz

# Conectar a la base de datos
def conectar_db():
    return sqlite3.connect("gestion_Alumnos.db")

# Crear la tabla de alumnos si no existe
def crearTabla():
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS estudiantes (
                        codigo TEXT PRIMARY KEY,
                        apellido TEXT,
                        nombre TEXT,
                        pc1 REAL,
                        pc2 REAL,
                        pc3 REAL,
                        pc4 REAL,
                        promedio REAL,
                        estado TEXT)''')
    conn.commit()
    conn.close()

# Función para generar el código del alumno con módulo 11
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

# Función para ingresar una nota válida
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

# Verificar existencia del alumno en la base de datos
def verificarExistencia(codigo):
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM estudiantes WHERE codigo = ?", (codigo,))
    if cursor.fetchone():
        conn.close()
        return True
    conn.close()
    return False

# Función para agregar un alumno
def agregarAlumno():
    crearTabla()  # Crear las tablas si no existen

    while True:
        codigo = input("Ingrese el codigo del alumno (6 dígitos): ")

        if len(codigo) != 6 or not codigo.isdigit():
            print("El código debe ser de 6 dígitos.")
            continue

        if verificarExistencia(codigo):
            print("Ese código ya existe")
            continue

        # Generar el código con Módulo 11
        newCodigo = modulo11(codigo)
        apellido = input("Apellido del alumno: ")
        nombre = input("Nombre del alumno: ")

        pc1 = validarNota("Nota PC1")
        pc2 = validarNota("Nota PC2")
        pc3 = validarNota("Nota PC3")
        pc4 = validarNota("Nota PC4")

        notas = [pc1, pc2, pc3, pc4]
        notas.remove(min(notas))  
        promedio = sum(notas) / 3  
        estado = "Aprobado" if promedio >= 10 else "Desaprobado"

        # Insertar el nuevo alumno en la base de datos SQLite
        conn = conectar_db()
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO estudiantes (codigo, apellido, nombre, pc1, pc2, pc3, pc4, promedio, estado)
                         VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''', 
                      (newCodigo, apellido, nombre, pc1, pc2, pc3, pc4, promedio, estado))
        conn.commit()
        conn.close()

        print(f"Alumno {nombre} {apellido} agregado con éxito. Codigo: {newCodigo}")
        voz(f"Alumno {nombre} {apellido} agregado con éxito. Codigo: {newCodigo}")
        
        break

