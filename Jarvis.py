# Jarvis AI Desktop Voice Assistant

import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import requests
import json
# for pyaudio: pip install pywin and pywin install pyaudio

engine=pyttsx3.init('sapi5') # microsoft speech api 
voices=engine.getProperty('voices') # getting vocies from pc
engine.setProperty('voice',voices[0].id) # voices[0] is male and voice[1] is female

def speak(audio):
    # it speaks the provided audio from pc

    engine.say(audio) # access to speak audio
    engine.runAndWait() # wait to speak the audio

def wishMe(): 
    # says good morning,afternoon,evening based on real time hour value

    hour = int(datetime.datetime.now().hour) # get hour value between 1 and 24
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Jarvis Sir. Please tell me how may I help you") 

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source,phrase_time_limit=3) # getting user voice within 3 seconds

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') # using google recognizer to recognize it
        print(f"User said: {query}\n")

    except Exception as e:    
        print("Say that again please...")  
        return "None"

    return query # contains recognized q=user query as statement

if __name__ == "__main__":
    wishMe()
    while True:
        query=takeCommand().lower() # converts user vocie query to lower case

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1) # getting query search in wikipedia ( 3 sentances)
            speak("According to Wikipedia")
            print(results) # printing the searched result
            speak(results) # speaking it

        elif 'open youtube' in query:
            webbrowser.open("http://youtube.com") # open youtube.com

        elif 'open google' in query:
            webbrowser.open("http://google.com") # open google.com

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com") # open stackoverflow.com

        elif 'play music' in query:
            music_dir="C:\\Users\\Apoorv Varshney\\Downloads\\Music" #  music directory
            songs = os.listdir(music_dir) # list all songs
            print(songs) # print song list
            os.startfile((os.path.join(music_dir,songs[0])))
        
        elif 'time' in query:
            strtime=datetime.datetime.now().strftime("%H:%M:%S") # provides current time
            speak(f"Sr,the time is {strtime}")

        elif 'open vs code' in query: # opens vs code 
            codepath="C:\\Users\\Apoorv Varshney\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif 'open cmd' in query: # open cmd
            cmdpath="C:\\Windows\\System32\\cmd.exe"
            os.startfile(cmdpath)

        elif 'how are you' in query: 
            speak("I am fine, Thank you") 
            speak("How are you, Sir") 
  
        elif 'fine' in query or "good" in query: 
            speak("It's good to know that your fine")

        elif 'search' in query: # searching content on google
            query = query.replace("search", "")
            url="https://www.google.com.tr/search?q={}".format(query)
            webbrowser.open(url)

        elif 'news' in query: # speakin 10 news of today
            url = ('http://newsapi.org/v2/top-headlines?country=in&apiKey=6e2165f0bbbc4917b53e3c154a86e11f')
            response = requests.get(url)
            text = response.text
            my_json = json.loads(text)
            arts=my_json['articles']
            for i in range(10):
                speak('top 10 news headlines are.')
                speak(arts[i]['title'])
                speak('next news.')

        elif 'bye' in query: # code to exit jarvis
            exit()