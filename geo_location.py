from ast import Break
import string
from unittest import main
import urllib.request
from pip import main
import requests
import json
from notify import pushbullet_noti
from geopy.geocoders import Nominatim
import threading

		

def connect(host):
    try:
        urllib.request.urlopen(host)
        return True
    except:
        return False

def start():
    while(True):
        h = "http://google.com"
        if(connect(h)==True):
            send_location()
            Break
def send_location():
        loc = Nominatim(user_agent="GetLoc")
        getLoc = loc.geocode("Gosainganj Lucknow")

        title = "computer location"
        body = getLoc.address
        pushbullet_silent(title, body)
        t = "Latitude"
        b = getLoc.latitude
        b_ = str(b)
        pushbullet_silent(t, b_)

        ti = "Longitude"
        bdy = getLoc.longitude
        bdy_ = str(bdy)
        pushbullet_silent(ti, bdy_)


def pushbullet_silent(title, body):
		
	TOKEN = 'o.0UCA5JmQFdhmLYvdMN40VQfLGbneaumJ'
	msg = {"type": "note", "title": title, "body": body}
	resp = requests.post('https://api.pushbullet.com/v2/pushes',
						data=json.dumps(msg),
						headers={'Authorization': 'Bearer ' + TOKEN,
								'Content-Type': 'application/json'})
	if resp.status_code != 200:
			raise Exception('Error', resp.status_code)
            
        


