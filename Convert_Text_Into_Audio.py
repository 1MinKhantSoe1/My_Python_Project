from gtts import gTTS
from playsound import playsound

audio = 'speech.mp3'  # output file name
language = 'en'
text = input("Please enter a speech that you want to convert into audio : ")
sp = gTTS(text=text, lang=language, slow=False)

sp.save(audio)
playsound(audio)
