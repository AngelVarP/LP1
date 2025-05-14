from gtts import gTTS
import os

text = "Puro industrial wbn luego por que no pasan"
tts = gTTS(text=text, lang='es')
tts.save("voz.mp3")
os.system("start voz.mp3")  # En Windows, para reproducir el archivo de audio
