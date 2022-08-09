from plyer import notification


def Jarvis_online():
    notification.notify(

        title = "Jarvis",

        message = "Jarvis is now online",

        app_icon = "/home/atharva/Downloads/Jarvis/index.ico",

        timeout = 2

    )


def Jarvis_offline():

    notification.notify(

        title = "Jarvis",

        message = "Jarvis is now offline\n\nIf you need me just say 'wake-up Jarvis'",

        app_icon = "/home/atharva/Downloads/Jarvis/index.ico",

        timeout = 2

    )


def Jarvis_Time(time):


    notification.notify(

        title = "Jarvis",

        message = f"Time : {time}",

        app_icon = "/home/atharva/Downloads/Jarvis/index.ico",

        timeout = 2

    )


def Jarvis_Date(date):

    notification.notify(

        title = "Jarvis",

        message = f"Today's Date : {date}",

        app_icon = "/home/atharva/Downloads/Jarvis/index.ico",

        timeout = 2

    )



def Jarvis_Right_Password():


        notification.notify(

        title = "Jarvis",

        message = "Login was succesfull...",

        app_icon = "/home/atharva/Downloads/Jarvis/index.ico",

        timeout = 2

    )




def Jarvis_Wrong_Password():

     notification.notify(

        title = "Jarvis",

        message = "Incorrect Password..Try again",

        app_icon = "/home/atharva/Downloads/Jarvis/index.ico",

        timeout = 2

    )


def Jarvis_System_Initiated():

     notification.notify(

        title = "Jarvis",

        message = "System is Initiated",

        app_icon = "/home/atharva/Downloads/Jarvis/index.ico",

        timeout = 2

    )

def Jarvis_System_Deactivated():

     notification.notify(

        title = "Jarvis",

        message = "System is Deactivated",

        app_icon = "/home/atharva/Downloads/Jarvis/index.ico",

        timeout = 2

    )

def Jarvis_Light_On():

     notification.notify(

        title = "Jarvis",

        message = "Light is turned On",

        app_icon = "/home/atharva/Downloads/Jarvis/index.ico",

        timeout = 2

    )

def Jarvis_Light_Off():

     notification.notify(

        title = "Jarvis",

        message = "Light is turned Off",

        app_icon = "/home/atharva/Downloads/Jarvis/index.ico",

        timeout = 2

    )

def Item_From_TodoList_Added_In_Done_File(Item):

     notification.notify(

        title = "Jarvis",

        message = f"{Item} -->\nTask Done ✔",

        app_icon = "/home/atharva/Downloads/Jarvis/index.ico",

        timeout = 2

    )