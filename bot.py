from pyautogui import * 
import pyautogui
import time
import keyboard
import random
import win32api, win32con

# pip install the above!


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:
    if pyautogui.pixel(440, 850) [0] == 0:
        click(440, 850)
    if pyautogui.pixel(570, 850) [0] == 0:
        click(570, 850)
    if pyautogui.pixel(700, 850) [0] == 0:
        click(700, 850)
    if pyautogui.pixel(860, 850) [0] == 0:
        click(860, 850)