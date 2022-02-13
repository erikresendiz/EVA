#imported Modules
import speech_recognition
import pyttsx3
from speak import speak
from connection_check import connect
from number_operation import num_am
#Text to Speech Modules
#engine = pyttsx3.init()
#engine.setProperty('voice', 'english_rp+f3')
#engine.setProperty('rate', 147)

#def offline_speak(mytext):
#uses pyttsx3's T2S (but like tbh it sounds really bad)
#    engine.say(mytext)
#    engine.runAndWait()

#def online_speak(mytext):
#    #Uses googles T2P which sounds much better
#    language = 'en'
#    myobj = gTTS(text=mytext, lang=language, slow=False)
#    myobj.save("EVA_AUDIO.mp3")
#    playsound('EVA_AUDIO.mp3')

#def connect(host='http://google.com'):
#    #makes sure there's and internet connection
#    #currently this is useless as it uses googles online voice recognition
#    #am trying to get an offline voice recognition to work
#    try:
#        urllib.request.urlopen(host) #Python 3.x
#        return True
#    except:
#        return False

con_stat = connect()

#sets the speak function to either use the offline or online T2S
#if con_stat == False:
#    def speak(mytext):
#        offline_speak(mytext)
#    speak("System Offline")
#else:
#    def speak(mytext):
#        online_speak(mytext)
#    speak("System Online")

#Speech Recognition
recognizer = speech_recognition.Recognizer()

#Action Functions
#def num_am(command, operation):
#    #splits string into words
#    split_cmd = command.split(" ")
    #sum or product of prevous numbers in for loop
#    prev = 0
#    for word in split_cmd:
        #tries to turn word into a number
#        try: 
#            word_int = int(word)
#            if operation == "add":
#                prev = word_int + prev
#            if operation == "mult":
#                prev = word_int * (prev + 1)
#        #if word can't be converted into an int it's passed
#        except:
#            pass
#    return str(prev)

#Eva Loop
while True:

    try:
        with speech_recognition.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)

            #Uses googles voice recogniton
            text = recognizer.recognize_google(audio)
            text = text.lower() #makes all text lowercase
            print(f"Recognized {text}") #prints recognized text (makes troubleshooting easier)
            
            #Makes bye the word to turn off system
            if "bye" in text:
                break
            #checks if calculate is in recongized text
            if "calculate" in text:
                #if there's a plus symbol '+' in recongized text it adds all the numbers
                if "+" in text:
                    speak(num_am(text, "add"))  
                #does the same but for multiplcation
                if "*" in text:
                    speak(num_am(text, "mult"))
    except:
        recognizer = speech_recognition.Recognizer()
        print("Didn't quite catch that")
    