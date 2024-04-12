import pyautogui
import time


def main():
    openWebsite()


def openWebsite():
    time.sleep(2)

    # Simulate pressing Ctrl + T to open a new tab
    pyautogui.hotkey('ctrl', 't')
    pyautogui.write("https://www.ticketcorner.ch")
    pyautogui.hotkey('enter')
    time.sleep(2)

    x, y = pyautogui.locateCenterOnScreen("img/Search.png", confidence=0.9)
    pyautogui.moveTo(x, y, 1)
    pyautogui.click()
    pyautogui.write("Knie")


if __name__ == '__main__':
    main()