import os
import cv2
import imutils
from validacionUsuario import cargarUsuarios
from validacionUsuario import obtenerRutaFotos
from comandoVoz import voz
from entrenarReconocimiento import entrenar
from comandoVoz import voz

# Funcion para agregar usuarios 
def agregarUsuario():
    # Cargar usuarios existentes
    usuarios = cargarUsuarios()
    voz("Agregar nuevo usuario")

    while True:
        # Solicitar nombre de usuario
        nuevoUsuario = input("Ingresa el nombre de usuario: ")

        # Verificar si el usuario ya existe
        if nuevoUsuario in usuarios:
            print("Este usuario ya existe. Intenta con otro nombre.")
        else:
            # Si el usuario no existe, salir del bucle
            break
    

    # Solicitar la contraseña del nuevo usuario
    nuevaClave = input("Ingresa la contraseña: ")

    # Crear una carpeta para almacenar las fotos del nuevo usuario
    persona = nuevoUsuario
    personaPath = os.path.join(obtenerRutaFotos(),persona)
    if not os.path.exists(personaPath):
        os.makedirs(personaPath)

    # Iniciar la captura del rostro
    cap = cv2.VideoCapture(0)
    faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    print("Capturando rostro. Mantente bien posicionado.")
    voz("Capturando rostro. Mantente bien posicionado.")

    count = 0 # Contador de imagenes capturadas

    # Bucle para capturar las fotos
    while count < 300:
        ret, frame = cap.read()
        if not ret:
            break

        # Dimensionar el frame
        frame = imutils.resize(frame, width=840)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detectar rostro en el frame
        faces = faceClassif.detectMultiScale(gray, 1.3, 5)
        
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            rostro = frame[y:y + h, x:x + w]
            rostro = cv2.resize(rostro, (120, 120), interpolation=cv2.INTER_CUBIC)
            cv2.imwrite(f"{personaPath}/rostro_{count}.jpg", rostro)
            count += 1

        cv2.imshow("Captura de rostro", frame)
        if cv2.waitKey(1) == 27 or count >= 300:
            break
    
    # Liberar la camara y cerrar las ventanas
    cap.release()
    cv2.destroyAllWindows()

    # Guardar usuario y contraseña en el archivo usuarios.txt
    with open("usuarios.txt", "a") as file:
        file.write(f"{nuevoUsuario},{nuevaClave}\n")

    # Confirmación de que el usuario se agrego correctamente
    print(f"Usuario {nuevoUsuario} agregado con éxito.")
    voz(f"Usuario {nuevoUsuario} agregado con éxito.")

    # Entrenar el modelo de reconocimiento facial con las fotos capturadas
    entrenar()
