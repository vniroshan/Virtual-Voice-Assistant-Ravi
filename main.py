import webbrowser
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import cv2
import requests
import subprocess
import tamil
import time
import os


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()
def stop():
    return 0

def wishMe():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        talk("Hello,Good Morning")
        print("Hello,Good Morning")
        talk("I am ravi \nTell me how may I help you")
        print("I am ravi \nTell me how may I help you")
    elif hour >= 12 and hour < 18:
        talk("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
        talk("I am ravi \nTell me how may I help you")
        print("I am ravi \nTell me how may I help you")
    else:
        talk("Hello,Good Evening")
        print("Hello,Good Evening")
        talk("I am ravi \nTell me how may I help you")
        print("I am ravi \nTell me how may I help you")
    while True:
        run_ravi()
def take_command():
    try:
        listener = sr.Recognizer()
        with sr.Microphone() as source:
            print("listening........")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
    except:
        pass
    return command

def run_ravi():
    command = take_command()
    print(command)
    if 'ravi' in command:
        command = command.replace('ravi', '')
        print(command)
        if 'play' in command:
            song = command.replace('play', '')
            talk('playing' + song)
            pywhatkit.playonyt(song)
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%H:%M %p')
            print(time)
            talk('Current time is ' + time)
        elif 'who is' in command:
            person = command.replace('who is', '')
            info = wikipedia.summary(person, 1)
            print(info)
            talk(info)
        elif'how are you' in command:
            talk('i am well\n and you')
            mgs = take_command()
            if 'fine' in mgs:
                talk('ok, How can help you?')
        elif 'kayana' in command:
            talk('Your name is Kayana')
        elif 'joke' in command:
            talk(pyjokes.get_joke())

        elif 'capital' in command:
            talk('Please say country name')
            capital_name = take_command()
            info = wikipedia.search('capital of ' + capital_name, results = 2 )
            print(info[1])
            talk(info[1])

        elif 'open youtube' in command:
            webbrowser.open_new_tab("https://www.youtube.com/")
            talk("Youtube is open now")
        elif 'media' in command:
            webbrowser.open_new_tab("https://www.youtube.com/channel/UCyaQdMM1EfFPhw4dUcGlyRg")
            talk("nirosh media is open now")
        elif 'news' in command:
            webbrowser.open_new_tab("https://www.newsfirst.lk/latest-news/")
            talk("Here are some headlines from the News First in sri lanka,Happy reading")

        elif 'search' in command:
            statement = command.replace("search", "")
            webbrowser.open_new_tab(statement)

        elif "camera" in command or "take a photo" in command:
            camera_port = 0
            camera = cv2.VideoCapture(camera_port)
            return_value, image = camera.read()
            cv2.imwrite("opencv.png", image)
            del (camera)  # so that others can use the camera as soon as possible

        elif "weather" in command:
            api_key = "0880acada31c8fe4b08afb47bb5eae93"
            base_url = "https://api.openweathermap.org/data/2.5/weather?"
            talk("what is the city name")
            city_name = take_command()
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name
            response = requests.get(complete_url)
            x = response.json()
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                talk(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(city_name)
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))

        elif "log off" in command or "sign out" in command:
            talk("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])

        elif "good bye" in command or "ok bye" in command or "stop" in command:
            talk('your personal assistant is shutting down,Good bye')
            print('your personal assistant is shutting down,Good bye')
            exit()
        else:
            talk('Please say the command again. meendum sollunkal')
    else:
        talk('Please say with Ravi')
wishMe()

