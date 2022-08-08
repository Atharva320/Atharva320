import speech_recognition as sr
import time
from datetime import date
def Listen_passw():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening the password...//..//")
        audio = r.listen(source)

    try:
        print("Recognizing the password...//..//")
        query = r.recognize_google(audio)
       
    except:
        print("Unclear sound...")
    query = str(query)
    return query.lower()

