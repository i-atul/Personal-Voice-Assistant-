import pyttsx3 
import speech_recognition as sr
import webbrowser
from pywikihow import search_wikihow
from bs4 import BeautifulSoup
import pywhatkit
import wikipedia
from googletrans import Translator
import os
import pyautogui
import psutil
import requests
from gtts import gTTS
import PyPDF2
from pytube import YouTube
import datetime
from playsound import playsound
import keyboard
import pyjokes

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[4].id)
engine.setProperty('rate',170)

def Speak(Audio):
    print("   ")
    print(f": {Audio}")
    engine.say(Audio)
    print("    ")
    engine.runAndWait()



def takecommand(): 
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("          ")
        print("Listening...")
        r.pause_threshold = 0.6
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"Your Command :  {query}\n")

    except:   
        return "None"
        
    return query.lower()

def TaskExe():



    def Music():
        Speak("Tell Me The NamE oF The Song!")
        musicName = takecommand()

        if 'shape of you' in musicName:
            os.startfile('C:\\Users\\DELL\\Desktop\\voiceass\\music\\ytmp3free.cc_shape-of-you-ed-sheeran-lyrics-youtubemp3free.org.mp3')

        elif 'fearless' in musicName:
            os.startfile('C:\\Users\\DELL\\Desktop\\voiceass\\music\\338420715.mp3')

        else:

            pywhatkit.playonyt(musicName)

        Speak("Your Song Has Been Started! , Enjoy Sir!")


    def OpenApps():
        Speak("Ok Sir , Wait A Second!")
        
        if 'code' in query:
            os.startfile("C:\\Users\\DELL\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")

        elif 'powerpoint' in query:
            os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE")

        elif 'excel' in query:
            os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE")

        elif 'wordpad' in query:
            os.startfile("C:\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE")

        elif 'chrome' in query:
            os.startfile("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")
        
        elif 'david' in query:
            os.startfile("C:\\Users\\DELL\\Desktop\\voiceass\\david.exe")
        
        elif 'facebook' in query:
            webbrowser.open('https://www.facebook.com/') 

        elif 'news' in query:
            webbrowser.open('https://www.moneycontrol.com/')
        
        elif 'linkedin' in query:
            webbrowser.open('https://in.linkedin.com/')
       
        elif 'twitter' in query:
            webbrowser.open('https://twitter.com/')

        elif 'map' in query:
            webbrowser.open('https://www.google.co.in/maps/place/Naraina+College+Of+Engineering+%26+Technology/@26.4753199,80.2235036,17z/data=!3m1!4b1!4m12!1m6!3m5!1s0x399c363184b23723:0x77a77b7a113116e5!2sNaraina+College+Of+Engineering+%26+Technology!8m2!3d26.4753199!4d80.2256976!3m4!1s0x399c363184b23723:0x77a77b7a113116e5!8m2!3d26.4753199!4d80.2256976/')

        elif 'youtube' in query:
            webbrowser.open('https://www.youtube.com')

        Speak("Your Command Has Been Completed Sir!")

    def CloseAPPS():
        Speak("Ok Sir , Wait A second!")

        if 'code' in query:
            os.system("TASKKILL /F /im Code.exe")
        
        if 'david' in query:
            os.system("TASKKILL /F /im david.exe")

        elif 'chrome' in query:
            os.system("TASKKILL /f /im chrome.exe")

        elif 'powerpoint' in query:
            os.system("TASKKILL /F /im POWERPNT.EXE")
        
        elif 'excel' in query:
            os.system("TASKKILL /F /im EXCEL.EXE")
       
        elif 'wordpad' in query:
            os.system("TASKKILL /F /im WINWORD.EXE")

        elif 'youtube' in query:
            os.system("TASKKILL /F /im chrome.exe")
        
        elif 'map' in query:
            os.system("TASKKILL /F /im chrome.exe")
       
        elif 'news' in query:
            os.system("TASKKILL /F /im chrome.exe")
       
        elif 'linkedin' in query:
            os.system("TASKKILL /F /im chrome.exe")
       
        elif 'twitter' in query:
            os.system("TASKKILL /F /im chrome.exe")
        
        elif 'facebook' in query:
            os.system("TASKKILL /F /im chrome.exe")
            
        Speak("Your Command Has Been Succesfully Completed!")

#tempreture

    def Temp():
        search = "temperature in Kanpur"
        url = f"https://www.google.com/search?q={search}"
        r = requests.get(url)
        data = BeautifulSoup(r.text,"html.parser")
        temperature = data.find("div",class_ = "BNeawe").text
        Speak(f"The Temperature Outside Is {temperature} celcius")

        Speak("Do I Have To Tell You Another Place Temperature ?")
        next = takecommand()

        if 'yes' in next:
            Speak("Tell Me The Name Of tHE Place ")
            name = takecommand()
            search = f"temperature in {name}"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temperature = data.find("div",class_ = "BNeawe").text
            Speak(f"The Temperature in {name} is {temperature} celcius")

        else:
            Speak("no problem sir")

