import pickle
from comandoVoz import voz
from menu import menu

ARCHIVO_USUARIOS_BIN = "usuarios.bin"

def cargar_usuarios():
    try:
        with open(ARCHIVO_USUARIOS_BIN, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return {}

def ingresoUsuario():
    voz("Bienvenido")
    usuarios = cargar_usuarios()
    intentos = 0

    while intentos < 3:
        usuario = input("Ingresa tu usuario: ")
        clave = input("Ingresa tu contraseña: ")

        if usuarios.get(usuario) == clave:
            print(f"Bienvenido, {usuario}.")
            voz(f"Bienvenido, {usuario}.")
            menu()  # Ejecuta el menú si credenciales válidas
            return True
        else:
            intentos += 1
            print(f"Usuario o contraseña incorrectos. Intentos restantes: {3 - intentos}")
            voz(f"Usuario o contraseña incorrectos. Intentos restantes: {3 - intentos}")

    print("Demasiados intentos fallidos. El programa se cerrará.")
    voz("Demasiados intentos fallidos. El programa se cerrará.")
    exit()
