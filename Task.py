import datetime
import calendar
from datetime import date
from getpass import getpass
import time
import os
import gpiozero
import RPi._GPIO as GPIO
from Study import Study
from Study import Yestarday
from Study import Remember
from prettytable import PrettyTable
import webbrowser
from Listen import Listen
from Listen_passw import Listen_passw
from Listen_name import Listen_name
from Notification import Jarvis_Time
from Notification import Jarvis_Date
from Notification import Jarvis_Right_Password
from Notification import Jarvis_Wrong_Password
from Notification import *
import wikipedia as googlescrap
import pywhatkit

def Time():
    t = time.strftime("%I:%M %p")
    print(t)
    Jarvis_Time(t)


def Date():
    date = datetime.date.today()
    print(date)
    Jarvis_Date(date)

def Calendar():
    yy = date.today().day
    mm = date.today().month
    print(calendar.month(yy, mm))

def Year():
    year = date.today().year
    print(year)

def Month():
    month = date.today().month
    print(month)

def Day():
    day = date.today().day
    print(day)

def Screenshot():
    import os
    os.system("gnome-screenshot")

def Notauth(name):
    file1=open('/home/atharva/Downloads/Jarvis/current_user.txt','w')
    file1.write(name)
    file1.close()

def Entry(name):
    file2=open('/home/atharva/Downloads/Jarvis/All_users.txt','a')
    current_date=date.today()
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    file2.write(f"\n User named {name} was logged in Jarvis on {current_date} at {current_time} \n")
    file2.close()

def Start():
    passw = Listen_passw()
    password = "time 6514"
    if passw == password:
        Jarvis_Right_Password()
        print("Welcome Sir \n \n")
        file=open('/home/atharva/Downloads/Jarvis/Users.txt','w')
        file.write('1')
        file.close()

    elif passw!=password:
        Jarvis_Wrong_Password()
        print("Try again...")
        passw1 = Listen_passw()
        if passw1!=password:
            print("Say your name")
            name1 = Listen_name()
            Notauth(name1)
            Entry(name1)
            file=open('/home/atharva/Downloads/Jarvis/Users.txt','w')
            file.write('2')
            file.close()
            exit()
        
        elif passw1==password:
            Jarvis_Right_Password()
            file=open('/home/atharva/Downloads/Jarvis/Users.txt','w')
            file.write('1')
            file.close()
            print("Welcome Sir...")


def Who():
    file=open('/home/atharva/Downloads/Jarvis/Users.txt','r')
    T = file.read(1)
    
    if T == '1' :
        print("Your name is Atharva Raut...sir")

    elif T == '2':
        print("You are not the authenticated user...")


def Hsitory():
    file=open('/home/atharva/Downloads/Jarvis/history.txt','r')
    L = file.readlines()
    b = []
    for line in L:
        length = len(line)
        command = line[20:length]
        date = line[0:10]
        time = line[11:16]
        A_p = line[17:19]
        a = [command,date,time,A_p]
        b.append(a)
    t = PrettyTable(['Date', 'Time', 'AM/PM', 'Command'])
    for i in range(len(b)):
        t.add_row([b[i][1], b[i][2], b[i][3], b[i][0]])
    print(t)


def relay_on():
    GPIO.setwarnings(False)

    GPIO.setmode(GPIO.BCM)

    GPIO.setup(17, GPIO.OUT)

    GPIO.output(17, 0)

    Jarvis_Light_On()

def relay_off():
    RELAY_PIN = 17

    relay = gpiozero.OutputDevice(RELAY_PIN,active_high=False,initial_value=False)

    relay.off()

    Jarvis_Light_Off

    
def Clear():
    os.system('clear')


def Google():
    webbrowser.open_new_tab("http://www.google.com")


def Search(query):
    query.replace("hey","")
    query.replace("can you","")
    query.replace("please","")
    query.replace("hi","")
    query.replace("buddy","")
    query.replace("jarvis","")
    query.replace("Jarvis","")
    print("This is what I found on web")
    pywhatkit.search(query)


def Files():
    os.system("xdg-open /home/atharva")


def System_On():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18, GPIO.OUT)
    GPIO.output(18, 0)

    Jarvis_System_Initiated()

def System_Off():
    RELAY_PIN = 18
    relay = gpiozero.OutputDevice(RELAY_PIN,active_high=False,initial_value=False)
    relay.off()

    Jarvis_System_Deactivated()

def Arc_blue_on():
    GPIO.setwarnings(False)

    GPIO.setmode(GPIO.BCM)

    GPIO.setup(22, GPIO.OUT)

    GPIO.output(22, False)

    GPIO.setwarnings(False)

    GPIO.setmode(GPIO.BCM)

    GPIO.setup(22, GPIO.OUT)

    GPIO.output(22, True)


def Arc_blue_off():
    GPIO.setwarnings(False)

    GPIO.setmode(GPIO.BCM)

    GPIO.setup(22, GPIO.OUT)

    GPIO.output(22, False)

def Arc_red_on():
    Arc_blue_off()
    GPIO.setwarnings(False)

    GPIO.setmode(GPIO.BCM)

    GPIO.setup(27, GPIO.OUT)

    GPIO.output(27, True)

def Arc_red_off():
    GPIO.setwarnings(False)

    GPIO.setmode(GPIO.BCM)

    GPIO.setup(27, GPIO.OUT)

    GPIO.output(27, False)


def Controls_GUI():
    os.system("python /home/atharva/Downloads/Jarvis/Control.py")



def Minimize_Window():
    os.system("xte 'keydown Control_L' 'keydown Alt_L' 'key d' 'keyup Control_L' 'keyup Alt_L'")

def Switch_Tab():
    import time
    import os
    os.system("xte 'keydown Alt_L' 'key Tab'")
    for i in range(1):      
        time.sleep(1)
        os.system("xte 'key Tab'")
    os.system("xte 'keyup Alt_L'")




def Maximize_Window():
    os.system("xte 'keydown Control_L' 'keydown Alt_L' 'key d' 'keyup Control_L' 'keyup Alt_L'")



def NonInputExecution(query):

    query = str(query)

    if "time" in query:
        Time()

    elif "date" in query:
        Date()

    elif "calendar" in query:
        Calendar()

    elif "screenshot" in query:
        Screenshot()

    elif "who" in query:
        Who()

    elif "history" in query:
        Hsitory()

    elif "study" in query:
        Study()
        
    elif "light on" in query:
        relay_on()

    elif "light off" in query:
        relay_off()

    elif "clear" in query:
        Clear()

    elif "study"in query:
        Study()

    elif "yestarday"in query:
        Yestarday()

    elif "remember"in query:
        Remember()

    elif "Google" in query:
        Google()

    elif "search" in query:
        Search()

    elif "files" in query:
        Files()

    elif "System_On" in query:
        System_On()
    
    elif "System_Off" in query:
        System_Off()

    elif "Controls_GUI" in query:
        Controls_GUI() 

    elif "Minimize_Window"in query:
        Minimize_Window()

    elif "Switch_Tab" in query:
        Switch_Tab() 
    
    elif "Maximize_Window"in query:
        Maximize_Window()

    


