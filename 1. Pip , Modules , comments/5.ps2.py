#install text to speech module and try
import pyttsx3

engine = pyttsx3.init()
engine.say("Hello Shivam")
engine.runAndWait()