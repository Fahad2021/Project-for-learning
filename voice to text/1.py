from gtts import gTTS
import os
f=open("1.txt")
x=f.read()
lanuage='bn'
audio=gTTS(text=x,lang=lanuage,slow=False)
audio.save("1.wav")
os.system("1.wav")