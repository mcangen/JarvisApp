import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()
engine.setProperty('rate', 180)
engine.setProperty('voice', engine.getProperty('voices')[0].id)

def hablar(texto):
    print(f"Jarvis 🗣️: {texto}")
    engine.say(texto)
    engine.runAndWait()

def escuchar():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎧 Escuchando...")
        audio = r.listen(source)
    try:
        texto = r.recognize_google(audio, language="es-CO")
        print(f"🗣️ Usuario: {texto}")
        return texto
    except sr.UnknownValueError:
        print("❌ No se entendió el audio.")
        return None
