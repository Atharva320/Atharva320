import speech_recognition as sr
import os

while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening ._._._._._")
        r.pause_threshold = 1
        audio = r.listen(source,0,2)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio)
        print(f"You Said : {query}")
        if "wake up" in query or "jarvis wake up" in query or "hey jarvis" in query or "jarvis" in query:
            os.system('gnome-terminal -x sh -c "Jarvis 2>/dev/null"; bash')
        
    except:
        print(".......")


