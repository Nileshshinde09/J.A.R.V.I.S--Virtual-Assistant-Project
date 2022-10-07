import speech_recognition as sr  
r = sr.Recognizer()
with sr.Microphone() as source:
  print("Listening...")
  r.pause_threshold = 1
  audio = r.listen(source)
try:  
   print("Sphinx thinks you said '" + r.recognize_google(audio))  
except sr.UnknownValueError:  
   print("Sphinx could not understand audio")  
except sr.RequestError as e:  
   print("Sphinx error; {0}".format(e))