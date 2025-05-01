import speech_recognition as sr

# Inicializar el reconocedor de voz
recognizer = sr.Recognizer()

# Usar el micrófono como fuente de entrada
with sr.Microphone() as source:
    print("Di algo:")
    audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        print(f"Reconocido: {text}")
    except sr.UnknownValueError:
        print("No se entendió lo que dijiste")
    except sr.RequestError as e:
        print(f"Error en la solicitud; {e}")


