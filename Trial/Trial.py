from logging import exception
import speech_recognition as sr
# def Listen():


    
#     query = str(query)
#     return query.lower()
    
while True:
    
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening....")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query= r.recognize_google(audio)
        if query is not None:
            print(f"You Said : {query}")
    except:
        print("Try again")
