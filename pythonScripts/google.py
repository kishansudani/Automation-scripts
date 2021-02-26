import pyttsx3
import speech_recognition as sr
import datetime
from selenium import webdriver
import os


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# use 0,1.. for chaning the voice
engine.setProperty('voice', voices[0].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()



def takeCommand():
    #It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("User said: \n",query)
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query



class google:
    def __init__(self):
        # enter the path of the chrome driver
        self.driver = webdriver.Chrome(executable_path=f'{path_value}chromedriver.exe')
        self.driver.get("https://www.google.com")

    def searchGoogle(self,qq):
        self.driver.find_element_by_xpath("//input[@name=\"q\"]").send_keys(qq)
        self.driver.find_element_by_xpath('//input[@type="submit"]').click()


if __name__ == "__main__"
	speak("do you want to search anything??")
	q = takeCommand().lower()
	if q is "yes":
	    my.searchGoogle(q)