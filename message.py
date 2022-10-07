try:
    from logging import exception
    import pywhatkit
    import pyautogui
    def send(number,message):
        pywhatkit.sendwhatmsg_instantly(number, message,5,True,2)
        pyautogui.press("enter")
        

    def send_message(query,msg):
    
            if 'Atul' in query:
                send("+917996943966",msg)
            elif 'Ajit sir' in query:
                send("+918660581597",msg)
            elif 'Sakshi' in query:
                send("+918108377248",msg)
            elif 'Dhondiba' in query:
                send("+91702823074",msg)
            elif 'Abhi' in query:
                send("+918308930142",msg)
except exception:
    pass

    
    