#reader

    def Reader():
        Speak("Tell Me The Name Of The Book!")

        name = takecommand()

        if 'computer' in name:

            os.startfile('C:\\Users\\DELL\\Desktop\\voiceass\\notes\\Let Us C - Yashwant Kanetkar(www.clanguagecodding.ooo).pdf')
            book = open('C:\\Users\\DELL\\Desktop\\voiceass\\notes\\Let Us C - Yashwant Kanetkar(www.clanguagecodding.ooo).pdf','rb')
            pdfreader = PyPDF2.PdfFileReader(book)
            pages = pdfreader.getNumPages()
            Speak(f"Number Of Pages In This Books Are {pages}")
            Speak("From Which Page I Have To Start Reading ?")
            numPage = int(input("Enter The Page Number :"))
            page = pdfreader.getPage(numPage)
            text = page.extractText()
            Speak("In Which Language , I Have To Read ?")
            lang = takecommand()

            if 'hindi' in lang:
                transl = Translator()
                textHin = transl.translate(text,'hi')
                textm = textHin.text
                speech = gTTS(text = textm )
                try:
                    speech.save('book.mp3')
                    playsound('book.mp3')

                except:
                    playsound('book.mp3')

            else:
                Speak(text)

        elif 'trade' in name:
            os.startfile('C:\\Users\\DELL\\Desktop\\voiceass\\notes\\International trade.pdf')
            book = open('C:\\Users\\DELL\\Desktop\\voiceass\\notes\\International trade.pdf','rb')
            pdfreader = PyPDF2.PdfFileReader(book)
            pages = pdfreader.getNumPages()
            Speak(f"Number Of Pages In This Books Are {pages}")
            Speak("From Which Page I Have To Start Reading ?")
            numPage = int(input())
            page = pdfreader.getPage(numPage)
            text = page.extractText()
            Speak("In Which Language , I Have To Read ?")
            lang = takecommand()

            if 'hindi' in lang:
                transl = Translator()
                textHin = transl.translate(text,'hi')
                textm = textHin.text
                speech = gTTS(text = textm )
                try:

                    speech.save('book.mp3')
                    playsound('book.mp3')

                except:
                    playsound('book.mp3')

            else:
                Speak(text)

 #youtbe automation  

    def YoutubeAuto():
        Speak("Whats Your Command ?")
        comm = takecommand()

        if 'stop' in comm:
            keyboard.press('space bar')

        elif 'restart' in comm:
            keyboard.press('0')

        elif 'mute' in comm:
            keyboard.press('m')

        elif 'skip' in comm:
            keyboard.press('l')

        elif 'back' in comm:
            keyboard.press('j')

        elif 'full screen' in comm:
            keyboard.press('f')

        elif 'film mode' in comm:
            keyboard.press('t')

        Speak("Done Sir")


#chrom automation
        
    def ChromeAuto():
        Speak("Chrome Automation started!")

        command = takecommand()

        if 'close this tab' in command:
            keyboard.press_and_release('ctrl + w')

        elif 'open new tab' in command:
            keyboard.press_and_release('ctrl + t')

        elif 'open new window' in command:
            keyboard.press_and_release('ctrl + n')

        elif 'history' in command:
            keyboard.press_and_release('ctrl +h')


        elif 'menu' in command:
            keyboard.press_and_release('Alt + f')

        elif 'reload' in command:
            keyboard.press_and_release('Ctrl + r')

        elif 'default' in command:
            keyboard.press_and_release('Ctrl + 0')


    while True:

        query = takecommand()

        if 'hello' in query:
            Speak("Hello Sir , I Am Emma .")
            Speak("Your Personal AI Assistant!")
            Speak("How can I Help You?")

        elif 'how are you' in query:
            Speak("I Am Fine Sir!")
            Speak("Whats About YOU?")

        elif 'you need a break' in query:
            Speak("Ok Sir , You Can Call Me Anytime !")
            Speak("Just Say Wake Up Jarvis!")
            break

        elif 'youtube search' in query:
            Speak("OK sIR , This Is What I found For Your Search!")
            query = query.replace("jarvis","")
            query = query.replace("youtube search","")
            web = 'https://www.youtube.com/results?search_query=' + query
            webbrowser.open(web)
            Speak("Done Sir!")

        elif 'website' in query:
            Speak("Ok Sir , Launching.....")
            query = query.replace("jarvis","")
            query = query.replace("website","")
            query = query.replace(" ","")
            web1 = query.replace("open","")
            web2 = 'https://www.' + web1 + '.com'
            webbrowser.open(web2)
            Speak("Launched!")

        elif 'launch' in query:
            Speak("Tell Me The Name Of The Website!")
            name = takecommand()
            web = 'https://www.' + name + '.com'
            webbrowser.open(web)
            Speak("Done Sir!")

        elif 'wikipedia' in query:
            Speak("Searching Wikipedia.....")
            query = query.replace("jarvis","")
            query = query.replace("wikipedia","")
            wiki = wikipedia.summary(query,2)
            Speak(f"According To Wikipedia : {wiki}")

        
        elif 'play music' in query:
            Music()
