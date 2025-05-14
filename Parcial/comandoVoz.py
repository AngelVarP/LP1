import gtts
import os
import pygame
import time

# Funcion para hablar estructuras de texto
def voz(texto):
    # Generar un nombre base
    nombreBase = "mensaje.mp3"
    if os.path.exists(nombreBase):
        # Para no sobreescribir, agregamos sufijos
        contador = 1
        while os.path.exists(f"mensaje_{contador}.mp3"):
            contador += 1
        archivoAudio = f"mensaje_{contador}.mp3"
    else:
        archivoAudio = nombreBase
    
    # Crear y guardar el archivo de audio
    tts = gtts.gTTS(texto, lang='es')
    tts.save(archivoAudio)
    
    # Inicializar pygame para reproducir el archivo de audio
    pygame.mixer.init()
    pygame.mixer.music.load(archivoAudio)
    pygame.mixer.music.play()

    # Esperar mientras se reproduce el audio
    while pygame.mixer.music.get_busy():  
        time.sleep(1)  # Esperar un segundo


