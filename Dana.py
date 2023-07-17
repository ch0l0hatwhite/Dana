from playsound import playsound
import speech_recognition as sr
import pywhatkit as py
from gtts import gTTS
import time as cholo
import os 


if not all([os.path.exists(file) for file in ["h.mp3", "s.mp3", "n.mp3"]]):
    tts = gTTS(
        "le doy la bienvenida! soy Dana, su asistente!, creada por cholohatwhite, dígame, ¿en qué le puedo servir?",
        lang="es",
    )
    tts.save("h.mp3")

    tts = gTTS("A sus órdenes, su búsqueda está en camino!", lang="es")
    tts.save("s.mp3")

    tts = gTTS("lo siento, ¿puede repetir por favor?", lang="es")
    tts.save("n.mp3")

print("""
======================================================================                                 
 ██████████                                          
░░███░░░░███
 ░███   ░░███  ██████   ████████    ██████           
 ░███    ░███ ░░░░░███ ░░███░░███  ░░░░░███          
 ░███    ░███  ███████  ░███ ░███   ███████          
 ░███    ███  ███░░███  ░███ ░███  ███░░███          
 ██████████  ░░████████ ████ █████░░████████ ██ ██ ██
░░░░░░░░░░    ░░░░░░░░ ░░░░ ░░░░░  ░░░░░░░░ ░░ ░░ ░░ 
======================================================================                                 
"""
)

print(" creada por cholohatwhite   github: https://github.com/ch0l0hatwhite \n\n")

print("Asistente virtual. No ocupa inteligencia artificial\n\n")

playsound("h.mp3")


def dana():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Microfono encendido! \n")
        print("Puedes Hablar Ahora : \n\n")
        print("\n\n")
        audio = r.listen(source)
        cholo.sleep(2)
        try:
            text = r.recognize_google(audio)
            print("\n\nTu dijiste : {}".format(text))
            playsound("s.mp3")
            py.search(text)

        except:
            playsound("n.mp3")
            dana()


r = sr.Recognizer()

with sr.Microphone() as source:
    print("Microfono encendido!\n")
    print("Puedes Hablar Ahora : \n")
    audio = r.listen(source)
    cholo.sleep(2)
    try:
        text = r.recognize_google(audio)
        print("Tu dijiste : {}".format(text))
        playsound("s.mp3")
        py.search(text)

    except:
        playsound("n.mp3")
        dana()
