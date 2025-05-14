import cv2
import os 
import numpy as np
import json
from comandoVoz import voz

# Funcion para cargar usuarios desde 'usuarios.txt'
def cargarUsuarios():
    # Diccionario para almacenar los usuarios y contraseñas
    usuarios = {}
    try:
        with open("usuarios.txt", "r") as file:
            for line in file:
                # Dividir cada linea en usuario y contraseña
                usuario, contrasena = line.strip().split(",")
                usuarios[usuario] = contrasena
    except FileNotFoundError:
        voz("El archivo usuarios.txt no se encuentra.")
        print("El archivo usuarios.txt no se encuentra.")
    return usuarios

# Funcion para obtener la ruta de la carpeta Fotos
def obtenerRutaFotos():
    return os.path.abspath('./Fotos')

# Funcion para validar el rostro del usuario
def validarRostro(usuario):
    # Inicialización de la cámara
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("No se pudo abrir la cámara.")
        return False

    # Cargar el clasificador de rostros
    faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('./Modelos/modeloLBPHFace.xml')

    # Mostrar video para que el usuario se posicione en la camara
    print("Por favor, posicione su rostro en cámara...")
    star_time = cv2.getTickCount()
    display_duration = 5

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Mostrar video
        elapsed_time = (cv2.getTickCount() - star_time) / cv2.getTickFrequency()
        if elapsed_time < display_duration: 
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) == 27:
                break
            continue

        # Validacion del rostro
        faces = faceClassif.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            rostro = gray[y:y + h, x:x + w]
            rostro = cv2.resize(rostro, (150, 150), interpolation=cv2.INTER_CUBIC)
            result = recognizer.predict(rostro)

            label, confidence = result

            # Comparar si las fotos coinciden con el usuario 
            if label == getUsuarioID(usuario) and confidence < 70:  # Umbral de confianza
                print(f"Rostro verificado con éxito: {usuario}")
                voz(f"Rostro verificado con éxito.")
                cap.release()
                cv2.destroyAllWindows()
                return True
            else:
                print("Rostro no reconocido.")
                voz("Rostro no reconocido.")
                cap.release()
                cv2.destroyAllWindows()
                return False

        if cv2.waitKey(1) == 27:  # Esc para salir
            break

    cap.release()
    cv2.destroyAllWindows()
    return False


# Funcion para obtener el ID asociado al usuario
def getUsuarioID(usuario):
    try:
        with open('./Modelos/usuarios_labels.json', 'r') as f:
            usuarios = json.load(f)
        
        return usuarios.get(usuario,-1)
    except FileNotFoundError:
        print("Archivo de usuarios no encontrado.")
        return -1
    except json.JSONDecodeError:
        print("Error al leer archivo JSON.")
        return -1
    
