#Libraries for making this application
import pyttsx3     # to convert text to speeches
import datetime    # to get current current time
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine=pyttsx3.init('sapi5') #init()  gives the reference to engine instanse and sapi5 is used for windows
voices=engine.getProperty('voices')   #getting voices available in the library
engine.setProperty('voice',voices[1].id)  # initialise the voice with a perticular available available

# Functions
def speak(audio):   #Speaks the particular string passed as an argument
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")

    speak("I am your personal voice assistant Please tell me how may I help you")

def listen():
    r=sr.Recognizer()
    my_mic=sr.Microphone(device_index=1)
    with my_mic as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing....")
        query=r.recognize_google(audio)
        print(f"User said-{query}")
    except Exception as e:
        print(e)
        print("Say that again Please !!")
        return "None"
    return query

# def sendEmail(to,content):

#Main function is as follows
if __name__ == '__main__':
    # print(sr.__version__)
    wishMe()
    #speak("Harry is a good boy")
    while True:
        queries=listen().lower()
        if 'wikipedia' in queries:
            speak("Searching in wikipedia")
            queries=queries.replace("wikipedia","")
            results=wikipedia.summary(queries,sentences=2)
            speak("According to wikipedia ")
            print(results)
            speak(results)
        elif 'search for' in queries:
            speak("Searching sir")
            queries=queries.replace("wikipedia","")
            results=wikipedia.summary(queries,sentences=2)
            print(results)
            speak(results)
        elif 'open youtube' in queries:
            webbrowser.open('youtube.com')

        elif 'open google' in queries:
            webbrowser.open('google.com')
        elif 'open stackoverflow' in queries:
            webbrowser.open('stackoverflow.com')
        elif 'open geeksforgeeks' in queries:
            webbrowser.open('geeksforgeeks.com')
        elif 'the time' in queries:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the time is {strTime}")

        elif 'open code' in queries:
            codePath="C:\\Users\\SHOBHIT BANSAL\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        # elif 'email to shobhit' in queries:
        #     try:
        #         speak("What should I say?")
        #         content=takeCommand()
        #         to="imshobhit.sb@gmail.com"
        #         sendEmail(to,content)
        #         speak("Email has been sent!")
        #     except Exception as e:
        #         print(e)
        #         speak("Sorry,unable to send this email ")

