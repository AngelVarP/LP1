from comandoVoz import voz

def cargarUsuarios():
    # Diccionario para almacenar los datos
    usuarios = {}
    try:
        with open("usuarios.txt", "r") as file:
            for line in file:
                usuario, contrasena = line.strip().split(",")
                usuarios[usuario] = contrasena
    except FileNotFoundError:
        voz("El archivo usuarios.txt no se encuentra.")
        print("El archivo usuarios.txt no se encuentra.")
    return usuarios

def ingresoUsuario():
    voz("Bienvenido")
    usuarios = cargarUsuarios()
    if not usuarios:
        return False  # No se cargaron usuarios

    intentos = 0
    while intentos < 3:
        print("\n")
        usuario = input("Ingresa tu usuario: ")
        clave = input("Ingresa tu contraseña: ")

        # Verificar si el usuario y la contraseña coinciden
        if usuario in usuarios and usuarios[usuario] == clave:
            print(f"Bienvenido, {usuario}.")
            voz(f"Bienvenido, {usuario}.")
            return True
        else:
            print(f"Usuario o contraseña incorrectos. Intentos restantes: {2 - intentos}")
            voz(f"Usuario o contraseña incorrectos. Intentos restantes: {2 - intentos}")
            intentos += 1
    print("Demasiados intentos fallidos. El programa finalizará.")
    voz("Demasiados intentos fallidos. El programa finalizará.")
    return False

