import speech_recognition as sr
import os
import sys
import re



def sundayResponse(audio):
    "speaks audio passed as argument"
    print(audio)
    for line in audio.splitlines():
        os.system("say " + audio)
def myCommand(user_command_entered):
    "listens for commands"
    user_input = sr.Recognizer()
    with sr.Microphone() as source:
        print('Say something...')
        user_input.pause_threshold = 1
        user_input.adjust_for_ambient_noise(source, duration=1)
        audio = user_input.listen(source)
    try:
        user_command_entered = user_input.recognize_google(audio).lower()
        print('You said: ' + user_command_entered + '\n')
    #loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        print('....')
        user_command_entered = myCommand();
    return user_command_entered