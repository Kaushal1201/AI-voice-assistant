import pyttsx3
import speech_recognition as sr
import random
import webbrowser
import datetime
import pyautogui
import wikipedia
import pywhatkit as pwk

engine = pyttsx3.init()
voices = engine.getProperty('voices')       #getting details of current voice
engine.setProperty('voice', voices[0].id)
engine.setProperty("rate",170) 

def speak(audio):
    engine.say(audio)
    engine.runAndWait()



def command():
    content=" "
    while content==" ":    
        # obtain audio from the microphone
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)

        # recognize speech using Google Speech Recognition
        try:
            content=r.recognize_google(audio)
            print("You said = " + content)
        except Exception as e:
            print("Please Try again...")
        
    return content
       
def main_process():
           
    while True:
        request=command().lower()
        if("hello" in request):
            speak("Welcome,How can i help you.")
        elif("play music" in request):
            speak("playing music")
            song=random.randint(1,3)
            if(song==1):
                webbrowser.open("https://www.youtube.com/watch?v=9HkE0KkTdI8")
            elif(song==2):
                webbrowser.open("https://www.youtube.com/watch?v=qqAYW7uxErI")
            elif(song==3):
                webbrowser.open("https://www.youtube.com/watch?v=AsqueHLf_yg")
        elif("say time" in request):
            now_time=datetime.datetime.now().strftime("%H:%M")
            speak("Current time is "+str(now_time))
            
        elif("say date" in request):
            now_date=datetime.datetime.now().strftime("%d;%m")
        
        elif("open youtube" in request):
            webbrowser.open("www.youtube.com")
            
        
        elif("open" in request):
            query=request.replace("open","")
            pyautogui.press("super")
            pyautogui.typewrite(query)
            pyautogui.sleep(2)
            pyautogui.press("enter")
            
        elif("wikipedia" in request):
            query=request.replace("search wikipedia ","")
            result=wikipedia.summary(query,sentences=2)
            print(result)
            speak(result)
        
        elif("search google" in request):
            query=request.replace("search google ","")
            webbrowser.open("https://www.google.com/search?q="+query)
        
        elif("send whatsapp" in request):
            pwk.sendwhatmsg("+910123456789", "Hi", 13, 30)
        
            
main_process()