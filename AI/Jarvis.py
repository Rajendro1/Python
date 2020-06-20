from datetime import datetime
import os
import webbrowser

import pyttsx3
import speech_recognition as sr
import wikipedia

engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
# print(voices[1])
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    """ This Function Wish Us When He First Speak"""
    hour = int(datetime.now().hour)
    if 4 <= hour < 12:
        speak('Good Morning, Have A Nice Day')
    elif 12 <= hour < 17:
        speak('Good Afternoon')
    elif 17 <= hour < 22:
        speak("Good Evening")
    else:
        speak('Good Night, Now Time To Sleep')


def takeCommand():
    """ It Takes Microphone Voices input From User To Give
    Output Of The String"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        # r.energy_threshold = 2000
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")

    except Exception as e:
        speak("Say that again please")
        return 'None'
    return query


if __name__ == '__main__':
    # speak('Rajendro Is Good Boy')
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace('wikipedia', "")
            results = wikipedia.summary(query, sentences=1)
            speak('According to Wikipedia')
            print(results)
            speak(results)
        if 'open youtube' in query:
            webbrowser.open_new_tab('youtube.com/')

        if 'shutdown' in query:
            os.system('shutdown /s')

        if 'cancel shutdown' in query:
            os.system('shutdown /a')

        if "time" in query:
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            speak(f"Current Time {current_time}")

        if 'exit' in query:
            os.system("exit()")

        if 'open google chrome' in query:
            chrome_path = 'C:\\Users\\Public\\Desktop\\"Google Chrome.lnk"'
            print(os.system(chrome_path))

        if 'play music' in query:
            music_dir = 'C:\\Users\\rajan\\Downloads\\Loading-and-chambering-gun-www.fesliyanstudios.com.mp3'
            print(os.system(music_dir))

        if 'open pycharm' in query:
            pycharm_path = 'C:\\Users\\Public\\Desktop\\"PyCharm Community Edition 2020.1 x64.lnk"'
            print(os.system(pycharm_path))

        if 'open virtualbox' in query:
            virtual_box = 'C:\\Users\\Public\\Desktop\\"Oracle VM VirtualBox.lnk"'
            print(os.system(virtual_box))

        if 'close virtualbox' in query:
            os.system('taskkill /im VBoxSVC.exe /im VirtualBox.exe')

        if 'searching google' in query:
            query = query.replace('searching', "")
            print(f"you said\n {query}")
            url = 'https://www.google.com/search?q='
            search_result = url + query
            webbrowser.open(search_result)
        if 'close google' in query:
            print(os.system('taskkill /im chrome.exe'))

        if 'project' in query:
            print(os.system('E:\\Python3.7\\Project\\Web Development\\Flask\\type ..'))

        # All Cmd Commands
        if 'stop' in query:
            print(os.system(''))
        if 'who am i' in query:
            print(os.system('whoami /all'))
        if 'open CMD' in query:
            print(os.system('start'))
            print(os.system('deactivate'))
