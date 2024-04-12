import pyautogui
import webbrowser
import time
from AudioProccessing import *


def main():
    openWebsite()
    searchEvent()
    time.sleep(3)
    orderProcesse()


def pressButton(url):
    x, y = pyautogui.locateCenterOnScreen(url, confidence=0.8)
    pyautogui.moveTo(x, y, 0.5)
    pyautogui.click()


def openWebsite():
    time.sleep(2)
    webbrowser.open("https://www.ticketcorner.ch")
    time.sleep(3)


def searchEvent():
    speak_text("Welches Event suchen Sie?")
    searchEntry = listen_text()
    pressButton("img/Search.png")
    pyautogui.write(searchEntry)
    time.sleep(3)
    pyautogui.hotkey('enter')


def orderProcesse():
    pressButton("img/EventButton.png")
    time.sleep(3)
    pressButton("img/OrderTicket.png")
    time.sleep(3)
    pressButton("img/continue_button.png")


if __name__ == '__main__':
    main()
