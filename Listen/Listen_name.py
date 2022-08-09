import speech_recognition as sr
import time
from datetime import date
def Listen_name():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening your name...//..//")
        audio = r.listen(source)

    try:
        print("Recognizing the name...//..//")
        query = r.recognize_google(audio)
        print(f"You Said : {query}")
       
    except:
        print("Unclear sound...")
    query = str(query)
    return query

