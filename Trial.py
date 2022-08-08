# import RPi._GPIO as GPIO
# import gpiozero
# from Listen import Listen
# # # def relay_on():
# # #     GPIO.setwarnings(False)

# # #     GPIO.setmode(GPIO.BCM)

# # #     # GPIO.setup(17, GPIO.OUT)
# # #     GPIO.setup(17, GPIO.OUT)

# # #     # GPIO.output(17, 0)
# # #     GPIO.output(17, 0)


# # # def relay_off():
# # #     RELAY_PIN = 17
# # #     # RELAY_PIN1 = 17

# # #     relay = gpiozero.OutputDevice(RELAY_PIN,active_high=False,initial_value=False)
# # #     # relay = gpiozero.OutputDevice(RELAY_PIN1,active_high=False,initial_value=False)
# # #     relay.off()



# # # relay_off()
# # GPIO.setwarnings(False)

# # GPIO.setmode(GPIO.BCM)

# # GPIO.setup(22, GPIO.OUT)

# # GPIO.output(22, False)

# from datetime import date
# from plyer import notification
# import calendar

# def Calendar():
#     yy = date.today().day
#     mm = date.today().month
#     print(calendar.month(yy, mm))
#     return calendar.month(yy,mm)
# cal = Calendar()
# notification.notify(

#     title = "Jarvis",

#     message = cal,

#     app_icon = "/home/atharva/Downloads/Jarvis/index.ico",

#     timeout = 50

# )




# from PyQt5 import QtWidgets, QtCore, QtGui
# from Test1 import Ui_MainWindow
# from PyQt5.QtCore import  QTimer, QTime, QDate, Qt
# from PyQt5.QtGui import QMovie
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *
# from PyQt5.QtWidgets import *
# import sys



# class MainThread(QThread):
#     def __init__(self):
#         super(MainThread,self).__init__()



# class Main(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.ui = Ui_MainWindow()
#         self.ui.setupUi(self)
#         self.ui.pushButton.clicked.connect(self.Initiate)
#         self.ui.pushButton_2.clicked.connect(self.Deactivate)

#     def Initiate(self):
#         GPIO.setwarnings(False)
#         GPIO.setmode(GPIO.BCM)
#         GPIO.setup(18, GPIO.OUT)
#         GPIO.output(18, 0)

#     def Deactivate(self):
#         RELAY_PIN = 18
#         relay = gpiozero.OutputDevice(RELAY_PIN,active_high=False,initial_value=False)
#         relay.off()

    

# app = QApplication(sys.argv)
# jarvis = Main()
# jarvis.show()
# exit(app.exec_())   



# def Google():
#     sentence = Listen()
#     Yes = ['what','what is','why','why is','who','who is','how','how to','can you tell something about','can you tell me about','tell me something about','tell me about','what does','why does','who does','Google','google search','search','search about','search this','search that','what to do','how to to','what should i do','wheather','whats the whethaer','whats']

#     s = sentence.split(" ")
#     for i in range(len(s)):
#         if s[i] in Yes:
#             t = 1
#             print(t)
#             break
# Google()




# from difflib import get_close_matches
  
# def closeMatches(patterns, word):
#      print(get_close_matches(word, patterns))
  
# # Driver program
# if __name__ == "__main__":
#     word = 'appel'
#     patterns = ['ape', 'apple', 'peach', 'puppy']
#     closeMatches(patterns, word)


# from thefuzz import fuzz, process
# sentence = Listen()



# Yes = ['what is meant by','what is mean by','means','meant','who is','who is the','how to do','how to cook','can you tell something about','can you tell me about','tell me something about','tell me about','what does mean','why does mean','who does','Google','google search','search','search about','search this','search that','what to do if','what to do','how to make','what should i do','weather','whats the weather','meaning','meaning of']
# a = process.extract(sentence,Yes,limit = 1)
# a1 = a[0][1]
# print(a)
# if a1 >=90:
#     print("Got it")   
# else:
#     print("Noop")
import time
import os
os.system("xte 'keydown Alt_L' 'key Tab'")
for i in range(1):      
    time.sleep(1)
    os.system("xte 'key Tab'")
os.system("xte 'keyup Alt_L'")







#   print("You pressed enter")
# else:
#   print("You didnt")







# os.system("xte 'keydown Control_L' 'keydown Alt_L' 'key d' 'keyup Control_L' 'keyup Alt_L'")