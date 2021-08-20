#!/usr/bin/env python3

import speech_recognition as sr
import os
import espeakng
import time
from datetime import datetime

mySpeaker = espeakng.Speaker()
mySpeaker.voice = 'hu'
recognizer = sr.Recognizer()
mic = sr.Microphone()


def take_command():
    try:
        with mic as source:
            audio = recognizer.listen(source)
            output = recognizer.recognize_google(audio, None, 'hu-HU').lower()
            output = output.lower()
            if output is not None and 'ubuntu' in output:
                output = output.replace('ubuntu', '')
                return output
    except sr.UnknownValueError:
        # mySpeaker.say('Bocs! Most nem érek rá.')
        time.sleep(2)


def virtual_assistant():
    output = take_command()
    print(output)
    if output is not None:
        if "fájl" in output:
            os.system('nautilus')
        elif "terminál" in output:
            os.system('gnome-terminal')
        elif ("level" or "levél") in output:
            os.system('thunderbird')
        elif ("zene" or "zené") in output:
            os.system('spotify')
        elif output.split()[0].lower() == "google":
            search = " ".join(output.split()[1:])
            os.system(f"google-chrome google.com/search?q='{search}'")
        elif 'pihenj' in output:
            exit()
        elif "óra" or "pontos idő" in output:
            now = datetime.now()
            current_hour = now.strftime("%H")
            current_minute = now.strftime("%M")
            mySpeaker.say("A pontos idő " + current_hour + "óra " + current_minute + "perc ");
        else:
            mySpeaker.say('Bocs! Nem értettem.')
            # time.sleep(2)


def run():
    while True:
        virtual_assistant()


if __name__ == "__main__":
    run()
