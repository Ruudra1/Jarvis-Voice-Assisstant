import pyttsx3
import datetime
import speech_recognition as sr 
import wikipedia
import webbrowser
import os
import smtplib
import requests
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
newVoiceRate = 5
def speak(audio):
    engine.say(audio)
    engine.runAndWait() 
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Boss!")
    elif hour>=12 and hour<18:
        speak("Good afternoon Boss!")
    else:
        speak("Good Evening Boss!")
    speak("Jarvis at your command sir!")
voiceEngine = pyttsx3.init()
rate = voiceEngine.getProperty('rate')
volume = voiceEngine.getProperty('volume')
voice = voiceEngine.getProperty('voice')
 
#print(rate)
#print(volume)
#print (voice)
def takeCommand():
    #it takes microphone input from the user and return string output. 
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Go on sir, I am all ears...")
        r.pause_threshold = 1.2
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")
    
    except Exception as e:
        #print(e)
        print("Say that again please.....")
        return "None"
    return query
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.echlo()
    server.starttls()
    server.login('youremail@gmail.com','your-password-here') #put your email id and password
    server.sendmail('youremail@gmail.com', to, content)
    server.close()
if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        #logic for executing task based query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("Wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            print(results)
            speak("According to Wikipedia")
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open my mail' in query:
            webbrowser.open("gmail.com")
        elif 'open classroom' in query:
            webbrowser.open("classroom.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'play music' in query:
            music_dir = 'D:\\Songs'
            songs = os.listdir(music_dir)
            #print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'the time inquiry' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, The time is {strTime}")
        elif 'you up' in query:
            speak("For you sir, always")
        elif 'open code' in query:
            codePath = "C:\\Users\\Naitik Shah\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'Email to Harshil' in query:
            try:
                speak("Sure boss, What should I say")
                content = takeCommand() #Take command converts the command to string
                to = "yourEmail@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir, I am not being able to send this email!")
        elif 'Jarvis quit' in query:
            exit

