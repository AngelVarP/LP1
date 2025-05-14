from comandoVoz import voz
from validacionUsuario import cargarUsuarios
from validacionUsuario import validarRostro
from menu import menu

# Funcion para el ingreso de usuarios
def ingresoUsuario():
    voz("Bienvenido")
    usuarios = cargarUsuarios()
    if not usuarios:
        return False  # No se cargaron usuarios

    # Inicializar contador de intentos
    intentos = 0
    while intentos < 3:
        print("\n")
        # Solicitar al usuario su nombre y contraseña
        usuario = input("Ingresa tu usuario: ")
        clave = input("Ingresa tu contraseña: ")

        # Verificar si el usuario y la contraseña coinciden
        if usuario in usuarios and usuarios[usuario] == clave:
            # Llave maestra (caso especial)
            if usuario == "user1" and clave == "100":
                print(f"Bienvenido, {usuario}. Saltando la validación facial.")
                voz(f"Bienvenido, {usuario}. Saltando la validación facial.")
                # Llamar al menú directamente
                menu()
                return True 
            
            voz("Bienvenido usuario. Estamos validando su rostro. Espere un momento por favor.")
             # Validación de rostro
            if  validarRostro(usuario):
                # Mensaje si la validacion facil es exitosa
                print(f"Bienvenido, {usuario}.")
                voz(f"Bienvenido, {usuario}.")
                # Llamar al menú despues de un inicio exitoso
                menu()
                return True
            else:
                # Mensaje si falla la validación facial
                print(f"No se ha podido verificar el rostro. Intentos restantes: {2 - intentos}")
                voz(f"No se ha podido verificar el rostro. Intentos restantes: {2 - intentos}")
                intentos += 1
        else:
            # Mensaje si falla la validación de usuario o contraseña
            print(f"Usuario o contraseña incorrectos. Intentos restantes: {2 - intentos}")
            voz(f"Usuario o contraseña incorrectos. Intentos restantes: {2 - intentos}")
            intentos += 1
            
    # Si el numero de intentos supera 3, finaliza el proceso        
    print("Demasiados intentos fallidos. El programa finalizará.")
    voz("Demasiados intentos fallidos. El programa finalizará.")
    return False