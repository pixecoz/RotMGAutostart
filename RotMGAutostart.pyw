import os
import time
import pyautogui
import psutil

# You can change this value to "False" if you want to keep the steam app running
# Default value is "True"
KILL_STEAM = True

def check_if_process_running(process_name):
    for process in psutil.process_iter(['name']):
        if process.info['name'] == process_name:
            return True
    return False

def script():
    CLICKED = 0
    while check_if_process_running('RotMG Exalt Launcher.exe') or CLICKED < 2:
        try:
            if CLICKED < 2:
                click_location = pyautogui.locateOnScreen('play.png', confidence=0.8)
                pyautogui.click(click_location)
                CLICKED = 2
        except pyautogui.ImageNotFoundException:
            try:
                if CLICKED == 0:
                    click_location = pyautogui.locateOnScreen('update.png', confidence=0.8)
                    pyautogui.click(click_location)
                    CLICKED = 1
            except pyautogui.ImageNotFoundException:
                pass
        finally:
            if check_if_process_running('RotMG Exalt.exe'):
                time.sleep(20)
                if KILL_STEAM:
                    os.system('TASKKILL /F /IM "steam.exe"')
                os.system('TASKKILL /F /IM "RotMG Exalt Launcher.exe"')
                break
            time.sleep(1)

def start_script():
    pyautogui.useImageNotFoundException()
    os.startfile("steam://rungameid/200210")
    script()

if __name__ == "__main__":
    start_script()
