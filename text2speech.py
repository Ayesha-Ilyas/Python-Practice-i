from gtts import gTTS
import os
f=open('t.txt')
x=f.read()
language='en'
audio=gTTS(text=x,lang=language,slow=False)
audio.save("t.wav")
os.system("t.wav")
