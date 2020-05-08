import speech_recognition as sr
import pyttsx3
import datetime as dt
import webbrowser
import re
import subprocess
import os
import random as rnd
import requests
from bs4 import BeautifulSoup
import wikipedia
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from mainwindow import *
from functools import partial


class App(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


ui = Ui_MainWindow()
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui.setupUi(MainWindow)


class Tasks:
    def command(self, task):
        """ Coordinate method.

            The method directs user's task to other methods.
            :param task:
        """
        if any(x in task.split() for x in self.notebook):
            self.note(task)
        elif 'launch ' in task or 'open ' in task or 'show ' in task:
            launch_task = re.search('launch (.*)', task) or re.search('open (.*)', task) or re.search('show (.*)', task)
            launch_task = launch_task.group(1).replace("ms ", "")
            launch_task = launch_task.replace("microsoft ", "")
            if launch_task.replace(" ", "") in list(zip(*self.ms))[0]:
                launch_task = launch_task.replace(" ", "")
                self.ms_office(launch_task)
            elif 'photo' in launch_task or 'picture' in launch_task or 'pictures' in launch_task:
                self.picture()
            elif 'video' in launch_task:
                self.video()
            elif '.' in launch_task:
                url = 'https://www.' + launch_task.replace(" ", "")
                webbrowser.open(url)
            else:
                self.talk("Sorry, I can't open it.")
        elif 'play ' in task:
            play_task = re.search('play (.*)', task)
            play_task = play_task.group(1)
            if 'music' in play_task:
                self.music()
            elif 'game' in play_task:
                self.talk("Sorry, I'm too little to play games.")
            elif 'video' in play_task:
                self.video()
            else:
                self.youtube(task, play_task)
        elif 'random number' in task:
            random_task = re.search('random number(.*)', task)
            random_task = random_task.group(1)
            self.random_number(random_task)
        elif (('calculate ' in task or 'solve ' in task or "what's " in task or 'what is ' in task) \
                and any(x in task.split() for x in self.arifm)) or ((any(x in task.split() for x in self.arifm))\
                or (any(x in tuple(task) for x in self.arifm))):
            calc_task = re.search('calculate (.*)', task) or re.search('solve (.*)', task)\
                        or re.search("what's (.*)", task) or re.search('what is (.*)', task) or re.search('(.*)', task)
            calc_task = calc_task.group(1)
            calc_task = calc_task.replace('^', '**')
            calc_task = calc_task.replace('x', '*')
            if calc_task[0] in self.arifm or calc_task[0].isdigit():
                self.calculator(calc_task)
            elif "what's " in task or 'what is ' in task:
                self.googling(calc_task)
        elif any(x in task for x in self.info):
            try:
                search_task = re.search('about (.*)', task) or re.search('is (.*)', task) or re.search("what's (.*)", task)
                search_task = search_task.group(1)
                self.googling(search_task)
            except AttributeError:
                self.googling('speech')
        elif 'aria bye' in task or 'aria exit' in task or 'aria close' in task or 'aria bye-bye' in task:
            bye = rnd.choice(self.goodbyes)
            self.talk(bye)
            exit()

    def note(self, task):
        """ Operations with notes.

            The method creates notes and open notebook.
            :param task:
        """
        if any(x in task for x in self.notebook) and not ('open' in task or 'show' in task or 'check' in task):
            note = self.dictation()
            if note != '':
                with open('Notebook.txt', 'a', encoding='utf-8') as file:
                    file.write(f"Note. {dt.datetime.now()}\n")
                    file.write(note), file.write('\n\n')
        if 'open' in task or 'show' in task or 'check' in task:
            try:
                os.startfile("C:\  Users\Елена\Desktop\Course work\  Notebook.txt".replace("  ", ""))
            except:
                self.talk("Can't open it.")

    def ms_office(self, task):
        """ "Microsoft Office" pack.

            The method opens apps from "Microsoft Office" pack.
            :param task:
        """
        ind = list(zip(*self.ms))[0].index(task)
        app = self.ms[ind][1] + ".exe"
        path = "C:\Program Files (x86)\Microsoft Office\  root\Office16\  ".replace("  ", "")
        if task == 'onedrive':
            path = "C:\Windows\FileManager\ ".replace(" ", "")
        try:
            subprocess.Popen([path + app], stdout=subprocess.PIPE)
        except:
            self.talk("Can't open it.")

    def picture(self):
        """ Random picture.

            The method opens random pictures from local folder, if there are any pictures.
        """
        pictures_format = ['.tif', '.jpg', '.gif', '.png']
        DIR = 'C:\ Users\Елена\Pictures\ '.replace(" ", "")
        files_list = os.listdir(DIR)
        pictures_list = []
        for picture in files_list:
            name, end = os.path.splitext(picture)
            if end.lower() in pictures_format:
                pictures_list.append(name + end)
        if len(pictures_list) == 0:
            self.talk('Sorry, your folder is empty.')
        else:
            os.startfile(DIR + rnd.choice(pictures_list))
            pictures_list.clear()

    def music(self):
        """ Random music.

            The method opens random music from local folder, if there are any music.
        """
        try:
            DIR = 'C:\ Users\Елена\Music\ '.replace(" ", "")
            files_list = os.listdir(DIR)
            music_list = []
            for picture in files_list:
                name, end = os.path.splitext(picture)
                if end.lower() == '.mp3':
                    music_list.append(name + end)
            if len(music_list) == 0:
                self.talk('Sorry, your folder is empty.')
            else:
                os.startfile(DIR + rnd.choice(music_list))
                music_list.clear()
        except:
            self.talk("Can't play music.")

    def video(self):
        """ Random video.

            The method opens random videos from local folder, if there are any videos.
        """
        try:
            DIR = 'C:\ Users\Елена\Videos\ '.replace(" ", "")
            video_format = ['.mp4', '.avi', '.wmv', '.mov', '.mpeg4', '.dv', '.xvid', '.divx']
            files_list = os.listdir(DIR)
            video_list = []
            for picture in files_list:
                name, end = os.path.splitext(picture)
                if end.lower() in video_format:
                    video_list.append(name + end)
            if len(video_list) == 0:
                self.talk('Sorry, your folder is empty.')
            else:
                os.startfile(DIR + rnd.choice(video_list))
                video_list.clear()
        except:
            self.talk("Can't play video.")

    def youtube(self, task, clip):
        """ Play videos on youtube.com.

            Behind the specified video title, the method searches for it on youtube.com and plays it.
            If there is nothing videos with this name, the method will search for it by Google searcher.
            :param task:
            :param clip:
        """
        try:
            url = 'https://www.youtube.com/results?search_query=' + clip
            search_result = requests.get(url).text
            soup = BeautifulSoup(search_result, 'html.parser')
            videos = soup.select(".yt-uix-tile-link")
            if not videos:
                url = 'https://www.google.com.ua/search?q=' + task
                webbrowser.open(url)
                return
            link = "https://www.youtube.com" + videos[0]["href"]
            webbrowser.open(link)
        except requests.exceptions.ConnectionError:
            self.talk('No Internet connection.')

    def calculator(self, task):
        """ Calculator.

            The method calculates user's mathematical examples.
            :param task:
        """
        try:
            res = eval(task)
            self.talk(str(res))
        except SyntaxError:
            self.talk('Unexpected data.')

    def googling(self, task):
        """ Search information.

            The method searchs for information on wikipedia.org or google.com.
            :param task:
        """
        try:
            ny = wikipedia.page(task)
            ind = ny.content.index('\n')
            res = ny.content[:ind+1]
            self.talk(str(res))
        except wikipedia.PageError:
            url = 'https://www.google.com.ua/search?q=' + task
            webbrowser.open(url)
        except wikipedia.DisambiguationError:
            url = 'https://www.google.com.ua/search?q=' + task
            webbrowser.open(url)
        except requests.exceptions.ConnectionError:
            self.talk('No Internet connection.')

    def random_number(self, random_task):
        """ Random number.

            The method outputs random numbers.
            :param random_task:
        """
        start = 0
        end = 100
        if random_task != '':
            num = []
            for i in random_task.split():
                if i.isdigit():
                    num.append(int(i))
            num.sort()
            if len(num) == 0:
                self.talk('Unexpected data.')
                return
            elif len(num) == 1:
                if num[0] > 0:
                    start = 0
                    end = num[0]
                else:
                    start = num[0]
                    end = 0
            elif len(num) >= 2:
                start = num[0]
                end = num[1]
        random_number = rnd.randint(start, end)
        self.talk(str(random_number))


class Engine(Tasks):
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')
        self.ms = [('word', 'WINWORD'), ('excel', 'EXCEL'), ('powerpoint', 'POWERPNT'), ('onenote', 'ONENOTE'),
                   ('publisher', 'MSPUB'), ('outlook', 'OUTLOOK'), ('access', 'MSACCESS'), ('skype', 'lync'),
                   ('onedrive', 'FileManager')]
        self.notebook = ['make a note', 'write down', 'remember', 'note', 'notes', 'notebook']
        self.goodbyes = ['Bye-bye!', 'See you later!', 'Bye!', 'Goodbye!']
        self.info = ['find', 'tell me about', 'info', 'info about', 'information', 'information about', 'what is', "what's", 'search', 'about']
        self.arifm = ['+', '-', '*', '/', '**', 'x', '^', '(', ')']

    def talk(self, string):
        """ Reproduce the text.

            The method reproduces the text from string.
            :param string:
        """
        interface.chat(string)
        self.engine.runAndWait()
        self.engine.say(str(string))
        self.engine.runAndWait()

    def speaking(self):
        """ Input voice messages.

            The method gets the voice message and translate it into text.
        """
        reco = sr.Recognizer()
        ui.Chat.append('Aria: ' + "Speak...")
        self.engine.runAndWait()
        with sr.Microphone() as source:
            reco.pause_threshold = 1
            reco.adjust_for_ambient_noise(source, duration=1)
            audio = reco.listen(source)
        try:
            flag = 1
            task = reco.recognize_google(audio).lower()
            interface.chat(task.capitalize(), flag)
        except sr.UnknownValueError:
            self.talk('Sorry, I misheard you. Please repeat.')
        except sr.RequestError:
            self.talk('No Internet connection.')
        return

    def dictation(self):
        """ Record user's messages.

            The method record user's messages for notes and translate it into text.
        """
        reco = sr.Recognizer()
        ui.Chat.append('Aria: ' + "Dictate...")
        self.engine.runAndWait()
        with sr.Microphone() as source:
            reco.pause_threshold = 1
            reco.adjust_for_ambient_noise(source, duration=1)
            audio = reco.listen(source)
        try:
            letter = reco.recognize_google(audio)
            ui.Chat.append('You: ' + letter)
            self.engine.runAndWait()
            return letter
        except sr.UnknownValueError:
            self.talk('Sorry, I misheard you. Please repeat.')
            return ''
        except sr.RequestError:
            self.talk('No Internet connection.')
            return ''


class Interface(Engine):
    def chat(self, message, flag=0):
        """ Control chat.

            The methods outputs every speeches.
            :param message:
            :param flag:
        """
        if message != '':
            if flag:
                ui.Chat.append('You: ' + message)
                self.command(message.lower())
            else:
                ui.Chat.append('Aria: ' + message)
            ui.Text_input.clear()
            self.engine.runAndWait()

    def copy_past(self):
        """ Get text from QLineEdit.

            The method gets user's text from QLineEdit. Add user's speech to QTextEdit.
        """
        if ui.Text_input.text() != '':
            task = ui.Text_input.text().lower()
            ui.Chat.append('You: ' + task.capitalize())
            ui.Text_input.clear()
            self.command(task.strip('.'))

    def main(self):
        """ The method contains all buttons. """
        ui.Enter.clicked.connect(self.copy_past)
        ui.Microphone.clicked.connect(self.speaking)
        ui.Make_a_note_btn.clicked.connect(partial(self.chat, ui.Make_a_note_btn.text(), 1))
        ui.Check_notes_btn.clicked.connect(partial(self.chat, ui.Check_notes_btn.text(), 1))
        ui.Open_MS_Word_btn.clicked.connect(partial(self.chat, ui.Open_MS_Word_btn.text(), 1))
        ui.Show_random_picture_btn.clicked.connect(partial(self.chat, ui.Show_random_picture_btn.text(), 1))
        ui.Open_donnu_btn.clicked.connect(partial(self.chat, ui.Open_donnu_btn.text(), 1))
        ui.Play_music_btn.clicked.connect(partial(self.chat, ui.Play_music_btn.text(), 1))
        ui.Play_video_btn.clicked.connect(partial(self.chat, ui.Play_video_btn.text(), 1))
        ui.Play_DL_WT_btn.clicked.connect(partial(self.chat, ui.Play_DL_WT_btn.text(), 1))
        ui.Show_random_number_btn.clicked.connect(partial(self.chat, ui.Show_random_number_btn.text(), 1))
        ui.Calculate_btn.clicked.connect(partial(self.chat, ui.Calculate_btn.text(), 1))
        ui.Python_btn.clicked.connect(partial(self.chat, ui.Python_btn.text(), 1))
        ui.Aria_close_btn.clicked.connect(partial(self.chat, ui.Aria_close_btn.text(), 1))


if __name__ == '__main__':
    e = Engine()
    interface = Interface()
    greetings = ['Hi', 'Hello']
    greeting = rnd.choice(greetings)
    interface.main()
    MainWindow.show()
    e.talk(greeting)
    sys.exit(app.exec_())
