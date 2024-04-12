import pyttsx3
import speech_recognition as sr

r = sr.Recognizer()

def speak_text(cmd):
    engine = pyttsx3.init()
    engine.setProperty('voice', 'german')
    engine.setProperty('rate', 115)
    engine.say(cmd)
    engine.runAndWait()

def listen_text():

    print("Say something: ")

    with sr.Microphone() as source:

        r.adjust_for_ambient_noise(source, duration=0.2)

        audio = r.listen(source)

        text = r.recognize_google(audio, language="de")
        text = text.lower()

        return text

def main():




    speak_text("Die Auswahlmöglichkeiten sind Platz 4A, 5B und 16C")

if __name__ == "__main__":
    main()
