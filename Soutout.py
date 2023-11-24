import win32com.client as w
Speaker=w.Dispatch("SAPI.SpVoice")
# import speech_recognition as sr
listOfMembers=["Hardik Baral",
"Leslie Melendez",
"Christa Herman",
"Jake Haley",
"Evelyn Casey",
"Marvin Gregory",
"Jessica Lamb",
"Ted Bartlett",
"Sonja Park",
"Sandi Marshall",
"Caroline Morrison",
"Virgil Clayton",
"Keri McDowell",
"Jenny Fernandez",
"Anita Mercer",
"Jessie Robbins",
"Cynthia Nixon",
"Paige Fritz",
"Bruce Loyd",
"Devin McMillan"]

for name in listOfMembers:
    print(f"SHOUT OUT TO {name}")
    Speaker.speak(f"SHOUT OUT TO {name}")
    









# speaker = w.Dispatch("SAPI.SpVoice")
# r = sr.Recognizer()
# with sr.Microphone() as source:
#     print('Listening...')
#     audio = r.listen(source)
#     print(audio)
#     txt=r.recognize_google(audio)
#     print("YOu said:",txt)
#     speaker.Speak("You said "+txt)

# speaker.Speak("hi ,Hardik what are you writting")