#open and close app

        elif 'open facebook' in query:
            OpenApps()

        elif 'open news' in query:
            OpenApps()
       
        elif 'open linkedin' in query:
            OpenApps()
        
        elif 'open twitter' in query:
            OpenApps()

        elif 'open map' in query:
            OpenApps()

        elif 'open code' in query:
            OpenApps()

        elif 'open youtube' in query:
            OpenApps()
            
        elif 'open powerpoint' in query:
            OpenApps()

        elif 'open excel' in query:
            OpenApps()
        elif 'open chrome' in query:
            OpenApps()

        elif 'open wordpad' in query:
            OpenApps()   
        elif 'connect david' in query:
            OpenApps()   



        elif 'close wordpad' in query:
            CloseAPPS()
        elif 'disconnect david' in query:
            CloseAPPS()

        elif 'close chrome' in query:
            CloseAPPS()

        elif 'close excel' in query:
            CloseAPPS()

        elif 'close powerpoint' in query:
            CloseAPPS()
        elif 'close youtube' in query:
            CloseAPPS()
        elif 'close code' in query:
            CloseAPPS()
        elif 'close map' in query:
            CloseAPPS()
        elif 'close twitter' in query:
            CloseAPPS()
        elif 'close linkedin' in query:
            CloseAPPS()
        elif 'close news' in query:
            CloseAPPS()
        elif 'close facebook' in query:
            CloseAPPS()

#youtube automation

        elif 'stop' in query:
            keyboard.press('space bar')

        elif 'restart' in query:
            keyboard.press('0')

        elif 'mute' in query:
            keyboard.press('m')

        elif 'skip' in query:
            keyboard.press('l')

        elif 'back' in query:
            keyboard.press('j')

        elif 'full screen' in query:
            keyboard.press('f')

        elif 'film mode' in query:
            keyboard.press('t')

        elif 'youtube tool' in query:
            YoutubeAuto()

        
#google automations
        
        elif 'chrome automation' in query:
            ChromeAuto()

        elif 'close the tab' in query:
            keyboard.press_and_release('ctrl + w')

        elif 'open new tab' in query:
            keyboard.press_and_release('ctrl + t')

        elif 'open new window' in query:
            keyboard.press_and_release('ctrl + n')

        elif 'history' in query:
            keyboard.press_and_release('ctrl +h')

        elif 'menu' in query:
            keyboard.press_and_release('Alt + f')

        elif 'reload' in query:
            keyboard.press_and_release('Ctrl + r')

        elif 'default' in query:
            keyboard.press_and_release('Ctrl + 0')

#joke
        elif 'joke' in query:
            get = pyjokes.get_joke()
            Speak(get)

#repeat my word

        elif 'repeat my word' in query:
            Speak("Speak Sir!")
            jj = takecommand()
            Speak(f"You Said : {jj}")


        elif 'open my location' in query:
            Speak("Ok Sir , Wait A Second!")
            webbrowser.open('https://www.google.com/maps/place/Naraina+College+Of+Engineering+%26+Technology/@26.4753199,80.2235089,17z/data=!3m1!4b1!4m5!3m4!1s0x399c363184b23723:0x77a77b7a113116e5!8m2!3d26.4753199!4d80.2256976')

        elif 'set alarm' in query:
            Speak("Enter The Time !")
            time = input(": Enter The Time :")

            while True:
                Time_Ac = datetime.datetime.now()
                now = Time_Ac.strftime("%H:%M:%S")

                if now == time:
                    Speak("Time To Wake Up Sir!")
                    playsound('iron.mp3')
                    Speak("Alarm Closed!")

                elif now>time:
                    break
                    
        
        elif 'remember that' in query:
            remeberMsg = query.replace("remember that","")
            remeberMsg = remeberMsg.replace("jarvis","")
            Speak("You Tell Me To Remind You That :"+remeberMsg)
            remeber = open('data.txt','w')
            remeber.write(remeberMsg)
            remeber.close()

     

        elif 'what do you remember' in query:
            remeber = open('data.txt','r')
            Speak("You Tell Me That" +remeber.read())

# google search 


        elif 'google search' in query:
            import wikipedia as googleScrap
            query = query.replace("jarvis","")
            query = query.replace("google search","")
            query = query.replace("google","")
            Speak("This Is What I Found On The Web!")
            pywhatkit.search(query)

            try:
                result = googleScrap.summary(query,2)
                Speak(result)

            except:
                Speak("No Speakable Data Available!")

        elif 'how to' in query:
            Speak("Getting Data From The Internet !")
            op = query.replace("jarvis","")
            max_result = 1
            how_to_func = search_wikihow(op,max_result)
            assert len(how_to_func) == 1
            how_to_func[0].print()
            Speak(how_to_func[0].summary)
            
        elif 'today temperature' in query:
            Temp()

        elif 'read book' in query:
            Reader()
         
TaskExe()