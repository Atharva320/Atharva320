import speech_recognition as sr
import time
from datetime import date
def Listen_City():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening the city name...")
        audio = r.listen(source)

    try:
        print("Recognizing the city name..")
        query = r.recognize_google(audio)
       
    except:
        print("Unclear sound...")
    query = str(query)
    return query.lower()

