import pyttsx3
import speech_recognition as sr

r = sr.Recognizer()

def speak_text(cmd):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    for voice in voices:
        if "german" in voice.languages:
            engine.setProperty('voice', voice.id)
            break
    engine.setProperty("rate", 115)
    engine.say(cmd)
    engine.runAndWait()

def listen_text():

    print("Say something amazing >>>")

    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=0.2)
            audio = r.listen(source)
            text = r.recognize_google(audio, language="de-DE")
            text = text.lower()

            return text

    except sr.UnknownValueError:
        speak_text("Ein Fehler ist aufgetreten. Bitte Versuchen Sie das erneut.")
        text = listen_text()
        return text

    except sr.RequestError:
        speak_text("Ein Fehler ist aufgetreten. Bitte Versuchen Sie das erneut.")
        text = listen_text()
        return text
