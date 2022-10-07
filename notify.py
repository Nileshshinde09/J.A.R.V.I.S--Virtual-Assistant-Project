import pyttsx3
import requests
import json
from speak_function import *
if __name__ == '__main__':
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)

	

def pushbullet_noti(title, body):
		
	TOKEN = 'o.0UCA5JmQFdhmLYvdMN40VQfLGbneaumJ'
	msg = {"type": "note", "title": title, "body": body}
	resp = requests.post('https://api.pushbullet.com/v2/pushes',
						data=json.dumps(msg),
						headers={'Authorization': 'Bearer ' + TOKEN,
								'Content-Type': 'application/json'})
	if resp.status_code != 200:
			raise Exception('Error', resp.status_code)
	else:
			print('Message sent')
			speak("message sent")

def pushbullet_silent(title, body):
		
	TOKEN = 'o.0UCA5JmQFdhmLYvdMN40VQfLGbneaumJ'
	msg = {"type": "note", "title": title, "body": body}
	resp = requests.post('https://api.pushbullet.com/v2/pushes',
						data=json.dumps(msg),
						headers={'Authorization': 'Bearer ' + TOKEN,
								'Content-Type': 'application/json'})
	if resp.status_code != 200:
			raise Exception('Error', resp.status_code)

             
