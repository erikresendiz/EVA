from gtts import gTTS
from playsound import playsound

def speak(mytext):
    #Uses googles T2P which sounds much better
    language = 'en'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save("EVA_AUDIO.mp3")
    playsound('EVA_AUDIO.mp3')