import speech_recognition as sr

r=sr.Recognizer()

a=sr.AudioFile('hello.wav')
with a as source :
	audio=r.record(source)

text=r.recognize_google(audio)


file1=open(r"E:\c,c++,py\python\Visual Stdio\spech recognizer.txt","a")
file1.writelines(text)
file1.close()