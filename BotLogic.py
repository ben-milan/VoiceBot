import pyautogui
import time
import win32gui



def get_browser_handle():
    # Adjust the title to match your browser window title
    browser_title = "Google Chrome"
    handle = win32gui.FindWindow(None, browser_title)
    return handle


def bring_to_front(handle):
    win32gui.ShowWindow(handle, 5)  # SW_SHOW
    win32gui.SetForegroundWindow(handle)


def main():
    time.sleep(2)

    # Get the handle of the browser window
    browser_handle = get_browser_handle()

    # Bring the browser window to the front
    bring_to_front(browser_handle)
    pyautogui.hotkey('ctrl', 't')


def openWebsite():
    time.sleep(2)

    # Simulate pressing Ctrl + T to open a new tab
    pyautogui.hotkey('ctrl', 't')


if __name__ == '__main__':
    main()
