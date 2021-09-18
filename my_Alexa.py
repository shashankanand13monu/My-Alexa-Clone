#--------------------------------------------------------------------------------------------------------#
import pyttsx3 #Text->Speech
import datetime
import speech_recognition as sr
import wikipedia 
import webbrowser
import os
import smtplib
from wikipedia import exceptions
import pywhatkit as kt #For searching
#------------------------------------------------------------------------------------------------------------###

engine= pyttsx3.init('sapi5') # init function to get & load an engine instance for the speech synthesis 
voices = engine.getProperty('voices') # voice is provided by ms-sapi5 
# print(voices[0].id) #1 : Zira voice , 0: David
engine.setProperty('voice',voices[1].id) #Changing Value | 'rate',300

#-------------------------------------------------------------------------------------------------------------#

def speak(audio): #Audio-> Argument to get speech
    print(audio)
    engine.say(audio) # say method on the engine that passing input text to be spoken
    engine.runAndWait() # queued commands, it processes the voice commands.

#-------------------------------------------------------------------------------------------------#

def wishMe():
    hour= int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour <18:
        speak("Good Evening")
    else:
        speak("Good Night")

    print(do_list)
    speak("Hi, I am Alexa  and here's a List of things you can do with me Try Saying Something")
    
chrome_path="C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" #CHANGE ACC. TO NEED
webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path),preferred=True)
wb= webbrowser.get('chrome')
# wb.open_new_tab("google.com")
open_code= "C:\\Users\\KIIT\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
music_dir = r"C:\Users\KIIT\Desktop\Apps\Project\My Alexa Assistant\Music" #r-> Spaces in b/w or use C:\\xx\\xx
songs = os.listdir(music_dir)

do_list= '''
Play Music
Open Youtube 
Send Email
what is the time
Search on web
Alexa Quit '''
#---------------------------------------------------------------------------------# 
   
def takeCommand(): # mICROPHONE iNPUT->sTRING oUTPUT
    
    r= sr.Recognizer()
    with sr.Microphone() as source:
        speak("Listening...")
        r.pause_threshold=1 #Gap between speaking
        audio= r.listen(source)  
    try:
        speak("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"You Said : {query}\n")
    
    except Exception as e:
        print(e)

        speak("Say that Again Please...")
        return "NONE"
    return query    
#-------------------------------------------------------------------------------#        

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587) #Must enable/allow less secure apps in gmail
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com','your-passward')
    server.sendmail('sample@gmail.com',to,content)
    server.close()
#---------------------------------------------------------------------------------#

if __name__ == '__main__':
    speak("i am made by Shashank")
    wishMe()

    # c= webbrowser.get('firefox')
    while True:
    # if 1:
        query = takeCommand().lower() #string->lowercase

        #Logic For Exceuting Tasks based on query
        if 'wikipedia' in query:
           speak("Searching Wikipedia...")
           query= query.replace("wikipedia","")
           results= wikipedia.summary(query,sentences=1)
           speak("According to Wikipedia ")
        #    print(results)
           speak(results) 
        elif 'open youtube' in query:
             webbrowser.open_new_tab("youtube.com")   # Or wb.open("URL")
            # webbrowser.open("youtube.com")
        elif 'play music' in query:
            print(songs)
            speak("Playing Music...")
            os.startfile(os.path.join(music_dir,songs[0])) # To join song and its dir. path | Tip: Or use random to play random song
        elif 'the time' in query:
            stringtime= datetime.datetime.now().strftime("%H:%M:%S")
            # print(f"The Time is {stringtime}")
            speak(f"The Time is {stringtime}")
        elif 'open code' in query:
            os.startfile(open_code)
        elif 'send email to aman' in query:
            try:
                # print("what should i say?")
                speak("What Should i say?")
                content= takeCommand()
                to = "sample@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent")
            except Exception as e:
              print(e)
              speak("Sorry, Mail can't be sent, Please check again later ")
                
        elif 'quit' in query:
            speak("goodbye , have a nice day and thanks for using me")
            exit()
        elif 'search' in query:
            speak("I Have found this on Google")
            kt.search(query)
            exit()
            
            