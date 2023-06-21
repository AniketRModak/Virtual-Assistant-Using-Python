import speech_recognition as sr
import os
import win32com.client
import webbrowser
from playsound import playsound
from AppOpener import open
import openai
from config import apikey

def say(text2):
    spekar = win32com.client.Dispatch("SAPI.Spvoice")
    spekar.speak(text2)

chatStr = ""
def chat(query):
    global chatStr
    print(chatStr)
    openai.api_key = apikey
    chatStr += f"Aniket: {query}\n veer: "
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt= chatStr,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # todo: Wrap this inside of a  try catch block
    try:
        say(response["choices"][0]["text"])
        chatStr += f"{response['choices'][0]['text']}\n"
        return response["choices"][0]["text"]
    except Exception as e:
        return "try again. Sorry from vertual device"

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.pause_threshold = 0.6
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            # print(f"User said: {query}")
            return query
        except Exception as e:
            return "try again. Sorry from vertual device"


if __name__ == '__main__':
    say(f"hello i am veer  ")
    while True:
        print("listnling......")
        query=takeCommand()
        sites=[["youtube","https://www.youtube.com"],["google","https://www.google.com"],["shop more","http://shopmore.rf.gd"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"opening {site[0]} sir")
                webbrowser.open(site[1])
                break
        if "open music" in query:
            playsound('C:\\Users\Aniket Modak\OneDrive\Desktop\All language\python\\Scam.mp3')


        if "open Camera".lower() in query.lower():
            say("opening camera")
            open("Camera")


        elif "veer Quit".lower() in query.lower():

            exit()

        elif "reset chat".lower() in query.lower():

             chatStr = ""


        else:

            print("Chatting...")

            chat(query)
