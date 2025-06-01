import sqlite3
from comandoVoz import voz


# Función para conectar a la base de datos SQLite
def conectar_db():
    return sqlite3.connect("gestion_alumnos.db")

# Función para cargar los usuarios desde la base de datos
def cargarUsuarios():
    usuarios = {}
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("SELECT usuario, contrasena FROM usuarios")
    rows = cursor.fetchall()
    conn.close()

    for row in rows:
        usuario, contrasena = row
        usuarios[usuario] = contrasena

    return usuarios


# Función para crear la tabla de usuarios si no existe
def crearTablaUsuarios():
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                        usuario TEXT PRIMARY KEY,
                        contrasena TEXT)''')
    conn.commit()
    conn.close()


# Función para agregar un usuario si no existe en la base de datos
def agregarNuevoUsuario():
    crearTablaUsuarios()  # Asegurarse de que la tabla de usuarios exista

    usuario = input("Ingrese un nuevo nombre de usuario: ")
    contrasena = input("Ingrese una nueva contraseña: ")

    # Verificar si el usuario ya existe
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE usuario = ?", (usuario,))
    if cursor.fetchone():
        print("El usuario ya existe. Intenta con otro nombre.")
        voz("El usuario ya existe. Intenta con otro nombre.")
        conn.close()
    else:
        # Si el usuario no existe, agregarlo
        agregarUsuario(usuario, contrasena)
        conn.close()

# Función para agregar un nuevo usuario a la base de datos
def agregarUsuario(usuario, contrasena):
    conn = conectar_db()
    cursor = conn.cursor()
    # Insertar un nuevo usuario en la tabla de usuarios
    cursor.execute('''INSERT INTO usuarios (usuario, contrasena)
                     VALUES (?, ?)''', (usuario, contrasena))
    conn.commit()
    conn.close()
    print(f"Usuario {usuario} agregado con éxito.")
    voz(f"Usuario {usuario} agregado con éxito.")

