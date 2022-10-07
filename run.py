# from logging import exception
# import pyautogui

# import os
# from lsHotword import ls
# def swich():
#     pyautogui.keyDown("alt")
#     pyautogui.press("tab")
#     pyautogui.keyUp("alt")
# while True:
#     try:

#         print("speak activate")
#         ls.lsHotword_loop()
#         print("OK")
#     except exception as e:
#         print(e)
#     print("OK")
import os
os.system("taskkill /f /im Media Player") 