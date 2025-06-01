import sqlite3
from comandoVoz import voz
from validacionUsuario import cargarUsuarios
from menu import menu
from validacionUsuario import conectar_db

# Función para la validación del usuario
def ingresoUsuario():
    voz("Bienvenido")
    
    conn = conectar_db()
    cursor = conn.cursor()
    
    # Límite de intentos fallidos
    intentos = 0

    while intentos < 3:
        # Solicitar el usuario y la contraseña
        usuario = input("Ingresa tu usuario: ")
        clave = input("Ingresa tu contraseña: ")

        # Verificar si el usuario y la contraseña coinciden
        cursor.execute("SELECT * FROM usuarios WHERE usuario = ? AND contrasena = ?", (usuario, clave))
        
        if cursor.fetchone():
            print(f"Bienvenido, {usuario}.")
            voz(f"Bienvenido, {usuario}.")
            conn.close()
            
            # Llamar a la función menu() si las credenciales son correctas
            menu()  # Asumo que esta función está definida en otro lugar de tu código
            return True
        else:
            intentos += 1
            print(f"Usuario o contraseña incorrectos. Intentos restantes: {3 - intentos}")
            voz(f"Usuario o contraseña incorrectos. Intentos restantes: {3 - intentos}")

    print("Demasiados intentos fallidos. El programa se cerrará.")
    voz("Demasiados intentos fallidos. El programa se cerrará.")
    conn.close()
    exit()  # Finaliza el