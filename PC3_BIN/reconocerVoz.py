import speech_recognition as sr

def reconocer_voz():
    # Crear el reconocedor
    r = sr.Recognizer()

    # Usar el micrófono como fuente
    with sr.Microphone() as source:
        print("Ajustando ruido ambiental, espera...")
        r.adjust_for_ambient_noise(source, duration=1)
        print("Habla ahora:")
        audio = r.listen(source)

    try:
        # Usar Google Speech Recognition para convertir a texto
        texto = r.recognize_google(audio, language="es-ES")
        print("Texto reconocido:", texto)
        return texto
    except sr.UnknownValueError:
        print("No se pudo entender el audio.")
    except sr.RequestError:
        print("Error con el servicio de reconocimiento.")

if __name__ == "__main__":
    reconocer_voz()
