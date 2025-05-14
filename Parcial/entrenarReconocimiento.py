import numpy as np
import json
import os
import cv2
from validacionUsuario import obtenerRutaFotos
from comandoVoz import voz

# Funcion para entrenar el reconocimiento facial
def entrenar():
    # Inicio de entrenamiento
    print("Entrenando el modelo de rostros...")
    voz("Entrenando el modelo de rostros...")

    # Ruta de las fotos de los usuarios
    dataPath = obtenerRutaFotos()
    peopleList = os.listdir(dataPath)  # Lista de personas en la carpeta Fotos

    labels = []
    facesData = []
    label = 0  # Etiqueta inicial para el primer usuario
    usuario_to_label = {}  # Diccionario para mapear el nombre de usuario

    # Iterar sobre cada usuario en la lista
    for nameDir in peopleList:
        personPath = os.path.join(dataPath, nameDir)

        print(f'Leyendo las imágenes de {nameDir}')
        for fileName in os.listdir(personPath):
            print(f'Rostro: {nameDir}/{fileName}')
            labels.append(label)
            facesData.append(cv2.imread(personPath + '/' + fileName, 0))  # Leer en escala de grises
            image = cv2.imread(personPath + '/' + fileName, 0)
            cv2.imshow('image', image)
            cv2.waitKey(50)

        usuario_to_label[nameDir] = label
        label += 1

    # Entrenar el reconocedor de rostros
    print("Entrenando...")
    voz("Entrenando...")
    face_recognizer = cv2.face.LBPHFaceRecognizer_create()  # Usamos LBPH
    face_recognizer.train(facesData, np.array(labels))

    # Guardar el modelo entrenado en 'Modelos'
    model_dir= './Modelos'
    if not os.path.exists(model_dir):
        os.makedirs(model_dir)

    face_recognizer.write(os.path.join(model_dir,'modeloLBPHFace.xml'))  # Guarda el modelo en la carpeta Modelos
    print("Modelo entrenado y guardado como modeloLBPHFace.xml")

    # Guardar el mapeo de usuarios en labels
    with open('./Modelos/usuarios_labels.json', 'w') as f:
        json.dump(usuario_to_label, f)
    print("Mapa de usuarios a labels guardado como usuarios_labels.json")

