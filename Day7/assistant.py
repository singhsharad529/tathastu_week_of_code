#!/usr/bin/env python3

# Requires PyAudio and PySpeech.

# pip install SpeechRecognition
# pip install gTTS
# pip install pygame

# while running, The code will take some time as it relies on online services.

import webbrowser as wb
import speech_recognition as sr
from tkinter import *
from time import ctime
import time
import os
from gtts import gTTS
import pygame
from pygame import mixer
## from threadpoolctl import threadpool_info

def speak(string):
    b = string
    global x
    if len(b) == 0: # do nothing
        #w1 = Label(root, text="No input!").pack()
        return
    tts = gTTS(text=b, lang='en-us')
    tts.save("voice%s.mp3"%(x))
    # x+=1
    pygame.init()
    pygame.display.set_mode((2, 1))
    mixer.music.load("voice%s.mp3" % (x))
    mixer.music.play(0)

    x += 1

    clock = pygame.time.Clock()
    clock.tick(10)
    while pygame.mixer.music.get_busy():
        pygame.event.poll()
        clock.tick(10)


def recordAudio():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Let's talk to your assistant...")
        testAudio = r.listen(source)
        print("Voice is processing....")
    # Speech recognition using Google Speech Recognition
    data = ""

    try:
        data = r.recognize_google(testAudio)
        print("You said : " + data )
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    return data


def jarvis(data):
    if "how are you" in data:
        speak("I am fine,and you? Hope you are fine")
        speak("any thing else")
        main()

    elif "what time is it" in data:
        speak(ctime())
        speak("Any thing else?")
        main()

    elif "no" in data:
    	speak("Hope we will meet soon,Bye good day")

    elif "where is" in data:
        data = data.split(" ")
        location = data[2]
        speak("Hold on nitesh, I will show you where " + location + " is.")
        wb.open_new_tab("https://www.google.nl/maps/place/" + location + "/&amp;")
        speak("Any thing else?")
        main()
    else :
        speak(",,,,,,,I did not get what you said !,please speak again")
        main()





def main():
	speak("Ask what you like....")
	voice= recordAudio()  
	jarvis(voice)  



x=0
print("Hi, I am your assistant..")
speak("Hello, I am your assistant ,how can i help you ?")
voice = recordAudio() # DO speech recognition
## data = "what time is it"
jarvis(voice) ## Process the text
speak("Turning off the program.")
print("Run complete")
