import pyttsx3
import speech_recognition as sr

engine=pyttsx3.init()
sound=engine.getProperty("voices")
engine.setProperty("voice", sound[1].id)
r=sr.Recognizer()

while True:
    try:
        with sr.Microphone() as source:
            cmdaudio = r.listen(source)
            cmdtext=r.recognize_google(cmdaudio)
            cmdvoc=format(cmdtext)
            if "sleep" in cmdvoc:
                break
            else:
                engine.say(cmdvoc)
                engine.runAndWait()
    except:
        continue

