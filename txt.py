from gtts import gTTS

import os

f=open('result.txt')
x=f.read()

language= 'en'

audio=gTTS(text=x, lang=language, slow=False)

audio.save("res.wav")
os.system("res.wav")

