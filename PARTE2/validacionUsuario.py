from comandoVoz import voz
import cv2
import os 
import imutils
import numpy as np

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

def agregarUsuario():
    usuarios = cargarUsuarios()
    print("Agregar nuevo usuario")

    # Se solicita nombre de usuario
    nuevoUsuario = input("Ingresa el nombre de usuario: ")

    if nuevoUsuario in usuarios:
        print("Este usuario ya existe")
        return
    
    nuevaClave = input("Ingresa la contraseña: ")

    persona = nuevoUsuario
    personaPath = f"./Fotos/{persona}"
    if not os.path.exists(personaPath):
        os.makedirs(personaPath)

    # Iniciar captura de rostro
    cap = cv2.VideoCapture(0)
    faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    print("Captura de rostro. Mantente bien posicionado.")

    count = 0
    while count < 30:
        ret, frame = cap.read()
        if not ret:
            break
        frame = imutils.resize(frame, width=840)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detectar rostro
        faces = faceClassif.detectMultiScale(gray, 1.3, 5)
        
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            rostro = frame[y:y + h, x:x + w]
            rostro = cv2.resize(rostro, (120, 120), interpolation=cv2.INTER_CUBIC)
            cv2.imwrite(f"{personaPath}/rostro_{count}.jpg", rostro)
            count += 1

        cv2.imshow("Captura de rostro", frame)
        if cv2.waitKey(1) == 27 or count >= 30:
            break

    cap.release()
    cv2.destroyAllWindows()

    # Guardar usuario y contraseña en el archivo usuarios.txt
    with open("usuarios.txt", "a") as file:
        file.write(f"{nuevoUsuario},{nuevaClave}\n")
    print(f"Usuario {nuevoUsuario} agregado con éxito.")


def entrenar():
    print("Entrenando el modelo de rostros...")

    # Ruta de las fotos de los usuarios
    dataPath = './Fotos'  # Asegúrate de que esta ruta sea correcta
    peopleList = os.listdir(dataPath)  # Lista de personas en la carpeta Fotos

    labels = []
    facesData = []
    label = 0

    for nameDir in peopleList:
        personPath = dataPath + '/' + nameDir
        print(f'Leyendo las imágenes de {nameDir}')

        for fileName in os.listdir(personPath):
            print(f'Rostro: {nameDir}/{fileName}')
            labels.append(label)
            facesData.append(cv2.imread(personPath + '/' + fileName, 0))  # Leer en escala de grises
            image = cv2.imread(personPath + '/' + fileName, 0)
            cv2.imshow('image', image)
            cv2.waitKey(50)
        label += 1

    # Entrenar el reconocedor de rostros
    print("Entrenando...")
    face_recognizer = cv2.face.LBPHFaceRecognizer_create()  # Usamos LBPH
    face_recognizer.train(facesData, np.array(labels))

    # Guardar el modelo entrenado
    model_dir= '-/Modelos'
    if not os.path.exists(model_dir):
        os.makedirs(model_dir)

    face_recognizer.write(os.path.join(model_dir,'modeloLBHFace.xml'))  # Guarda el modelo en la carpeta Modelos
    print("Modelo entrenado y guardado como modeloLBPHFace.xml")


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

            # Validación de rostro
            if not validarRostro(usuario):
                print("No se ha podido verificar el rostro.")
                voz("No se ha podido verificar el rostro.")
                return False
            
            return True
        else:
            print(f"Usuario o contraseña incorrectos. Intentos restantes: {2 - intentos}")
            voz(f"Usuario o contraseña incorrectos. Intentos restantes: {2 - intentos}")
            intentos += 1
    print("Demasiados intentos fallidos. El programa finalizará.")
    voz("Demasiados intentos fallidos. El programa finalizará.")
    return False

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

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = faceClassif.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            rostro = gray[y:y + h, x:x + w]
            rostro = cv2.resize(rostro, (150, 150), interpolation=cv2.INTER_CUBIC)
            result = recognizer.predict(rostro)

            if result[1] < 70:  # Umbral de confianza
                print(f"Rostro verificado con éxito: {result}")
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

        cv2.imshow('frame', frame)
        if cv2.waitKey(1) == 27:  # Esc para salir
            break

    cap.release()
    cv2.destroyAllWindows()
    return False


# Llamar a agregar un usuario de prueba
agregarUsuario()

# Ahora que tienes al menos un usuario con fotos, puedes entrenar el modelo
entrenar()
