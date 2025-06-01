import pickle
from comandoVoz import voz

ARCHIVO_USUARIOS_BIN = "usuarios.bin"
ARCHIVO_USUARIOS_TXT = "usuarios.txt"

def cargar_usuarios():
    try:
        with open(ARCHIVO_USUARIOS_BIN, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return {}  # Diccionario vacío si no existe el archivo

def guardar_usuarios(usuarios):
    with open(ARCHIVO_USUARIOS_BIN, "wb") as f:
        pickle.dump(usuarios, f)

def guardar_txt_usuarios(usuarios, ruta_txt=ARCHIVO_USUARIOS_TXT):
    with open(ruta_txt, "w", encoding="utf-8") as f:
        f.write("Usuario | Contraseña\n")
        f.write("-" * 30 + "\n")
        for usuario, contrasena in usuarios.items():
            f.write(f"{usuario} | {contrasena}\n")

def crearTablaUsuarios():
    # No hace nada aquí porque con archivos binarios no necesitas crear tablas
    pass

def agregarNuevoUsuario():
    usuarios = cargar_usuarios()

    usuario = input("Ingrese un nuevo nombre de usuario: ")
    contrasena = input("Ingrese una nueva contraseña: ")

    if usuario in usuarios:
        print("El usuario ya existe. Intenta con otro nombre.")
        voz("El usuario ya existe. Intenta con otro nombre.")
    else:
        usuarios[usuario] = contrasena
        guardar_usuarios(usuarios)
        guardar_txt_usuarios(usuarios)
        print(f"Usuario {usuario} agregado con éxito.")
        voz(f"Usuario {usuario} agregado con éxito.")


