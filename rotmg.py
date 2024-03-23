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

count1 = 0
count2 = 0

os.startfile("steam://rungameid/200210")

while True:
    try:
        location = pyautogui.locateOnScreen('play.png')
        print('*Clicks*')
        break
    except pyautogui.ImageNotFoundException:
        print(f'Please wait. Time elapsed: {count1} seconds')
        count1 += 1
        time.sleep(1)

pyautogui.click(location)

while True:
    if check_if_process_running('RotMG Exalt.exe'):
        os.system('TASKKILL /F /IM "steam.exe"')
        os.system('TASKKILL /F /IM "RotMG Exalt Launcher.exe"')
        break
    else:
        print(f'Closing Steam and Launcher, Please wait. Time elapsed: {count2} seconds')
        count2 += 1
        time.sleep(1)