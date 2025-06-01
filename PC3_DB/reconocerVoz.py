import speech_recognition as sr
from gtts import gTTS
import playsound
import os

# Crear un reconocedor
r = sr.Recognizer()

# Usar el micrófono como fuente
with sr.Microphone() as source:
    print("Escuchando... di 'Hola [tu nombre]' para comenzar.")

    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)

    try:
        # Reconocer el texto con Google
        texto = r.recognize_google(audio, language="es-ES")
        print("Texto reconocido:", texto)

        # Comprobar si la frase contiene la palabra clave (por ejemplo, "Hola [tu nombre]")
        if "hola tu nombre" in texto.lower():  # Sustituye "tu nombre" por tu nombre real
            print("Voz reconocida, procesando...")
            
            # Convertir texto a voz con gTTS
            tts = gTTS(text="Comando reconocido", lang='es')
            archivo = "voz_generada.mp3"
            tts.save(archivo)

            # Reproducir el audio
            playsound.playsound(archivo)

            # Eliminar el archivo después
            os.remove(archivo)

        else:
            print("No reconocí el comando, intenta de nuevo.")
    
    except sr.UnknownValueError:
        print("No se entendió el audio.")
    except sr.RequestError:
        print("Error al conectar con el servicio de reconocimiento.")
