import subprocess
import wolframalpha
import pyttsx3
import tkinter
import json
import random
import operator
import requests
import pyautogui
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import winshell
import pyjokes
import feedparser
import smtplib
import ctypes
import time
import requests
import shutil
from twilio.rest import Client
from clint.textui import progress
from ecapture import ecapture as ec
import win32com.client as wincl
from urllib.request import urlopen
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices)
engine.setProperty('voice', voices[3].id)
engine.setProperty("rate",170)
def speak(audio):
	engine.say(audio)
	engine.runAndWait()

def wishMe():
	hour = int(datetime.datetime.now().hour)
	if hour>= 0 and hour<12:
		speak("Good Morning Sir !")

	elif hour>= 12 and hour<18:
		speak("Good Afternoon Sir !")

	else:
		speak("Good Evening Sir !")

	assname =("david")
	speak("I am your Assistant")
	speak(assname)
	

def username():
	speak("What should i call you sir")
	uname = takeCommand()
	speak("Welcome Mister")
	speak(uname)
	columns = shutil.get_terminal_size().columns
	
	print("#####################".center(columns))
	print("Welcome Mr.", uname.center(columns))
	print("#####################".center(columns))
	
	speak("How can i Help you, Sir")

def takeCommand():
	
	r = sr.Recognizer()
	
	with sr.Microphone() as source:
		
		print("Listening...")
		r.pause_threshold = 1
		r.pause_threshold = 1
		r.energy_threshold = 300
		audio = r.listen(source)

	try:
		print("Recognizing...")
		query = r.recognize_google(audio, language ='en-in')
		print(f"User said: {query}\n")

	except Exception as e:
		print(e)
		print("Unable to Recognize your voice.")
		return "None"
	
	return query

if __name__ == '__main__':
	clear = lambda: os.system('cls')
	
	clear()
	wishMe()
	username()
	
	while True:
		
		query = takeCommand().lower()
		

		if 'wikipedia' in query:
			speak('Searching Wikipedia...')
			query = query.replace("wikipedia", "")
			results = wikipedia.summary(query, sentences = 3)
			speak("According to Wikipedia")
			print(results)
			speak(results)




		elif 'how are you' in query:
			speak("I am Fine, Thank you")
			speak("How are you, Sir")
		

		elif 'fine' in query or "good" in query:
			speak("It's good to know that your fine")

		elif "change my name to" in query:
			query = query.replace("change my name to", "")
			assname = query

		elif "change name" in query:
			speak("What would you like to call me, Sir ")
			assname = takeCommand()
			speak("Thanks for naming me")

		elif "what's your name" in query or "What is your name" in query:
			speak("My friends call me David")
			

		elif 'exit' in query:
			speak("Thanks for giving me your time and you also call me again")
			exit()

		elif 'say positive word about me' in query:
			speak("Yes of course I have lot of word to say you first you are positive minded and always see the good in others. Second is You are a goal chaser, you don’t give up until you achieve your goal goals.")
			speak("That’s enough now I can not lie more")
 
		
		elif "who developed you" in query:
			speak("I have Developed by 5 student of BCA Group at naraina collage of managment frist student is Atol singh second is khoshi shukla third is Manvendra singh fourth is Pooja Pal and fifth is Naavyaa Panday")
		
		elif "what is voice assistant" in query:
			speak("A voice assistantis a digital assistant that uses voice recognition, language processing algorithms, and voice synthesis to listen to specific voice commands and return relevant information or perform specific functions as requested by the user.")

		elif "about naraiana group of institution" in query or "about our campus" in query:
			speak("our campus Naraina Group of Institutions (NGI ) established in 2007 at Ratanpur and Gangaganj, Panki, Kanpur; is a self-financed Institute, offering world class standard of education to students from all corners of the country. ")
		
		elif "about chhatrapati shahu ji maharaj university" in query or "about our university" in query:
			speak("Our University Chhatrapati Shahu Ji Maharaj University stands as a hallmark of higher education. It is an educational community where students of various religions and cultural backgrounds study and work together in a congenial atmosphere ")
		
		elif "saying abuse" in query:
			speak("Sorry, I don’t understand what you’re saying. I don’t speak bullsh*t.")
		
		
		elif "how was your day" in query:
			speak("Depends who you ask, if you ask me, it was fine")
	
		
		elif "what is machine learning" in query:
			speak("Machine Learning : We feed in DATA (Input) + Output, run it on machine during training and the machine creates its own program (logic), which can be evaluated while testing. What does exactly learning means for a computer")
		
		elif "what are you doing" in query:
			speak("Trying to remember the name of that weird person you remind me of.")
		
		elif "what is ai" in query or "what is artificial intelligence" in query:
			speak("Artificial intelligence (AI) is the science of using a machine to automate tasks that would otherwise be performed by a human")
			
		elif 'joke' in query:
			speak(pyjokes.get_joke())
			

		elif 'search' in query or 'play' in query:
			
			query = query.replace("search", "")
			query = query.replace("play", "")		
			webbrowser.open(query)


		
		elif "who is alexa" in query:
			speak("Alexa, is a virtual assistant technology largely based on a Polish speech synthesiser named Ivona, bought by Amazon in 2013. many people us alexa but I don't like him")

		elif "who i am" in query:
			speak("If you talk me then definitely you are human.")


		elif "tell me about something yourself" in query:
			speak("I am david ! personal AI assistant which Developed by 5 student of BCA Group at naraina collage of managment frist student is Atol singh second is khoshi shukla third is Manvendra singh fourth is Pooja Pal and fifth is Naavyaa Panday")
      
		



		elif 'change background' in query:
			ctypes.windll.user32.SystemParametersInfoW(20,
													0,
													"Location of wallpaper",
													0)
			speak("Background changed successfully")

		

		
		elif 'lock window' in query:
				speak("locking the device")
				ctypes.windll.user32.LockWorkStation()

		elif 'shutdown system' in query:
				speak("Hold On a Sec ! Your system is on its way to shut down")
				subprocess.call('shutdown / p /f')
				
		elif 'empty recycle bin' in query:
			winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
			speak("Recycle Bin Recycled")

		elif "don't listen" in query or "stop listening" in query:
			speak("for how much time you want to stop jarvis from listening commands")
			a = int(takeCommand())
			time.sleep(a)
			print(a)



		elif "restart" in query:
			subprocess.call(["shutdown", "/r"])
			
		elif "hibernate" in query or "sleep" in query:
			speak("Hibernating")
			subprocess.call("shutdown / h")

		elif "log off" in query or "sign out" in query:
			speak("Make sure all the application are closed before sign-out")
			time.sleep(5)
			subprocess.call(["shutdown", "/l"])
        
	
	





		
