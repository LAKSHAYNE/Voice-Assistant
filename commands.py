import pywhatkit
import speech_recognition as sr
import playsound  # to play saved mp3 file
from gtts import gTTS  # google text to speech
import os  # to save/open files
import wolframalpha  # to calculate strings into formula
import time
from assi_text import *
from gui import *


class Commands(Gui):
    def __init__(self):
        self.num = 1
        Gui.__init__(self, self.startListen)

    def assistant_speaks(self, output):
        self.num += 1
        # Gui.assistant_text(self,"Assistant : ", output)
        toSpeak = gTTS(text=output, lang='en', slow=False)
        # saving the audio file given by google text to speech
        file = str(self.num) + ".mp3"
        toSpeak.save(file)
        # playsound package is used to play the same file.
        # Gui.checking(self)
        Gui.assistant_text(self, f"Assistant : {output}")
        playsound.playsound(file, True)
        Gui.assistant_text(self, f"Assistant : {output}")
        os.remove(file)

    def get_audio(self):
        rObject = sr.Recognizer()
        audio = ''

        with sr.Microphone() as source:
            Gui.assistant_text(self, "Speak...")
            # recording the audio using speech recognition
            audio = rObject.listen(source, phrase_time_limit=5)
            Gui.assistant_text(self, "Stop.")  # limit 5 secs

        try:
            text = rObject.recognize_google(audio, language='en-US')
            Gui.assistant_text(self, f"You : {text}")
            return text
        except:

            self.assistant_speaks(
                "Could not understand your audio, PLease try again !")
            return self.get_audio()

    def process_text(self, input):
        try:
            if 'search' in input or 'play' in input:
                self.search_web(input)
                return

            elif "who are you" in input or "define yourself" in input:
                speak = '''Hello, I am Your personal Assistant. 
				I am here to make your life easier. You can command me to perform 
				various tasks such as calculating sums or opening applications etcetra'''
                self.assistant_speaks(speak)
                return

            elif "what can you do" in input:
                speak = "My actions depends on what you ask for. I will try my best to provide you with best results. Thank You"
                self.assistant_speaks(speak)
                return

            elif "who made you" in input or "created you" in input:
                speak = "I have been created by Group-9 members which comprise of Ishwam Lakshay Ishika and Mani."
                self.assistant_speaks(speak)
                return

            elif "geeksforgeeks" in input:  # just
                speak = """Geeks for Geeks is the Best Online Coding Platform for learning. Here is result for geeksforgeeks"""
                self.assistant_speaks(speak)
                pywhatkit.search('geeksforgeeks')
                return

            elif "what" in input or "who" in input:
                try:
                    app_id = "3XL874-4GXR8EVV89"  # my wolframaplha id
                    client = wolframalpha.Client(app_id)
                    res = client.query(input)
                    answer = next(res.results).text
                    self.assistant_speaks(answer)
                    return
                except BaseException as e:
                    Gui.assistant_text(self, e)

            elif "calculate" in input.lower():
                # write your wolframalpha app_id here #working
                Gui.assistant_text(self, "calculate called")
                try:
                    app_id = "3XL874-4GXR8EVV89"  # my wolframaplha id
                    client = wolframalpha.Client(app_id)
                    indx = input.lower().split().index('calculate')
                    query = input.split()[indx + 1:]
                    res = client.query(' '.join(query))
                    answer = next(res.results).text
                    self.assistant_speaks("The answer is " + answer)
                    return
                except BaseException as e:
                    Gui.assistant_text(self, e)

            elif "open" in input:
                # another function to open
                # different application availaible
                self.open_application(input.lower())
                return

            else:
                try:
                    app_id = "3XL874-4GXR8EVV89"  # my wolframaplha id
                    client = wolframalpha.Client(app_id)
                    res = client.query(input)
                    answer = next(res.results).text
                    self.assistant_speaks(answer)
                    return
                except BaseException as e:
                    Gui.assistant_text(self, e)
        except:
            self.assistant_speaks(
                "I don't understand, I can search the web for you, Do you want to continue?")
            ans = self.get_audio()
            if 'yes' in str(ans) or 'yeah' in str(ans):
                self.search_web(input)

    def search_web(self, input):

        if 'youtube' in input:
            self.assistant_speaks("Opening in youtube")
            # indx = input.lower().split().index('youtube')
            # query = input.split()[indx + 1:]
            query = input.replace('youtube', '')
            query = query.replace('play', '')
            query = query.replace('search', '')
            query = query.replace('on', '')
            pywhatkit.playonyt(query)
            return

        elif 'wikipedia' in input:
            self.assistant_speaks("Here is your search from Wikipedia")
            query = input.replace('wikipedia', '')
            pywhatkit.info(query, lines=5)
            return

        else:
            self.assistant_speaks("here is your search result")
            query = input.replace("search", '')
            query = query.replace("google", '')
            pywhatkit.search(query)
            time.sleep(15)
            return
    # function used to open application
    # present inside the system.

    def open_application(self, input):
        if "chrome" in input:
            self.assistant_speaks("Opening Google Chrome")
            os.startfile(
                'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')
            return
        elif "firefox" in input or "mozilla" in input:
            self.assistant_speaks("Opening Mozilla Firefox")
            os.startfile('C:\Program Files\Mozilla Firefox\\firefox.exe')
            return
        elif "word" in input:
            self.assistant_speaks("Opening Microsoft Word")
            os.startfile(
                'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\\Word.lnk')
            return
        elif "excel" in input:
            self.assistant_speaks("Opening Microsoft Excel")
            os.startfile(
                'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\\Excel.lnk')
            return
        elif "powerpoint" in input:
            self.assistant_speaks("Opening This PC")
            os.startfile(
                'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\\PowerPoint.lnk')
        elif "whatsapp" in input:
            self.assistant_speaks("Opening Your Whatsapp")
            os.startfile(
                'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\\WhatsApp.lnk')
        elif "edge" in input:
            self.assistant_speaks("Opening Microsoft edge")
            os.startfile(
                'C:\Program Files (x86)\Microsoft\Edge\Application\\msedge.exe')
        elif "epic games" in input:
            self.assistant_speaks("Opening Epic Games")
            os.startfile(
                'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\\Epic Games Launcher.lnk')
        elif "android studio" in input:
            self.assistant_speaks("Opening Android Studio")
            os.startfile(
                'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Android Studio\\Android Studio.lnk')
        elif "sublime text" in input:
            self.assistant_speaks("Opening Your Sublime Text Editor")
            os.startfile(
                'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\\Sublime Text 3.lnk')
        else:
            self.assistant_speaks(
                "Application not available,Therefore showing results on google")
            query = input.replace("open", '')
            pywhatkit.search(query)
            return
    # Driver Code

    def startListen(self):
        if (self.num == 1):
            self.assistant_speaks("Hi, I am Your Assistant. What's your name?")
            name = 'human'
            name = self.get_audio()
            self.assistant_speaks("Hi, " + name)
        self.assistant_speaks("What can i do for you?")
        text = self.get_audio().lower()
        if "thank" in str(text):
            self.assistant_speaks(
                "It is my pleasure to help you. What can I do for you now")
            text = self.get_audio().lower()
        if "exit" in str(text) or "bye" in str(text) or "sleep" in str(text):
            self.assistant_speaks("Ok bye " + name)
            time.sleep(2)
            Gui.destroy()

        # calling process text to process the query
        self.process_text(text)
