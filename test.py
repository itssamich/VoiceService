import speech_recognition as sr
import pyttsx3
import sys
from datetime import datetime
from datetime import date


#TODO:
#Google searching with string from user like with wikipedia?
#Alexa-esque start up..."Alexa...What's..." but with a different name obviously. Kind of done, may have a simpler/better solution since this current one was made at 5 AM
#The original plan was gif searching but this could be a lot more fun
#Find a better TTS service or learn how to change the voice , I don't like the default voice
#Create a check for 2 valid variables in the operator section



r = sr.Recognizer()
engine = pyttsx3.init() #Text-to-Speech library
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id) #0 is the default male voice, the female voice has some weird issues with speech. Like when saying "is" she pronouses it "i s". 1 is the female voice

#This loop allows for the program to always be listening but it won't process any data until the keyword is spoken. For now this is "Computer...". I didn't notice any memory problems or any other issues but let me know if something I didn't notice occurs
while True:
    # Uses the current system microphone to recieve a single string of input
    with sr.Microphone() as source:
        print("start")
        audio = r.listen(source)
    #Checks if there is currently input for the program to pass through google. Catches the error for when there is no valid speech recognized, then it continues the loop to allow for continous listening
    try:
        voiceString = r.recognize_google(audio).lower()
    except:
        print("Not Requested")
        continue
    
    #Checks if the words spoken are meant to for the computer to process
    if "computer" in voiceString:
        
        #This splits the string by head(the part before the word 'computer'), sep(the word 'computer), and voiceString/tail(everything after the word 'computer')
        head, sep, voiceString = voiceString.partition('computer')

        #Allows user to cancel the processing of their voice clip if contains "cancel" in the string
        if "cancel" not in voiceString:
            try:
                #For now this just prints out what google voice recognition services thinks was said and then has pyttsx3 read aloud what was saved by google
                print("User: \"" + voiceString + "\"")

                #Sets current time in Hour:Minute:Second format, 24 hr clock is used(i.e. 10:41 P.M. would be 22:41)
                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")

                #Sets current date in FullMonth NumericalDate, 4 digit year format. Like June 06, 2021
                today = date.today()
                d2 = today.strftime("%B %d, %Y")
                
                
                #eval() could be abusable and as such is not a safe method if input is trusted. I think the operator check would suffice to ensure that a valid input is being processed. Can evaluate later
                #This does not check for a second variable, much less a first. Only looks for the math operator to be involved. Will crash if no valid variables are given. Will work on checks later
                if "+" in voiceString or "-" in voiceString or "*" in voiceString or "/" in voiceString: #Basic math operations
                    stringtest = voiceString.replace("what's ", "")
                    stringtest = stringtest.replace("what is ", "")
                    print("Computer: \"" + stringtest + " is " + str(eval(stringtest)) + "\"")
                    engine.say(stringtest + "is ")
                    engine.say(eval(stringtest))
                elif "time" in voiceString: #Current time requests
                    print("Computer: \"It is " + current_time + "\"")
                    engine.say("It is ")
                    engine.say(current_time)
                elif "the date" in voiceString or "day is" in voiceString: #Current date requests
                    print("Computer: \"It is " + d2 + "\"")
                    engine.say("It is ")
                    engine.say(d2)
                elif "exit program" in voiceString: #Ends the program's continous listening
                    break

                engine.runAndWait()

            except sr.UnknownValueError:
                print("Google could not understand audio")
            except sr.RequestError as e:
                print("Could not get results; {0}".format(e))
    else:
        print("Not Requested")
        continue
