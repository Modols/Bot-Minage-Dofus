import pyautogui
import time
import keyboard
import random
import win32api
import win32con

png = 'minerai_fer_minimize.png'
regi = "region=(300, 50, 1300, 980)"
confi = "confidence=0.7"


time.sleep(2)


def click(x, y):
    win32api.SetCursorPos((x, y))
    pyautogui.keyDown('shift')
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    # pyautogui.click(button='left')
    pyautogui.keyUp('shift')


def locate(p, r, c):
    return pyautogui.locateCenterOnScreen(p, r, c)


while keyboard.is_pressed('q') == False:
    if pyautogui.locateOnScreen('minerai_fer_minimize.png', region=(300, 50, 1300, 980), confidence=0.7) != None:
        x, y = pyautogui.locateCenterOnScreen(
            'minerai_fer_minimize.png', region=(300, 50, 1300, 980), confidence=0.7)
        click(x, y)
        time.sleep(14)
        click(1005, 565)
        # click(980, 410)
