import speech_recognition as sr
import pyttsx3

#TODO:
#Add Basic Math Operators(i.e. + = "add", - = "subtract", * = "times", / = "divided by"... etc. String requirements to follow)
#Google searching with string from user?
#Alexa-esque start up..."Alexa...What's..." but with a different name obviously
#The original plan was gif searching but this could be a lot more fun

r = sr.Recognizer()
engine = pyttsx3.init() #Text-to-Speech library


# Uses the current system microphone to recieve a single string of input
with sr.Microphone() as source:
    print("start")
    audio = r.listen(source)
voiceString = r.recognize_google(audio)

#Allows user to cancel the processing of their voice clip if contains "cancel" in the string
if "cancel" not in voiceString:
    try:
        #For now this just prints out what google voice recognition services thinks was said and then has pyttsx3 read aloud what was saved by google
        print("Google thinks I said \"" + voiceString + "\"")
        engine.say(voiceString)
        engine.runAndWait()
    except sr.UnknownValueError:
        print("Google could not understand audio")
    except sr.RequestError as e:
        print("Could not get results; {0}".format(e))

