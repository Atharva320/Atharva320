from logging import exception
# from xml.etree.ElementTree import TreeBuilder
import speech_recognition as sr
import time
from datetime import date
import gpiozero
import RPi._GPIO as GPIO
def Listen():


    r = sr.Recognizer()

    with sr.Microphone() as source:
        GPIO.setwarnings(False)

        GPIO.setmode(GPIO.BCM)

        GPIO.setup(22, GPIO.OUT)

        GPIO.output(22, True)
        print("Listening....")
        audio = r.listen(source)

    try:
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(22, GPIO.OUT)
        GPIO.output(22, False)
        print("Recognizing....")
        query = r.recognize_google(audio, language = 'en-IN')
        print(f"You Said : {query}")
        if "None" in query:
            pass
        current_date=date.today()
        t = time.strftime("%I:%M %p")
        file=open('/home/atharva/Downloads/Jarvis/DataBase/history.txt','a')
        file.write(f'{current_date} {t} {query}\n')
        file.close()
    except:
        print("Try again")
        with sr.Microphone() as source:
            GPIO.setwarnings(False)
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(22, GPIO.OUT)
            GPIO.output(22, True)
            print("Listening....")
            audio = r.listen(source)
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(22, GPIO.OUT)
        GPIO.output(22, False)
        print("Recognizing....")
        query = r.recognize_google(audio, language = 'en-IN')
        print(f"You Said : {query}")
        if "None" in query:
            pass
        current_date=date.today()
        t = time.strftime("%I:%M %p")
        file=open('/home/atharva/Downloads/Jarvis/DataBase/history.txt','a')
        file.write(f'{current_date} {t} Unable to recognize..\n')
        file.close()
    query = str(query)
    return query.lower()