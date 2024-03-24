import os
import time
import pyautogui
import psutil

def check_if_process_running(process_name):
    for process in psutil.process_iter(['name']):
        if process.info['name'] == process_name:
            return True
    return False

pyautogui.useImageNotFoundException()

a = 0
b = 0

os.startfile("steam://rungameid/200210")

while a <= 120:
    try:
        location = pyautogui.locateOnScreen('play.png')
        pyautogui.click(location)
        break
    except pyautogui.ImageNotFoundException:
        try:
            location = pyautogui.locateOnScreen('update.png')
            pyautogui.click(location)
        except pyautogui.ImageNotFoundException:
            pass
        a += 1
        time.sleep(1)

while b <= 120:
    if check_if_process_running('RotMG Exalt.exe'):
        os.system('TASKKILL /F /IM "steam.exe"')
        os.system('TASKKILL /F /IM "RotMG Exalt Launcher.exe"')
        break
    else:
        b += 1
        time.sleep(1)
