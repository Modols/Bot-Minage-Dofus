import pyautogui
import time
import keyboard
import random
import win32api
import win32con


posAmakna = [
    [1005, 565],
    [1149, 495],
    [1103, 520],
    [959, 539],
    [1242, 445],
    [864, 589]]
posSadi = [[959, 444]]
pos = [[957, 538]]
# [959, 349],
posSplitted = [[1436, 548]]

fullScreen = (300, 50, 1300, 980)
splitedScreen = (1100, 250, 700, 350)


class Bot:
    def __init__(self, tabPos, regg):
        # ajouter les différents pngs
        self.pngs = ["minerai_fer_minimize.png",
                     "minerai_cuivre_minimize.png"]
        # self.pngs = ["kobalt.png"]
        # self.pngs = ["bronze_splitted.png",
        #              "bronze_splitted_2.png", "bronze_splitted_3.png"]
        # self.pngs = ["bronze.png", "bronze_2.png",
        #              "other_bronze.png", "bronze_3.png"]
        # ajouter la liste des positions où le bot se replace automatiquement
        # self.returnPosition = [[1005, 565], [948, 421]] [959, 349]
        # "minerai_fer_minimize.png",
        #                  "minerai_cuivre_minimize.png",
        self.returnPosition = tabPos
        self.reg = regg

    def start(self):
        # lance la boule infinie
        # faire boucle for pour tout le tableau
        # check if echange ou if passage de niveau
        # check if pods > jsp combien go to banque

        time.sleep(2)
        while keyboard.is_pressed('q') == False:
            # 1300, 980
            for png in self.pngs:
                if self.locateScreen(png, self.reg, 0.73) != None:
                    x, y = self.locateCenter(png, self.reg, 0.73)
                    self.click(x, y)
                    time.sleep(11)
                    self.goToRandomPosition()
                    print(png)

    def locateScreen(self, png, tupleRegion, tauxConfidence):
        try:
            return pyautogui.locateOnScreen(png, region=tupleRegion,  confidence=tauxConfidence)
        except TypeError:
            print("ça à planté")
            self.locateScreen(png, region=tupleRegion,
                              confidence=tauxConfidence)

    def locateCenter(self, png, tupleRegion, tauxConfidence):
        return pyautogui.locateCenterOnScreen(png, region=tupleRegion,  confidence=tauxConfidence)

    def click(self, x, y):
        # fonction click
        win32api.SetCursorPos((x, y))
        pyautogui.keyDown('shift')
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
        pyautogui.keyUp('shift')

    def goToRandomPosition(self):
        # va chercher un point et le retourne avec un time sleep
        lenghtListePosition = len(self.returnPosition)
        randNumber = random.randint(0, lenghtListePosition-1)
        self.click(self.returnPosition[randNumber]
                   [0], self.returnPosition[randNumber][1])
        time.sleep(0.5)

    def getPosition(self):
        pyautogui.displayMousePosition()


# bot1 = Bot(posSplitted, splitedScreen)
bot1 = Bot(pos, fullScreen)
bot1.start()
# bot1.getPosition()

# TypeError: cannot unpack non-iterable NoneType object
