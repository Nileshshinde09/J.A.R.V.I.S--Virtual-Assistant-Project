from ast import Break
from unittest import main
from geo_location import send_location
import urllib.request

def connect(host):
    try:
        urllib.request.urlopen(host)
        return True
    except:
        return False

if __name__ == "__main__":
    while(True):
        h = "http://google.com"
        if(connect(h)==True):
            send_location()
            Break


