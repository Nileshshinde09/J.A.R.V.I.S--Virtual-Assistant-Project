# importing packages
import sys
import ctypes
import speech_recognition as speech

# define function
def fxn():

	# voice recognizer object
	voice = speech.Recognizer()

	# use microphone
	with speech.Microphone() as source:
		print("Say something!")
		voice_command = voice.listen(source)

	# check input
	try:
		command = voice.recognize_google(voice_command)
		print(command)
		
	# handle the exceptions
	except speech.UnknownValueError:
		print("Google Speech Recognition system could not\
		understand your instructions please give instructions carefully")
		
	except speech.RequestError as e:
		print(
			"Could not request results from Google Speech Recognition \
			service; {0}".format(e))

	# validate input
	if command == "nick":
		# ctypes.windll.user32.LockWorkStation()
		return 1
		
	elif command == "stop":
		sys.exit(0)
		
	else:
		print("Not a command.")
		fxn()

fxn()
